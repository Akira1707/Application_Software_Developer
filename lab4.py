from typing import Union
if __name__ == "__main__":

    class Device:
        def __init__(self, brand: str, model: str, price: float):
            """Конструктор базового класса.

            Args:
                brand (str): Марка устройства.
                model (str): Модель устройства.
                price (float): Цена устройства.
            """
            self._brand = brand  # Используем инкапсуляцию для скрытия прямого доступа к атрибутам
            self._model = model
            self._price = price

        @property
        def brand(self) -> str:
            """Марка устройства."""
            return self._brand

        @property
        def model(self) -> str:
            """Модель устройства."""
            return self._model

        @property
        def price(self) -> float:
            """Цена устройства."""
            return self._price

        def turn_on(self) -> str:
            """Включение устройства.

            Returns:
                str: Сообщение о включении устройства.
            """
            return f"{self.brand} {self.model} включено."

        def __str__(self) -> str:
            """Возвращает строковое представление устройства."""
            return f"{self.brand} {self.model}, Цена: {self.price}"

        def __repr__(self) -> str:
            """Возвращает формальное строковое представление устройства."""
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, price={self.price!r})"


    class Smartphone(Device):
        def __init__(self, brand: str, model: str, price: float, os: str, storage: Union[int, None] = None):
            """Конструктор дочернего класса Smartphone.

            Args:
                brand (str): Марка смартфона.
                model (str): Модель смартфона.
                price (float): Цена смартфона.
                os (str): Операционная система смартфона.
                storage (Union[int, None]): Объем встроенной памяти в ГБ. Может быть None, если нет встроенной памяти.
            """
            super().__init__(brand, model, price)
            self._os = os
            self._storage = storage

        @property
        def os(self) -> str:
            """Операционная система смартфона."""
            return self._os

        @property
        def storage(self) -> Union[int, None]:
            """Объем встроенной памяти в ГБ."""
            return self._storage

        def make_call(self, number: str) -> str:
            """Совершение звонка.

            Args:
                number (str): Номер телефона.

            Returns:
                str: Сообщение о звонке.
            """
            return f"Совершен звонок с {self.brand} {self.model} на номер {number}."

        def turn_on(self) -> str:
            """Перегруженный метод включения для смартфона.

            Returns:
                str: Сообщение о включении смартфона.
            """
            return f"{self.brand} {self.model} с операционной системой {self.os} включен."