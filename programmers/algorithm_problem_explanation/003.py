def solution(v):
    answer = []
    xs = {}
    ys = {}
    for x, y in v:
        if x not in xs:
            xs[x] = 1
        else:
            xs[x] += 1
        if y not in ys:
            ys[y] = 1
        else:
            ys[y] += 1
    xs = {num: x for x, num in xs.items()}
    ys = {num: y for y, num in ys.items()}

    answer.append(xs.get(1))
    answer.append(ys.get(1))

    print('Hello Python')

    return answer