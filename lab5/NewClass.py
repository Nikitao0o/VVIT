class Book():
    def __init__(self, title=None, author=None, year=None):
        self.author = author
        self.title = title
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год публикации: {self.year}"


class Circle():
    def __init__(self, radius=0):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius
