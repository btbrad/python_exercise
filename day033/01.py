class CountFromBy:

    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)

if __name__ == '__main__':
    c = CountFromBy(100, 10)
    print(c.val)
    print(c.incr)
    c.increase()
    print(c.val)
    print(c)