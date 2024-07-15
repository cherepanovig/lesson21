# Атрибуты и методы объекта.

class House:
    # Вунтри класса House определим метод __init__, в который передадим название и кол-во этажей
    def __init__(self, name, number_of_floors):
        self.name = name # Инициализация атрибута name
        self.number_of_floors = number_of_floors # Инициализация атрибута number_of_floors

# Создаем метод go_to с параметром new_floor
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print(f'Такого этажа не существует')


# Создаем объект класса House с произвольным названием и количеством этажей
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# Вызываем метод go_to у этого объекта с произвольным числом этажей
h1.go_to(5)
h2.go_to(10)
# print(h1.name, h1.number_of_floors)
# print(h2.name, h2.number_of_floors)



