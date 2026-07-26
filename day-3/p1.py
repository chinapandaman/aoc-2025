def get_max(s):
    result = ""
    for i, each in enumerate(s):
        if not result or int(each) > int(result[1]):
            result = (i, each)

    return result

result = 0
with open("./test.txt", "r") as f:
    for line in f:
        code = line.rstrip("\n")

        left = ""
        right = ""
        r = get_max(code)
        if r and r[0] == len(code) - 1:
            right = r
            left = get_max(code[:-1])
        else:
            left = r
            right = get_max(code[int(left[0]) + 1:])

        result += int(left[1] + right[1])

print(result)
