def F(n):
    curr, next = 0, 1
    for i in range(n):
        curr, next = next, curr+next
    return curr

def solution(n):
    return F(n)%1234567

print(solution(5))