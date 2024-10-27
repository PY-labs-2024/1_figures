class Shape:
    """Геометрические фигуры"""
    name = 'геометрическая фигура'

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"{self.name} по координатам ({self.__x}, {self.__y})"


class Rectangle(Shape):
    """Прямоугольники"""
    name = 'прямоугольник'

    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return (f"{Shape.__repr__(self)}, со сторонами {self.width} и {self.height},"
                f" с площадью {self.area()} и периметром {self.perimeter()}")


class Square(Rectangle):
    """Квадраты"""
    name = 'квадрат'

    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)

    @property
    def width(self):
        print(f"Getter квадрата на width")
        return self.__width

    @width.setter
    def width(self,w):
        self.__width = w
        self.__height = w
        print(f"Setter квадрата на width")

    @property
    def height(self):
        print(f"Getter квадрата на height")
        return self.__height

    @height.setter
    def height(self,h):
        self.__width = h
        self.__height = h
        print(f"Setter квадрата на height")


if __name__ == '__main__':
    a = Square(2)
    print(a)
    a.width = 4
    if (a.width == a.height):
        print(f"True")
