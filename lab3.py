class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
    @property
    def name(self)->str:
        return self._name

    @property
    def author(self)->str:
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self._pages = pages
    @property
    def pages(self)->int:
        return self._pages
    @pages.setter
    def pages(self, value:int):
        if not isinstance(value, int) or value<=0:
            raise ValueError
        self_pages = value

    def __str__(self):
        return f"{super().__str__()}, страницы: {self.pages}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(self, name, author)
        self._duration = None
        self.duration = duration
    @property
    def duration(self)->float:
        return self._duration
    @duration.setter
    def duration(self, value:float):
        if not isinstance(value, float) or value<=0:
            raise ValueError
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}, продолжительность: {self.duration} часов"
