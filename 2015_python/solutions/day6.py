FILE_PATH = "../inputs/actual/day6.in"

with open(FILE_PATH) as file:
    data = file.readlines()

data = list(map(lambda _line: _line.strip(), data))


def parse_instruction(instruction: str):
    elements = instruction.split(" ")
    x1, y1 = elements[-3].split(',')
    x2, y2 = elements[-1].split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    action = elements[-4]
    return action, x1, y1, x2, y2


# Part 1
# "Light" = (x, y): on/off
lights = {}
for instruction in data:
    action, x1, y1, x2, y2 = parse_instruction(instruction)
    if action == "on":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = True

    elif action == "off":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = False

    else:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                light_status = lights.get((x, y), False)
                lights[(x, y)] = not light_status

count = 0
for status in lights.values():
    if status:
        count += 1
print(count)

# Part 2
lights = {}
for instruction in data:
    action, x1, y1, x2, y2 = parse_instruction(instruction)
    if action == "on":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = lights.get((x, y), 0) + 1

    elif action == "off":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = max(lights.get((x, y), 1) - 1, 0)

    else:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lights[(x, y)] = lights.get((x, y), 0) + 2

total_brightness = 0
for brightness in lights.values():
    total_brightness += brightness
print(total_brightness)
