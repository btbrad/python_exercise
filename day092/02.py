class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            raise ValueError("分数必须在0到100之间")


if __name__ == "__main__":
    s = Student("Bob", 59)
    print(s.score)
    s.score = 60
    print(s.score)
    # s.score = 999 # ValueError: 分数必须在0到100之间
    print(s._score)
