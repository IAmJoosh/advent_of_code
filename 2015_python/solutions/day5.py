FILE_PATH = "../inputs/actual/day5.in"

with open(FILE_PATH) as file:
    data = file.readlines()

data = list(map(lambda _line: _line.strip(), data))


def contains_n_vowels(n: int, string: str):
    count = 0
    for char in string:
        if char in ('a', 'i', 'e', 'o', 'u'):
            count += 1
    return count >= n


def contains_letter_repeating_n_times(n: int, string: str):
    right = 1
    string_length = len(string)

    repeated_char_length = 1
    char = string[0]

    while right < string_length:
        next_char = string[right]
        if next_char == char:
            repeated_char_length += 1

            if repeated_char_length >= n:
                return True

        else:
            char = next_char
            repeated_char_length = 1

        right += 1

    return False


def contains_faulty_string(string: str):
    faulty_strings = ('ab', 'cd', 'pq', 'xy')
    for faulty_string in faulty_strings:
        if faulty_string in string:
            return True
    return False


def chars_are_overlapping(pair, left_index, seen):
    end_index_of_seen_pair = seen[pair]
    return end_index_of_seen_pair == left_index


def contains_pair_of_non_overlapping_letters(string: str):
    seen = {}
    left = 0
    right = left + 1
    string_length = len(string)
    while right < string_length:
        pair = f"{string[left]}{string[right]}"
        if pair in seen:
            if not chars_are_overlapping(
                pair,
                left,
                seen,
                    ):
                return True
        else:
            seen[pair] = (right)

        right += 1
        left += 1

    return False


def contains_repeating_letter_with_seperand(string: str):
    left = 0
    right = left + 2
    string_length = len(string)

    while right < string_length:
        if string[left] == string[right]:
            return True
        left += 1
        right += 1

    return False


def is_nice(string: str):
    if (
        contains_n_vowels(3, string) and
        contains_letter_repeating_n_times(2, string) and
        not contains_faulty_string(string)
            ):
        return True
    return False


def is_nice_two(string: str):
    if (
        contains_pair_of_non_overlapping_letters(string) and
        contains_repeating_letter_with_seperand(string)
            ):
        return True
    return False


# Part 1
number_of_nice_strings = 0
for string in data:
    if is_nice(string):
        number_of_nice_strings += 1
print(number_of_nice_strings)

# Part 2
number_of_nice_strings = 0
for string in data:
    if is_nice_two(string):
        number_of_nice_strings += 1
print(number_of_nice_strings)
