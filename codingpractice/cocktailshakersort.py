li = [6,15,1,1,1,2,2,8,5,11,9,7,15]

for i in range(len(li)-1, 0, -1):
    if i % 2 == 1 :
        for j in range(1, i):
            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]
    else:
        for j in range(i, 1, -1):
            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]

print(li)