import tkinter.messagebox


class View:
    def __init__(self):
        self.__header = "A tiny MVC Python program"
        self.__footer = "made by JAD"
        self.__createWindow()

    def __createWindow(self):
        self.__window = tkinter.Tk()
        self.__window.title(self.__header)
        self.__rank = tkinter.IntVar(value=0)
        tkinter.Label(self.__window, text='Rank : ').pack()
        tkinter.Entry(self.__window, textvariable=self.__rank).pack()
        tkinter.Button(self.__window, text='Ok', command=lambda: self.__buttonOk()).pack()

    def __buttonOk(self):
        self.__window.destroy()

    def showMessage(self, message):
        tkinter.messagebox.showinfo(self.__header, message)

    def askRank(self):
        self.__window.mainloop()
        return self.__rank.get()
