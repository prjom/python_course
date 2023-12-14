print('Задание№1')
class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def square(self):
        print(self.height * self.width)

    def perim(self):
        print(2*(self.height + self.width))

rect1 = Rectangle(10, 15)
print('Площадь:')
rect1.square()
print('Периметр:')
rect1.perim()