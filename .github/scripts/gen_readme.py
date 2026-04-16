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
        'problem_url': '',
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
    if has_number:
        match = re.match(r'^(\d+)[_\-\s](.+)$', stem)
        if match:
            return match.group(1), match.group(2).replace('_', ' ')
        if stem.isdigit():
            return stem, ''
    return '', stem.replace('_', ' ')


def collect(platform: str, meta: dict) -> list:
    folder = ROOT / platform
    if not folder.exists():
        return []
    results = []
    for py_file in sorted(folder.rglob('*.py')):
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


def make_two_column_table(problems: list, meta: dict) -> list:
    """문제 목록을 2열 마크다운 표로 변환. 제목에 풀이 링크 포함."""
    has_number = meta['has_number']
    url_tpl    = meta.get('problem_url', '')

    def num_cell(p):
        if not p['number']:
            return ''
        return f'[{p["number"]}]({url_tpl.format(p["number"])})' if url_tpl else p['number']

    def title_cell(p):
        title = p['title'] if p['title'] else p['number'] if p['number'] else '-'
        return f'[{title}]({p["path"]})'

    lines = []
    if has_number:
        lines.append('| 번호 | 제목 | &nbsp;&nbsp;&nbsp; | 번호 | 제목 |')
        lines.append('|:---:|:---|---|:---:|:---|')
    else:
        lines.append('| 제목 | &nbsp;&nbsp;&nbsp; | 제목 |')
        lines.append('|:---|---|:---|')

    for i in range(0, len(problems), 2):
        left  = problems[i]
        right = problems[i + 1] if i + 1 < len(problems) else None

        if has_number:
            ln = num_cell(left)
            lt = title_cell(left)
            rn = num_cell(right)   if right else ''
            rt = title_cell(right) if right else ''
            lines.append(f'| {ln} | {lt} | | {rn} | {rt} |')
        else:
            lt = title_cell(left)
            rt = title_cell(right) if right else ''
            lines.append(f'| {lt} | | {rt} |')

    return lines


def make_collapsible(summary: str, content_lines: list) -> list:
    return [
        '<details>',
        f'<summary>{summary}</summary>',
        '',
        *content_lines,
        '',
        '</details>',
        '',
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
        table  = make_two_column_table(problems, meta)
        summary = f'📂 {meta["name"]} &nbsp;·&nbsp; {len(problems)}문제'
        lines.extend(make_collapsible(summary, table))

    if concepts:
        lines.append('---\n')
        lines.append('## 개념 정리\n')
        concept_lines = [
            '| 주제 | 링크 |',
            '|:---|:---:|',
            *[f'| {c["name"]} | [정리]({c["path"]}) |' for c in concepts],
        ]
        lines.extend(make_collapsible(
            f'📖 개념 정리 &nbsp;·&nbsp; {len(concepts)}개',
            concept_lines,
        ))

    lines += [
        '---\n',
        '## Best Practice\n',
        '1. **가독성 우선** — 변수명은 `a, b` 대신 `node_count`, `is_visited`처럼 직관적으로',
        '2. **효율성 체크** — 시간복잡도 O(N)을 항상 계산하고 제출',
        '3. **기록의 힘** — 왜 이 알고리즘을 선택했는지 주석으로 생각의 흐름 남기기\n',
        '---\n',
        '<p align="right"><em>"가독성 우선, 효율성 체크, 기록의 힘"</em></p>\n',
    ]

    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    all_problems = {p: collect(p, m) for p, m in PLATFORMS.items()}
    concepts     = collect_concepts()
    readme       = render(all_problems, concepts)

    with open(ROOT / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

    total = sum(len(v) for v in all_problems.values())
    print(f'README.md 업데이트 완료 — 총 {total}문제, 개념 {len(concepts)}개')