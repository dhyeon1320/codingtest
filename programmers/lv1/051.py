def solution(nums):
    n = len(nums)
    count = len(set(nums))
    answer = min(int(n/2), count)
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))