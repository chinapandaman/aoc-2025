ranges = []

with open("./test.txt", "r") as f:
    for line in f:
        line = line.rstrip("\n")
        for _range in line.split(","):
            if _range:
                ranges.append([int(each) for each in _range.split("-")])

result = 0
for r in ranges:
    for i in range(r[0], r[1] + 1):
        s = str(i)
        if len(s) % 2:
            continue

        mid = int(len(s) / 2)

        if s[:mid] == s[mid:]:
            result += i

print(result)
