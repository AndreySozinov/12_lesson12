# Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.
class FactorialGenerator:
    def __init__(self, *args):
        match len(args):
            case 3:
                self.start = args[0]
                self.stop = args[1]
                self.step = args[2]
            case 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case _:
                self.start = 1
                self.stop = 1
                self.step = 1
        self.factorial = self.start

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            self.start += self.step
            self.factorial *= self.start
            return self.factorial
        raise StopIteration


if __name__ == '__main__':
    fact = FactorialGenerator(5)
    for number in fact:
        print(number)
