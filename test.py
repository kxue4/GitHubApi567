#!/usr/bin/python


class EnglishMeasure:

    def __init__(self, foot, inch):
        self.foot = foot
        self.inch = inch

    def __add__(self, other):
        self.foot = self.foot + other.foot
        self.inch = self.inch + other.inch
        return EnglishMeasure(self.foot, self.inch)

    def __str__(self):

        if self.inch >= 12:
            self.foot += self.inch // 12
            self.inch = self.inch % 12

        return str(self.foot) + ' feet ' + str(self.inch) + ' inches'


def main():
    print(EnglishMeasure(1, 3))
    print(EnglishMeasure(1, 13))
    print(EnglishMeasure(0, 37))
    m1 = EnglishMeasure(1, 2)
    m2 = EnglishMeasure(2, 11)
    print(m1 + m2)


if __name__ == '__main__':
    main()