from NewClass import Book, Circle

book1 = Book("Harry Potter and the Philosopher's Stone","J. K. Rowling", "1997")
book2 = Book()
print(book1.get_info())
print(book2.get_info())

rad = Circle(40)
print(rad.get_radius())
rad.set_radius(eval(input()))
print(rad.get_radius())
