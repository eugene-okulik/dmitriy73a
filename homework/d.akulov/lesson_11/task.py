class Book:
    page_material = "paper"
    presence_of_text = True

    def __init__(self, title_book, author, count_pages, isbn, reserve):
        self.title_book = title_book
        self.author = author
        self.count_pages = count_pages
        self.isbn = isbn
        self.reserve = reserve

    def for_print(self):
        if self.reserve:
            print(
                f"Название: {self.title_book}, Автор: {self.author}, страниц: {self.count_pages},"
                f" материал: {self.page_material}, зарезервирована")
        else:
            print(
                f"Название: {self.title_book}, Автор: {self.author}, страниц: {self.count_pages}, "
                f"материал: {self.page_material}")


class SchoolBook(Book):
    def __init__(self, title_book, author, count_pages, isbn, reserve, academic_subject, class_level,
                 availability_of_tasks):
        super().__init__(title_book, author, count_pages, isbn, reserve)
        self.academic_subject = academic_subject
        self.class_level = class_level
        self.availability_of_tasks = availability_of_tasks

    def for_print(self):
        if self.reserve:
            print(
                f"Название: {self.title_book}, Автор: {self.author}, страниц: {self.count_pages}, "
                f"предмет: {self.academic_subject}, класс: {self.class_level}, зарезервирована")
        else:
            print(
                f"Название: {self.title_book}, Автор: {self.author}, страниц: {self.count_pages}, "
                f"предмет: {self.academic_subject}, класс: {self.class_level}")


mathematics = SchoolBook("Математика", ["Виленкин Н.Я.", "Жохов В.И."],
                         500, 66666, True, "Математика", 5,
                         True)

history = SchoolBook("История Древнего мира и Средних веков",
                     ["О.В.Кравченко", "О.Г.Журавлевич"],
                     123, 77777, False, "История", 6,
                     True)

physics = SchoolBook("Физика",
                     ["ТотСамый Д.В"],
                     99999, 88888, True, "Физика", 99,
                     True)

war_and_peace = Book("Война и мир", "Лев Толстой", 1700, 11111, True)
how_google_tests_software = Book("How Google Tests Software",
                                 ["James Whittaker", "Jason Arbon", "Jeff Carollo"], 446,
                                 22222, True)
deniskins_stories = Book("Денискины рассказы", "Виктор Драгунский",
                         260, 33333, False)
knight_of_the_seven_kingdoms = Book("Рыцарь Семи Королевств", "George R.R.Martin",
                                    384, 44444, False)
the_road = Book("The Road", "Cormac McCarthy", 320, 55555, True)

lst_book = [war_and_peace, how_google_tests_software, deniskins_stories, knight_of_the_seven_kingdoms, the_road]

print("------------принтуем обычные книги------------")
for i in lst_book:
    Book.for_print(i)
print("---------------принтуем учебники--------------")
mathematics.for_print()
history.for_print()
physics.for_print()
