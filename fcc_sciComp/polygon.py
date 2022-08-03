# https://replit.com/@apnatvar/boilerplate-polygon-area-calculator#shape_calculator.py

class Rectangle:

    width = 0
    height = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        picture = ""
        for h in range(0,self.height):
            for w in range(0,self.width):
                picture += "*"
            picture += "\n"
        return picture

    def get_amount_inside(self, shape):
      return (self.width//shape.width * self.height//shape.height)


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        super(Square, self).set_width(side)
        super(Square, self).set_height(side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
