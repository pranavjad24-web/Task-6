from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


def checkout(payment: Payment):
    payment.pay(500)


checkout(CardPayment())
checkout(UPIPayment())
