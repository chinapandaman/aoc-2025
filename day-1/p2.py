current = 50
result = 0

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

with open("./test.txt", "r") as f:
    for line in f:
        code = line.rstrip("\n")

        times = int(code[1:])

        if code[0] == "L":
            op = minus
        else:
            op = add

        for _ in range(times):
            current = op(current, 1)
            if current in (0, 100):
                result += 1
            if current < 0:
                current += 100
            if current > 100:
                current -= 100

print(result)
