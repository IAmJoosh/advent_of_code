import logging

FILE_PATH = "../inputs/actual/day1.in"

with open(FILE_PATH) as file:
    data = file.read()

data = data.strip()

# Part 1
floor = 0
already_printed = False
for index, char in enumerate(data):
    if char == "(":
        floor += 1

    elif char == ")":
        floor -= 1

    else:
        logging.warning(f"Unexpected character found: {ord(char)}")

    if not already_printed and floor == -1:
        print(f"Part 2 Answer: {index=}")
        already_printed = True

print(f"Part 1 Answer: {floor=}")
