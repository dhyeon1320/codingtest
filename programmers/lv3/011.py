def solution(genres, plays):
    answer = []
    playsum = {}
    for idx, genre in enumerate(genres):
        if genre not in playsum:
            playsum[genre] = plays[idx]
        else:
            playsum[genre] += plays[idx]
    playsum = dict(sorted(playsum.items(), key=lambda x: -x[1]))
    genreplay = []
    for idx, (genre, play) in enumerate(zip(genres,plays)):
        genreplay.append([idx, genre, play])
    genreplay.sort(key=lambda x: -x[2])
    for key in playsum.keys():
        cnt = 0
        for play in genreplay:
            if cnt == 2:
                break
            if key in play:
                answer.append(play[0])
                cnt += 1
    return answer