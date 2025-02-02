
class shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class square(shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

n = int(input())
a = square(n)
print(a.area())
