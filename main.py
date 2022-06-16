from tkinter import ttk, filedialog
import tkinter as tk
from PyPDF2 import PdfFileReader

root = tk.Tk()
root.resizable(0, 0)

#temp
print(root.winfo_screenheight())
print(root.winfo_screenwidth())
print(root.winfo_reqheight())
print(root.winfo_reqwidth())
print(root.winfo_height())
print(root.winfo_width())

#screen in center of screen
x_coordinate = int(root.winfo_screenwidth()/2 - 375/2)
y_coordinate = int(root.winfo_screenheight()/2 - 185/2)
root.geometry(f"358x115+{x_coordinate}+{y_coordinate}")

#classes and def.
class Tkinter:
    def __init__(self, master):
        self.label = ttk.Label(master, text = "Edit PDF's")
        self.label.config(font = ("Arial", 18))
        self.label.grid(row = 0, columnspan = 3, padx = 3, pady = 8)

        self.button1 = ttk.Button(master, text = "rotate", width = 15, command = self.rotate)
        self.button1.grid(row = 1, column = 0, ipady = 2)

        self.button2 = ttk.Button(master, text = "split", width = 15, command = self.split)
        self.button2.grid(row = 1, column = 1)

        self.button3 = ttk.Button(master, text = "combine", width = 15, command = self.combine)
        self.button3.grid(row = 1, column = 2)

        self.label2 = ttk.Label(master, text = "Enjoy!")
        self.label2.config(font = ("Arial", 10))
        self.label2.grid(row = 2, columnspan = 3, padx = 160, pady = 8)

    def destroy(self):
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.label.destroy()
        self.label2.destroy()

    # def new_design(self, master):
    #     self.entry1 = ttk.Entry(master, width = 40)
    #     self.entry1.grid(row = 0, column = 0)

    def rotate(self):
        self.destroy()
        #self.new_design()

        #self.files = filedialog.askopenfilenames()

    def split(self):
        self.destroy()
        print("split")

    def combine(self):
        self.destroy()
        print("combine")

class PDF:
    pass


if __name__ == "__main__":
    Tkinter(root)
    root.mainloop()