t = int(input())
lst = []
for j in range(t):
    string = input()
    count = 0
    for i in string:
        x = string.split("1")

    while("" in x):
        x.remove("")
        
    lst.append(len(x))
for i in lst:
    print(i)