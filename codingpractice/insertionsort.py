li = [6,15,1,1,1,2,2,8,5,11,9,7,15]

for i in range(1, len(li)):
    for j in range(i, 0, -1):
        if li[j] < li[j-1]:
            li[j], li[j-1] = li[j-1], li[j]
        else:
            break

print(li)
