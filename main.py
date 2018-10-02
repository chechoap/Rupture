import time
import tkinter as tk
import util
import DialogueHandler

__author__ = "Lapse"

dh = DialogueHandler
dh.introtext()

uc = input
print("a. Go left (Stairs to the second floor).\nb. Go right.(Deeper into the first floor")

# validation to receive either "a" or "b"
while uc != "a" or uc != "b":
    if(uc == "a" or uc== "b"):
        break
    else:
        print("Pick a or b.")
        uc = input()

dh.choices(uc)











"""def lineSkipper(label):

    def cicle():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, cicle)
    cicle()


# Drawing and packing everything into 'window' which is the main window the user is going to see.

window = tk.Tk()
label = tk.Label(window, fg="green")
label.pack()
lineSkipper(label)
window.mainloop()



for TextLine in script:
    if "police" in TextLine:
        print(TextLine)


"""
