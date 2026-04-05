def solution(genres, plays):
    answer = []
    
    # 장르별 총 재생수, 곡 목록 집계
    genre_total = {}
    genre_songs = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] = genre_total.get(g, 0) + p
        if g not in genre_songs:
            genre_songs[g] = []
        genre_songs[g].append((p, i))
    
    # 장르 총 재생수 내림차순 정렬
    sorted_genres = sorted(genre_total, key=lambda x: -genre_total[x])
    
    for g in sorted_genres:
        # 재생수 내림차순, 같으면 고유번호 오름차순으로 최대 2곡
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))
        for p, i in songs[:2]:
            answer.append(i)
    
    return answer