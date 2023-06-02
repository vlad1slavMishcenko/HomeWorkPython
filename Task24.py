n = int(input())
lis = list()
for i in range(n):
    lis.append(int(input()))
lis2 = list()
for i in range(len(lis)-1 ):
    lis2.append(lis[i - 1] + lis[i] + lis[i+1])
lis2.append(lis[ -2] + lis[ - 1] + lis[0])
print(max(lis2), lis2)
