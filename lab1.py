import doctest

class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        return self.occupied_volume == 0

    def add_water_to_glass(self, water: float) -> None:
       if self.occupied_volume + water >self.capacity_volume:
           raise ValueError("Добавляемая жидкость должна менше")
       self.occupied_volume += water
    def remove_water_from_glass(self, estimate_water: float) -> None:
        if self.occupied_volume< estimate_water:
            raise ValueError("Вылитая жидкости должна меньше")
        self.occupied_volume -= estimate_water

class Library:
    def __init__(self, number_books: int, names: list):
        if not isinstance(number_books, int):
            raise TypeError("Количество книги должно быть типа int")
        self.number_books = number_books
        self.names = names

    def Borrow_book(self, name : str):
        if name not in self.names:
            raise ValueError("Нет этой книг")
        self.number_books -=1
        self.names.remove(name)

    def Return_book(self, name):
        self.number_books +=1
        self.name.append(name)

class Parking:
    def __init__(self, number_cars: int, max_cars: int):
        if not isinstance(number_cars,int):
            raise TypeError("Количество машин должно быть типа int")
        if not isinstance(max_cars,int):
            raise TypeError("Максимальноек количество машин должно быть типа int")
        if max_cars < number_cars:
            raise ValueError("Максимальное количество машин должно быть больше или равно количеству машин")
        self.number_cars = number_cars
        self.max_cars = max_cars

    def Add_car(self, number_add: int):
        if self.number_cars + number_add> self.max_cars:
            raise ValueError("Количество въезжающих машин меньше")
        self.number_cars += number_add

    def Remove_car(self, number_remove: int):
        if self. number_cars< number_remove:
            raise ValueError("Количесво выезжающих машин больше")
        self.number_cars -= number_remove

if __name__ == "__main__":
    doctest.testmod()