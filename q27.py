from datetime import datetime

class Experiment:
    def run(self):
        self.start = datetime.now()
        print("Start:", self.start)

        self.end = datetime.now()
        print("End:", self.end)

Experiment().run()
