from tkinter import *
from tkinter.ttk import *


def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(ventana)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,text="This is a new window").pack()


label = Label(ventana,text="This is the main window")

# creamos la ventana
ventana = Tk()
ventana.title("DentiX")
ventana.geometry("500x700")

btn = Button(ventana,text="Click to open a new window",command=openNewWindow)









ventana.mainloop()













