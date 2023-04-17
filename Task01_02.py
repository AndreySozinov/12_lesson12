# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json


class K_factorials:

    def __init__(self, k: int):
        self.k = k
        self.storage = []
        self.name_json_file = 'records.json'

    def __call__(self, number: int):
        self.factorial = 1
        for i in range(1, number + 1):
            self.factorial *= i
        if len(self.storage) >= self.k:
            self.storage.pop(0)
        self.storage.append({number: self.factorial})
        return self.factorial

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.name_json_file, 'w', encoding='utf-8') as fw:
            json.dump(self.storage, fw, indent=2)

    def show_record(self):
        print(f'Последние {self.k} значений и их факториалы: {self.storage}')


if __name__ == '__main__':
    with K_factorials(3) as f1:
        print(f1(5))
        print(f1(6))
        print(f1(7))
        print(f1(8))
        print(f1(9))
        print(f1(10))
        f1.show_record()
