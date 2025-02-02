class shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class rectangle(shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length

