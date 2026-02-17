class Evaluation:
    def result(self):
        pass

class Exam(Evaluation):
    def result(self):
        print("Exam result")

class Assignment(Evaluation):
    def result(self):
        print("Assignment result")

for e in [Exam(), Assignment()]:
    e.result()
