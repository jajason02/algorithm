"""
Algorithm 리포지토리 README 자동 생성 스크립트

파일명 규칙:
  baekjoon/    → 2603_색종이.py       (번호_제목.py)
  programmers/ → 두_개_뽑아서_더하기.py (제목.py, 번호 없음)
  SWEA/        → 1234_파리퇴치.py      (번호_제목.py)
  algoalgo_arena/ → 임의 파일명 허용

실행: python .github/scripts/generate_readme.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent

PLATFORMS = {
    'baekjoon': {
        'name': 'Baekjoon',
        'has_number': True,
        'problem_url': 'https://www.acmicpc.net/problem/{}',
    },
    'SWEA': {
        'name': 'SWEA',
        'has_number': True,
        'problem_url': '',  # SWEA는 URL 구조가 복잡해서 생략
    },
    'programmers': {
        'name': 'Programmers',
        'has_number': False,
        'problem_url': '',
    },
    'algoalgo_arena': {
        'name': 'AlgoAlgo 스터디',
        'has_number': False,
        'problem_url': '',
    },
}


def parse_filename(stem: str, has_number: bool) -> tuple[str, str]:
    """
    파일명(확장자 제외)에서 (번호, 제목) 파싱.

    has_number=True  → '2603_색종이'    → ('2603', '색종이')
    has_number=False → '두_개_뽑아서'   → ('', '두 개 뽑아서')
    """
    if has_number:
        match = re.match(r'^(\d+)[_\-\s](.+)$', stem)
        if match:
            number = match.group(1)
            title = match.group(2).replace('_', ' ')
            return number, title
        # 번호만 있는 경우 (제목 없음)
        if stem.isdigit():
            return stem, ''
    # 번호 없는 경우 or 파싱 실패
    title = stem.replace('_', ' ')
    return '', title


def collect(platform: str, meta: dict) -> list:
    folder = ROOT / platform
    if not folder.exists():
        return []

    results = []
    for py_file in sorted(folder.rglob('*.py')):
        # __init__.py 등 제외
        if py_file.stem.startswith('__'):
            continue

        number, title = parse_filename(py_file.stem, meta['has_number'])
        results.append({
            'number': number,
            'title':  title,
            'path':   py_file.relative_to(ROOT),
        })

    return results


def collect_concepts() -> list:
    folder = ROOT / 'Concepts'
    if not folder.exists():
        return []
    return [
        {'name': f.stem.replace('_', ' '), 'path': f.relative_to(ROOT)}
        for f in sorted(folder.glob('*.md'))
        if f.name != 'README.md'
    ]


def render(all_problems: dict, concepts: list) -> str:
    total = sum(len(v) for v in all_problems.values())

    lines = [
        '# Algorithm\n',
        '알고리즘 문제 풀이 및 개념 정리 저장소입니다.  ',
        'Python으로 작성하며, 꾸준한 풀이와 기록을 목표로 합니다.\n',
        '<p>',
        '  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />',
        '</p>\n',
        '---\n',
        '## 목표\n',
        '- [ ] SWEA B형 취득',
        '- [x] 백준 일관적 풀이 습관 형성',
        '- [ ] 주요 알고리즘 개념 전체 정리\n',
        '---\n',
        f'## 문제 풀이 현황 — 총 {total}문제\n',
    ]

    for platform, meta in PLATFORMS.items():
        problems = all_problems.get(platform, [])
        if not problems:
            continue

        lines.append(f'### {meta["name"]} ({len(problems)})\n')

        if meta['has_number']:
            lines.append('| 번호 | 제목 | 풀이 |')
            lines.append('|:---:|:---|:---:|')
            for p in problems:
                url = meta['problem_url'].format(p['number']) if meta['problem_url'] and p['number'] else ''
                num_str = f'[{p["number"]}]({url})' if url else p['number']
                title_str = p['title'] if p['title'] else '-'
                lines.append(f'| {num_str} | {title_str} | [풀이]({p["path"]}) |')
        else:
            lines.append('| 제목 | 풀이 |')
            lines.append('|:---|:---:|')
            for p in problems:
                title_str = p['title'] if p['title'] else p['path'].stem
                lines.append(f'| {title_str} | [풀이]({p["path"]}) |')

        lines.append('')

    if concepts:
        lines.append('---\n')
        lines.append(f'## 개념 정리 ({len(concepts)})\n')
        lines.append('| 주제 | 링크 |')
        lines.append('|:---|:---:|')
        for c in concepts:
            lines.append(f'| {c["name"]} | [정리]({c["path"]}) |')
        lines.append('')

    lines.append('---\n')
    lines.append('<p align="right"><em>"가독성 우선, 효율성 체크, 기록의 힘"</em></p>\n')

    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    all_problems = {p: collect(p, m) for p, m in PLATFORMS.items()}
    concepts = collect_concepts()
    readme = render(all_problems, concepts)

    with open(ROOT / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

    total = sum(len(v) for v in all_problems.values())
    print(f'README.md 업데이트 완료 — 총 {total}문제, 개념 {len(concepts)}개')
