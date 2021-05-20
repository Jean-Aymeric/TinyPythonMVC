class View:
    def __init__(self):
        self.__header = "A tiny MVC Python program"
        self.__footer = "made by JAD"

    def showMessage(self, message):
        print(self.__header)
        print(message)
        print(self.__footer)
