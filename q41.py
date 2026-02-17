class Gateway:
    def pay(self):
        pass

class PayPal(Gateway):
    def pay(self):
        print("Paid via PayPal")

class Stripe(Gateway):
    def pay(self):
        print("Paid via Stripe")

for g in [PayPal(), Stripe()]:
    g.pay()
