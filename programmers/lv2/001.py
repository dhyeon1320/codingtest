def solution(s):
    nums = s.split(' ')
    sort_nums = sorted(nums, key=int)
    answer = sort_nums[0] + ' ' + sort_nums[-1]
    return answer

print(solution("-1 -1"))