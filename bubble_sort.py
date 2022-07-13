num = [4, 9, 39, 57, 473, 30, 23, -34, -9, 35, 21]
n = len(num)      

for i in range(0, n-1):     
    for j in range(0, n-1-i):   
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

print(*num)
