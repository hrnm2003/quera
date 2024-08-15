n = int(input())
hex = {"0":"F", "1":"E", "2":"D", "3": "C",  "4": "B", "5": "A", "6": "9", "7": "8", "8": "7", "9": "6",
       "A": "5", "B": "4", "C": "3", "D": "2", "E": "1", "F": "0"}

color = []
for i in range(n):
    string = input().split("#")[1]
    reversed = "#"
    for i in string:
        reversed += f"{hex[i]}"
    color.append(reversed)

print(*color, sep="\n")