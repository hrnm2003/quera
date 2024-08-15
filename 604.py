def Josephus(n, k):
    if (n == 1):
        return 1
    else:
        return (Josephus(n - 1, k) + k-1) % n + 1

n = int(input(""))
k = 2
print(Josephus(n, k))