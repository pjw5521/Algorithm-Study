def solution(genres, plays):
    answer = []
    genre_count = {}
    song = []

    for i in range(len(genres)):
        if genres[i] not in genre_count:
            genre_count[genres[i]] = plays[i]
        else:
            genre_count[genres[i]] += plays[i]
        song.append([genres[i], plays[i], i])

    genre_count = sorted(genre_count.items(), key=lambda item: -item[1])
    song = sorted(song, key=lambda x: (x[0], -x[1], x[2]))

    for i in genre_count:
        cnt = 0
        for j in range(len(song)):
            if cnt == 2:
                break
            if i[0] == song[j][0]:
                answer.append(song[j][2])
                cnt += 1

    return answer

