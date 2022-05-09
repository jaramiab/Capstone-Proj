from tkinter import*
from tkinter import ttk
import tkinter as tk

root = Tk()
root.geometry('550x800')
root.title('Market')
root.resizable(False, False)


main_frame = Frame(root, bg='blue')
main_frame.pack(expand=True, fill=BOTH)

my_canvas = Canvas(main_frame, bg='white')
my_canvas.pack(side=LEFT, fill=BOTH, expand=True)


scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
scroll.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=scroll.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

secondFrame = Frame(my_canvas)
my_canvas.create_window((0,0), window=secondFrame, anchor='nw')
price = Button(secondFrame, text='Price', command=None, borderwidth=0)
price.pack(anchor=NE, side=RIGHT)

my_canvas.create_rectangle(10, 120, 500, 10, fill='grey')
my_canvas.create_rectangle(10, 250, 500, 125, fill='grey')
my_canvas.create_rectangle(10, 380, 500, 255, fill='grey')
my_canvas.create_rectangle(10, 500, 500, 385, fill='grey')
my_canvas.create_rectangle(10, 505, 500, 645, fill='grey')
my_canvas.create_rectangle(10, 650, 500, 780, fill='grey')
my_canvas.create_rectangle(10, 790, 500, 880, fill='grey')
my_canvas.create_text(50, 20, fill='black', font='Arial', text='Item Name')
my_canvas.create_text(75, 65, fill='black', font='Arial 15', text='Item Description')


root.mainloop()