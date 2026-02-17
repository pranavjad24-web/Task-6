class Book:
    def __init__(self, price):
        self.__price = price

    def update_price(self, p):
        self.__price = p

    def get_price(self):
        return self.__price

b = Book(500)
b.update_price(600)
print(b.get_price())
