FILE_PATH = "../inputs/actual/day2.in"

with open(FILE_PATH) as file:
    data = file.readlines()

data = map(lambda _line: _line.strip(), data)
print(type(data))

# Part 1
total_surface_area = 0
for line in data:
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)
    surface_area = 2 * (l * w + w * h + h * l)
    smallest_face = (l * w * h) // max([l, w, h])
    total_surface_area += surface_area + smallest_face

print(f"Part 1 Answer: {total_surface_area=}")

# Part 2
ribbon_length = 0
for line in data:
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)
    ribbon = 2 * (l + w + h - max([l, w, h]))
    volume = l * w * h
    ribbon_length += ribbon + volume

print(f"Part 2 Answer: {ribbon_length=}")
