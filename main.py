from tkinter import *
import parser
# get user input and place in display
i = 0


def getVariable(num):
    global i
    display.insert(i, num)
    i += 1


def clear_all():
    display.delete(0, END)


def undo():
    old_string = display.get()
    if len(old_string):
        new_string = old_string[:-1]
        clear_all()
        display.insert(0, new_string)


root = Tk()
root.title('Calculator')

# display input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

# adding buttons
Button(root, text="1", command=lambda: getVariable(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: getVariable(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: getVariable(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: getVariable(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: getVariable(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: getVariable(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: getVariable(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: getVariable(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: getVariable(9)).grid(row=4, column=2)

Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", command=lambda: getVariable(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: getVariable(E)).grid(row=5, column=2)

Button(root, text="+").grid(row=2, column=3)
Button(root, text="-").grid(row=3, column=3)
Button(root, text="*").grid(row=4, column=3)
Button(root, text="/").grid(row=5, column=3)

# adding other buttons
Button(root, text="pi").grid(row=2, column=4)
Button(root, text="%").grid(row=3, column=4)
Button(root, text="(").grid(row=4, column=4)
Button(root, text="exp").grid(row=5, column=4)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="x!").grid(row=3, column=5)
Button(root, text=")").grid(row=4, column=5)
Button(root, text="^2").grid(row=5, column=5)

root.mainloop()
