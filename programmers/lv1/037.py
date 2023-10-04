def solution(sizes):
    s = []
    for x, y in sizes:
        if x >= y :
            s.append([x,y])
        else:
            s.append([y,x])
    m = max([x for x, _ in s])
    n = max([y for _, y in s])
    return m*n