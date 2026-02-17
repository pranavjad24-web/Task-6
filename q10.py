from datetime import datetime

class Experiment:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.now()

    def end(self):
        self.end_time = datetime.now()

    def show(self):
        print("Start:", self.start_time)
        print("End:", self.end_time)


exp = Experiment()
exp.start()
exp.end()
exp.show()
