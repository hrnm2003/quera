string1 = str(input())
string2 = str(input())

if string1[0] == string2[-1:]:
    print("YES")
else:
    print("NO")