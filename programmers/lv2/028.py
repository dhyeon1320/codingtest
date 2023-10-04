def solution(priorities, location):
    answer = 0
    nums = list(range(len(priorities)))
    real = priorities
    print(nums)
    order = []
    while True:
        if priorities == []:
            break
        for process, num in zip(priorities, nums):
            if process < max(priorities):
                priorities, nums = priorities[1:], nums[1:]
                priorities.append(process)
                nums.append(num)
                print(priorities)
                print(nums)
            elif process == max(priorities):
                order.append([process, num])
                priorities = priorities[1:]
                nums = nums[1:]
                print('order', order)
    answer = order.index([real[location], location])+1
    return answer

print(solution([2,1,3,2],2))