FILE_PATH = "../inputs/actual/day3.in"

with open(FILE_PATH) as file:
    data = file.read()

# Part 1
visited = set()
x, y = 0, 0
visited.add((x, y))

for char in data:
    if char == "<":
        x -= 1
    elif char == ">":
        x += 1
    elif char == "v":
        y -= 1
    elif char == "^":
        y += 1

    visited.add((x, y))

print(f"Part 1 Answer: {len(visited)}")

# Part 2
visited = set()
x_me, x_robo, y_me, y_robo = 0, 0, 0, 0
visited.add((x_me, y_me))

for index, char in enumerate(data):
    if char == "<":
        if index % 2 == 0:
            x_me -= 1
        else:
            x_robo -= 1

    elif char == ">":
        if index % 2 == 0:
            x_me += 1
        else:
            x_robo += 1

    elif char == "v":
        if index % 2 == 0:
            y_me -= 1
        else:
            y_robo -= 1

    elif char == "^":
        if index % 2 == 0:
            y_me += 1
        else:
            y_robo += 1

    visited.add((x_me, y_me))
    visited.add((x_robo, y_robo))

print(f"Part 2 Answer: {len(visited)}")
