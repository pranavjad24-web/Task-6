class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def update_salary(self, amount):
        self.__salary = amount

    def get_salary(self):
        return self.__salary


e = Employee(30000)
e.update_salary(35000)
print(e.get_salary())
