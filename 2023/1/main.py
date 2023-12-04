with open("2023/1/input.txt", "r") as f:
    lines = f.readlines()

def isdigit(char, line: str, side):
    """Will return char of digit should it be a digit, else will return -1"""

    if char.isdigit():
        return char

    # print(line)

    digits_spelled_out = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    if side == "left":
        possible_digits = {digit: val for digit, val in digits_spelled_out.items() if digit.startswith(char)}
    elif side == "right":
        possible_digits = {digit: val for digit, val in digits_spelled_out.items() if digit.endswith(char)}

    for possible_digit, value in possible_digits.items():
        print(possible_digit, value)
        if side == "left":
            if line.startswith(possible_digit):
                return str(value)
        elif side == "right":
            if line.endswith(possible_digit):
                print(value)
                return str(value)

    return -1

calibration_values = []

for line in lines:
    print(line)
    for i, char in enumerate(line):
        # print(char)
        check = isdigit(char, line[i:], "left")
        if check != -1:
            left_digit: str = check
            print(left_digit)
            break
    for i, char in enumerate(reversed(line)):
        check = isdigit(char, line[:len(line)-i], "right")
        if check != -1:
            right_digit: str = check
            print(right_digit)
            break

    # print(left_digit, right_digit)
    concat = left_digit + right_digit
    # print(concat)
    calibration_values.append(int(concat))

print(sum(calibration_values))
