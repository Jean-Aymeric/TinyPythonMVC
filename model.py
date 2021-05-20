class Model:
    def __init__(self):
        self.__messages = ["Hello World!", "Bonjour le monde !", "Hola mundo !", "Hi Welt !"]

    def getMessage(self, rank):
        if len(self.__messages)-1 < rank or rank < 0:
            return self.__messages[0]
        return self.__messages[rank]
