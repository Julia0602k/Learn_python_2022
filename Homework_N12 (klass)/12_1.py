# 1. Придумайте по одному своему примеру на каждую из парадигм:
# Абстракция
# Полиморфизм
# Инкапсуляция
# Наследование
# Продемонстрировать работу данных классов, отвечающих за примеры парадигм ООП.
# Абстракция
class Road:
    pass
# Полиморфизм
class Tree:
    pass
# Инкапсуляция
class Weather:
    pass

# Наследование
class Flower:
    def __init__(self, color):
        self.color = color
    def print_info(self):
        print(f'Это {self.color} цветок')
class Summer_Flower(Flower):
    def __init__(self, color, height):
        super().__init__(color)
        self.height = height
    def print_info(self):
        print(f'Цветок {self.color}, высотой {self.height}')
class Spring_Flower(Flower):
    def __init__(self, color, month):
        super().__init__(color)
        self.month = month
    def print_info(self):
        print(f'''Цветок {self.color}, цветет в месяце "{self.month}"''')
class New_flower(Spring_Flower):
    def __init__(self, color, month, price):
        super().__init__(color, month)
        self.price = price
    def print_info2(self):
        print(f'Цена этого цветка {self.price}')
flower1 = Flower('красный')
flower2 = Spring_Flower('белый', 'май')
flower3 = Summer_Flower('розовый', '50 см')

flower1.print_info()
flower2.print_info()
flower3.print_info()

flower2.color = 'синий'
flower2.month = 'март'
flower2.print_info()

flower4 = New_flower('желтый', 'апрель', '10 рублей')
flower4.print_info()
flower4.print_info2()



