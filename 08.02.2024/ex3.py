import random


def random_numbers_generator(count, start, end):
    for _ in range(count):
        yield random.randint(start, end)


generator = random_numbers_generator(5, 1, 10)
for num in generator:
    print(num)
