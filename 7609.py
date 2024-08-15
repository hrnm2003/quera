s = input()
sum = 1
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        sum +=1
    else:
        if((sum % 2) == 1):
            print("bad")
            break
        sum = 1

else:
    if len(s)%2 == 1:
        print("bad")
    else:
        print("khoob")