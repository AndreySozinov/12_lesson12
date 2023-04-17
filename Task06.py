# Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
class Positive:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value >= 0:
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Must be positive.')

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')


class Rectangle:
    """Rectangle class containing length & width, computing perimeter & area."""
    length = Positive()
    width = Positive()

    def __init__(self, length: int | float, width=0):
        self.length = length
        if not width:
            width = length
        self._width = width

    def perimeter(self) -> int | float:
        """Return perimeter of the rectangle"""
        return 2 * self.length + 2 * self.width

    def area(self) -> int | float:
        """Return area of the rectangle"""
        return self.length * self.width

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
        return f'length = {self.length}; width = {self.width}'

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width}'


if __name__ == '__main__':
    pass
