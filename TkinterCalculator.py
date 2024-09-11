from tkinter import *
from tkinter import font

window = Tk()
window.title("Calculator คอบ. 2")
# font size
button_font = font.Font(size="20")
entry_font = font.Font(size="30")


getValue = Entry(width=70,justify="right",font=entry_font).grid(row=0, column=0,columnspan=4,pady=20,padx=0,sticky="ew")

clear = Button(text="C",font=button_font,width=4).grid(row=1, column=3)
plus = Button(text="+",font=button_font,width=4).grid(row=2, column=3)

bt_one = Button(text="1",font=button_font,width=4).grid(row=2, column=0)
bt_two = Button(text="2",font=button_font,width=4).grid(row=2, column=1)
bt_three = Button(text="3",font=button_font,width=4).grid(row=2, column=2)
bt_four = Button(text="4",font=button_font,width=4).grid(row=3, column=0)
bt_five = Button(text="5",font=button_font,width=4).grid(row=3, column=1)
bt_six = Button(text="6",font=button_font,width=4).grid(row=3, column=2)
bt_seven = Button(text="7",font=button_font,width=4).grid(row=4, column=0)
bt_eight = Button(text="8",font=button_font,width=4).grid(row=4, column=1)
bt_nine = Button(text="9",font=button_font,width=4).grid(row=4, column=2)
bt_zero = Button(text="0",font=button_font,width=4).grid(row=5, column=1)

window.grid_columnconfigure(0, weight=1)
window.geometry("300x400")
window.minsize(300, 400)
window.mainloop()