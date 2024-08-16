n, m = map(int, input().split())
days1 = []
days2 = []
for i in range(n):
    l, r = map(int, input().split())
    for j in range(l, r+1):
        days1.append(j)

for i in range(m):
    l, r = map(int, input().split())
    for j in range(l, r+1):
        days2.append(j)

print(len(set(days1)&set(days2)))