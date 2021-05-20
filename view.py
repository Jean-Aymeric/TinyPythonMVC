import tkinter.messagebox

class View:
    def __init__(self):
        self.__header = "A tiny MVC Python program"
        self.__footer = "made by JAD"

    def showMessage(self, message):
        tkinter.messagebox.showinfo(self.__header, message)
        print(self.__header)
        print(message)
        print(self.__footer)

    def askRank(self):
        print(self.__header)
        print("Enter a rank : ", end='')
        return int(input())
