import tkinter.messagebox
from icontroller import IController


class View:
    def __init__(self, controller: IController):
        self.__header = "A tiny MVC Python program"
        self.__footer = "made by JAD"
        self.__createWindow()
        self.__controller = controller

    def __createWindow(self):
        self.__window = tkinter.Tk()
        self.__window.title(self.__header)
        self.__rank = tkinter.IntVar(value=0)
        self.__rank.trace_add("write", self.__rankUpdated)
        self.__message = tkinter.StringVar(value='')
        tkinter.Label(self.__window, text='Rank : ').pack()
        tkinter.Entry(self.__window, textvariable=self.__rank).pack()
        tkinter.Label(self.__window, textvariable=self.__message).pack()

    def __rankUpdated(self, *args):
        try:
            self.__controller.performUpdateRank(self.__rank.get())
        except tkinter.TclError:
            self.__controller.performUpdateRank(-1)

    def __buttonOk(self):
        self.__window.destroy()

    def showMessage(self, message):
        self.__message.set(message)
        self.__window.update_idletasks()

    def askRank(self):
        self.__window.mainloop()
        return self.__rank.get()
