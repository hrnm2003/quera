word = str(input())
vowel = ['a', 'e', 'i', 'o', 'u']

count = 0
for i in word:
    if i in vowel:
        count += 1

print(2**count)