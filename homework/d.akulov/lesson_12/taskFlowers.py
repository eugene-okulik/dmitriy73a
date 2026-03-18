class Flowers:

    def __init__(self, title, color, shelf_life, price):
        self.title = title
        self.color = color
        self.shelf_life = shelf_life
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __repr__(self):
        return f"{self.title}"


class RoseFlowers(Flowers):

    def __init__(self, title, color, shelf_life, price, sort):
        super().__init__(title, color, shelf_life, price)
        self.sort = sort


class PeonyFlowers(Flowers):

    def __init__(self, title, color, shelf_life, price, flower_structure):
        super().__init__(title, color, shelf_life, price)
        self.flower_structure = flower_structure


class LilyFlowers(Flowers):

    def __init__(self, title, color, shelf_life, price, flower_structure, aroma):
        super().__init__(title, color, shelf_life, price)
        self.flower_structure = flower_structure
        self.aroma = aroma


class BouquetFlowers:

    def __init__(self, lst_flowers):
        self.lst_flowers = lst_flowers

    def price_bouquet(self):
        """цена букета"""
        return sum([e.price for e in self.lst_flowers])

    def avg_time_withering_bouquet(self):
        """время увядания по среднему времени жизни всех цветов в букете(в днях)"""
        return round(sum([e.shelf_life for e in self.lst_flowers]) / len(self.lst_flowers))

    def sort_color(self):
        """сортировка цветов в букете по цвету"""
        return sorted(self.lst_flowers, key=lambda x: x.color)

    def sort_price(self):
        """сортировка цветов в букете по цене"""
        return sorted(self.lst_flowers, key=lambda x: x.price)

    def serch_time_life(self, day_time):
        """поиск цветков по дням их жизни(в днях)"""
        return [e for e in self.lst_flowers if e.shelf_life == day_time] \
            if day_time <= max([e.shelf_life for e in self.lst_flowers]) else "так долго живущих у нас нет))"


rose1 = RoseFlowers("роза1", "Желтый", 3, 111, "большая")
rose2 = RoseFlowers("роза2", "Красный", 5, 122, "средняя")
rose3 = RoseFlowers("роза3", "Розовый", 5, 133, "средняя")

peony1 = PeonyFlowers("пион1", "Синий", 1, 222, "Махровая")
peony2 = PeonyFlowers("пион2", "Красный", 5, 233, "Анемоновидная")
peony3 = PeonyFlowers("пион3", "Белый", 4, 244, "Японская")

lily1 = LilyFlowers("лилия1", "Белый", 3, 333, "трубчатая", "сильный")
lily2 = LilyFlowers("лилия2", "Розовый", 2, 344, "чашевидная", "средний")
lily3 = LilyFlowers("лилия3", "Желтый", 5, 355, "звездчатые", "слабый")

bouquet = BouquetFlowers([rose1, peony1, lily1, rose2, peony2, lily2, rose3, peony3, lily3])

print(bouquet.price_bouquet())
print(bouquet.avg_time_withering_bouquet())
print(bouquet.sort_color())
print(bouquet.sort_price())
print(bouquet.serch_time_life(5))
