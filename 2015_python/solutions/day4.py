from hashlib import md5

FILE_PATH = "../inputs/actual/day4.in"

with open(FILE_PATH) as file:
    secret_key = file.readline().strip()

# Part 1
number = 0
while True:
    hash_input = f"{secret_key}{number}".encode('-utf-8')
    hash_output = md5(hash_input).hexdigest()
    if hash_output.startswith("00000"):
        print(number)
        break
    number += 1

# Part 2
number = 0
while True:
    hash_input = f"{secret_key}{number}".encode('-utf-8')
    hash_output = md5(hash_input).hexdigest()
    if hash_output.startswith("000000"):
        print(number)
        break
    number += 1
