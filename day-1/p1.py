current = 50
result = 0

with open("./test.txt", "r") as f:
    for line in f:
        code = line.rstrip("\n")

        times = int(code[1:])

        if code[0] == "L":
            current -= times
        elif code[0] == "R":
            current += times

        while current < 0:
            current += 100
        while current >= 100:
            current -= 100

        print(f"code: {code} check: {current}")
        if current == 0:
            result += 1

print(result)
