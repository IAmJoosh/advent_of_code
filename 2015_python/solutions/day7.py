from functools import lru_cache


FILE_PATH = "../inputs/actual/day7.in"

with open(FILE_PATH) as file:
    data = file.readlines()

data = list(map(lambda _line: _line.strip(), data))


def parse_line(line: str) -> (str, dict):
    circuit, wire = line.split(' -> ')
    circuit_pieces = circuit.split(' ')
    if (number_of_pieces := len(circuit_pieces)) == 1:
        instruction = {'operation': 'EQUAL', 'left': circuit_pieces[0]}

    elif number_of_pieces == 2:
        instruction = {'operation': 'NOT', 'left': circuit_pieces[1]}

    else:
        instruction = {
            'operation': circuit_pieces[1],
            'left': circuit_pieces[0],
            'right': circuit_pieces[2],
        }

    return wire, instruction


WIRES = {}

for line in data:
    wire, instruction = parse_line(line)
    WIRES[wire] = instruction


@lru_cache
def solve(wire: str):
    if isinstance(wire, int):
        return wire

    instruction = WIRES[wire]

    operation = instruction['operation']
    left = instruction['left']
    right = instruction.get('right', '')

    if left.isdigit():
        left = int(left)

    if right.isdigit():
        right = int(right)

    if operation == 'EQUAL':
        return solve(left)

    elif operation == 'NOT':
        return ~solve(left) & 0xffff

    elif operation == 'AND':
        return solve(left) & solve(right)

    elif operation == 'OR':
        return solve(left) | solve(right)

    elif operation == 'RSHIFT':
        return solve(left) >> solve(right)

    elif operation == 'LSHIFT':
        return solve(left) << solve(right)


# Part 1
part1 = solve('a')
print(part1)

# Part 2
solve.cache_clear()
WIRES['b'] = {'left': str(part1), 'operation': 'EQUAL'}
print(solve('a'))
