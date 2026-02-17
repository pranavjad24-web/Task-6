class Shipment:
    def delivery_time(self):
        pass

class Air(Shipment):
    def delivery_time(self):
        print("2 days")

class Ground(Shipment):
    def delivery_time(self):
        print("5 days")

for s in [Air(), Ground()]:
    s.delivery_time()
