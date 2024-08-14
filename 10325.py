
r, c = map(int, input().split())

a = 11 - r
if c < 11 :
    print("Right {} {}".format(a, c))
else:
    print("Left {} {}".format(a, 21 - c))