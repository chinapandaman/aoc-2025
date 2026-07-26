def get_max_12(s):
    result = ""
    pos = 0

    for i in range(12):
        remaining_needed = 12 - i
        latest_pos = len(s) - remaining_needed

        best_digit = -1
        best_pos = 0

        for j in range(pos, min(latest_pos + 1, len(s))):
            d = int(s[j])
            if d > best_digit:
                best_pos = j
                best_digit = d

        result += str(best_digit)
        pos = best_pos + 1

    return result


result = 0
with open("./test.txt", "r") as f:
    for line in f:
        code = line.rstrip("\n").rstrip()
        selected = get_max_12(code)
        result += int(selected)

print(result)
