class Strategy:
    def respond(self):
        pass

class Friendly(Strategy):
    def respond(self):
        print("Hello friend!")

class Formal(Strategy):
    def respond(self):
        print("Good day.")

for s in [Friendly(), Formal()]:
    s.respond()
