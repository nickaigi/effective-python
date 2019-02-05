class Rect(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        area = self.x * self.y
        return area


if __name__ == '__main__':
    rect = Rect(5, 4)
    print(rect())
