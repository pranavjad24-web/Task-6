class Config:
    def __init__(self):
        self.__key = "SECRET"

    def get_key(self):
        return self.__key

c = Config()
print(c.get_key())
