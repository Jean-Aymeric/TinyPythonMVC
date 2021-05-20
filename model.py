class Model:
    def __init__(self):
        self.__message = "Hello World!"

    @property
    def Message(self):
        return self.__message
