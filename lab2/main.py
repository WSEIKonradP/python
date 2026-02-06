class PowerGenerator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.step = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.step >= self.n:
            raise StopIteration
        result = self.a ** self.step
        self.step = self.step + 1
        return result


if __name__ == "__main__":
    gen = PowerGenerator(2, 5)
    for value in gen:
        print(value)
    print("---")
    gen2 = PowerGenerator(3, 4)
    print(list(gen2))
