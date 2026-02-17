class Report:
    def generate(self):
        pass

class SalesReport(Report):
    def generate(self):
        print("Sales Report")

class FinanceReport(Report):
    def generate(self):
        print("Finance Report")

reports = [SalesReport(), FinanceReport()]

for r in reports:
    r.generate()
