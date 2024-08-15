number = int(input())
result = 1
i = 1
while result <= number:
    result = 2 ** i
    i += 1

print(result)