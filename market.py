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
my_canvas.create_window((0,0), window=secondFrame)

#Grey Blocks
my_canvas.create_rectangle(10, 120, 500, 10, fill='grey')
my_canvas.create_rectangle(10, 250, 500, 125, fill='grey')
my_canvas.create_rectangle(10, 380, 500, 255, fill='grey')
my_canvas.create_rectangle(10, 500, 500, 385, fill='grey')
my_canvas.create_rectangle(10, 505, 500, 645, fill='grey')
my_canvas.create_rectangle(10, 650, 500, 780, fill='grey')
my_canvas.create_rectangle(10, 790, 500, 880, fill='grey')

#First Block Text
my_canvas.create_text(50, 20, fill='black', font='Arial', text='Item Name')
my_canvas.create_text(75, 65, fill='black', font='Arial 15', text='Item Description')
price = Button(my_canvas, text='Price', command=None, borderwidth=0)
price.pack(padx=35, pady=25, anchor=E)

#Second Block Text
my_canvas.create_text(50, 135, fill='black', font='Arial', text='Item Name')
my_canvas.create_text(75, 180, fill='black', font='Arial 15', text='Item Description')
price2 = Button(my_canvas, text='Price', command=None, borderwidth=0)
price2.pack(padx=35, pady=125, anchor=E)

#Third Block Text
my_canvas.create_text(50, 265, fill='blue', font='Arial', text='Item Name')
my_canvas.create_text(75, 300, fill='blue', font='Arial 15', text='Item Description')
price3 = Button(my_canvas, text='Price', command=None, borderwidth=0)
price3.pack(padx=35, pady=275, anchor=E)

#Fourth Block Text
my_canvas.create_text(50, 400, fill='red', font='Arial', text='Item Name')
my_canvas.create_text(75, 435, fill='red', font='Arial 15', text='Item Description')
price4 = Button(my_canvas, text='Price', command=None, borderwidth=0)
price4.pack(padx=35, pady=135, anchor=E)

#Fifth Block Text
my_canvas.create_text(50, 665, fill='black', font='Arial', text='Item Name')
my_canvas.create_text(75, 700, fill='black', font='Arial 15', text='Item Description')
price5 = Button(my_canvas, text='Price', command=None, borderwidth=0)
price5.pack(padx=35, pady=650, anchor=E)

#Sixth Block Text
my_canvas.create_text(50, 520, fill='green', font='Arial', text='Item Name')
my_canvas.create_text(75, 570, fill='green', font='Arial 15', text='Item Description')
price6 = Button(my_canvas, text='Price', command=None, borderwidth=0)
price6.pack(padx=35, pady=790, anchor=E)

root.mainloop()