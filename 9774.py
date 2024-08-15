number = input()
for i in [int(d) for d in str(number)]:
    print("{}: {}".format(i, str(i)*i), end="\n")