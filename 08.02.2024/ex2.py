import random

class RandomNumber:
    def __init__(self, count, start, end):
        self.count = count
        self.start = start
        self.end = end
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count < self.count:
            self.current_count += 1
            return random.randint(self.start, self.end)
        else:
            raise StopIteration

iterator = RandomNumber(5, 1, 10)
for num in iterator:
    print(num)