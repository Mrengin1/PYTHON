from tkinter import *

count = 0
def click():
    global count
    count+=1
    print(count)
    

window = Tk()

button = Button(window,
                text="click me!",
                command=click,
                font=("comic sans",30),
                fg="#00FF00",
                bg="black",
                activebackground="#00FF00",
                activeforeground="black",
                state=ACTIVE)
button.pack()

window.mainloop()
