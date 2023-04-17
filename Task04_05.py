# Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.
class Rectangle:
    """Rectangle class containing length & width, computing perimeter & area."""
    __slots__ = ('_length', '_width')

    def __init__(self, length: int | float, width=0):
        self._length = length
        if not width:
            width = length
        self._width = width

    def perimeter(self) -> int | float:
        """Return perimeter of the rectangle"""
        return 2 * self._length + 2 * self._width

    def area(self) -> int | float:
        """Return area of the rectangle"""
        return self._length * self._width

    def __add__(self, other):
        perimeter = self.perimeter() + other.perimeter()
        return Rectangle(perimeter / 4)

    def __sub__(self, other):
        perimeter = max(self.perimeter(), other.perimeter()) - min(self.perimeter(), other.perimeter())
        return Rectangle(perimeter / 4)

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'length = {self._length}; width = {self._width}'

    def __repr__(self):
        return f'Rectangle({self._length}, {self._width}'

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError(f'New length must be greater than zero.')

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError(f'New width must be greater than zero.')


if __name__ == '__main__':
    pass
