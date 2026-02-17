class Employee:
    def __init__(self, name):
        self.name = name

    def salary(self):
        pass

class FullTime(Employee):
    def salary(self):
        return 50000

class Contract(Employee):
    def salary(self):
        return 30000

for e in [FullTime("A"), Contract("B")]:
    print(e.name, e.salary())
