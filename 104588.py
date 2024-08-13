a1, a2, a3, a4, a5 = map(int, input().split())
lst = [a1, a2, a3, a4, a5]

pos = 0
for i in lst:
    if i >= 80:
        pos += 1
if pos >= 3:
    print("Mamma mia!")
elif 1 <= pos <= 2:
    print("Mamma mia!!")
else:
    print("Mamma mia!!!")