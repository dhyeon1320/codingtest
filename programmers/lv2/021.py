def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h = []
    for idx, cite in enumerate(citations):
        if idx+1 <= cite:
            h.append(min(idx+1, cite))
    answer = max(h) if len(h) >= 1 else 0
    return answer