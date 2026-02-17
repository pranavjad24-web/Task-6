class Delivery:
    def deliver(self):
        pass

class BikeDelivery(Delivery):
    def deliver(self):
        print("Delivered by Bike")

class TruckDelivery(Delivery):
    def deliver(self):
        print("Delivered by Truck")

for d in [BikeDelivery(), TruckDelivery()]:
    d.deliver()
