class Workout:
    def calories(self):
        pass

class Running(Workout):
    def calories(self):
        return 300

class Cycling(Workout):
    def calories(self):
        return 250

for w in [Running(), Cycling()]:
    print(w.calories())
