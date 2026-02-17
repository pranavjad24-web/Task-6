class Processor:
    def process(self):
        pass

class ImageProcessor(Processor):
    def process(self):
        print("Processing image")

class TextProcessor(Processor):
    def process(self):
        print("Processing text")

for p in [ImageProcessor(), TextProcessor()]:
    p.process()
