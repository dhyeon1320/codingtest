li = [6,15,1,1,1,2,2,8,5,11,9,7,15]

for i in range(len(li)):
    minarg = min(li[i:])
    minargindex = li[i:].index(minarg) + i
    if li[minargindex] < li[i]:
        li[i], li[minargindex] = li[minargindex], li[i]

print(li)