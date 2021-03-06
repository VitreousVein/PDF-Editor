from tkinter import CENTER, X, ttk, filedialog
import tkinter as tk
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

class Initiation:
    global root
    root = tk.Tk()
    root.resizable(0, 0)

    #screen in center of screen
    # x_coordinate = int(root.winfo_screenwidth()/2 - 375/2)
    # y_coordinate = int(root.winfo_screenheight()/2 - 185/2)
    # root.geometry(f"358x115+{x_coordinate}+{y_coordinate}")

#classes and def.
class Tkinter:
    def __init__(self, master):
        self.set_location = tk.StringVar()
        self.set_location2 = tk.StringVar()
        self.set_page = tk.StringVar()

        self.label = ttk.Label(master, text = "Edit PDF's")
        self.label.config(font = ("Arial", 18))
        self.label.grid(row = 0, columnspan = 3, padx = 3, pady = 8)

        self.button1 = ttk.Button(master, text = "rotate to the right", width = 20, command = self.rotate_right)
        self.button1.grid(row = 1, column = 0, ipady = 2, padx = 5)

        self.button5 = ttk.Button(master, text = "rotate to the left", width = 20, command = self.rotate_left)
        self.button5.grid(row = 2, column = 0, ipady = 2, padx = 5, pady = 5)

        self.button6 = ttk.Button(master, text = "rotate for 180°", width = 20, command = self.rotate_180)
        self.button6.grid(row = 3, column = 0, ipady = 2, padx = 5)

        self.button2 = ttk.Button(master, text = "split", width = 15, command = self.split)
        self.button2.grid(row = 1, column = 1, padx = 5)

        self.button3 = ttk.Button(master, text = "merge", width = 20, command = self.merge)
        self.button3.grid(row = 1, column = 2, padx = 5)

        # self.label2 = ttk.Label(master, text = "Enjoy!")
        # self.label2.config(font = ("Arial", 10))
        # self.label2.grid(row = 2, columnspan = 3, padx = 160, pady = 8)

        self.label3 = ttk.Label(master, text = "Insert PDF Location:")
        self.label3.grid(row = 5, column = 0)
        
        self.entry = ttk.Entry(master, width = 50, textvariable = self.set_location)
        self.entry.grid(row = 5, column = 1, pady = 0, padx = 0)

        self.button4 = ttk.Button(master, text = "Go!", command = self.exit_program, width = 15)
        self.button4.grid(row = 6, column = 2)

        self.label4 = ttk.Label(master, text = "Put the number of page to modify:")
        self.label4.grid(row = 4, columnspan = 3, padx = 0, ipadx = 120)

        self.entry2 = ttk.Entry(master, width = 4, justify = "center", textvariable = self.set_page)
        self.entry2.grid(row = 4, column = 1, padx = 0, ipadx = 0)

        self.entry3 = ttk.Button(master, width = 50, textvariable = self.set_location2)
        self.entry3.grid(row = 6, column = 1)

        self.label7 = ttk.Label(master, text = "Insert 2nd PDF Location:")
        self.label7.grid(row = 6, column = 0, pady = 10)
    

    def exit_program(self):
        self.watch = self.button4.quit()

    def pdf_location(self):
        self.files = filedialog.askopenfilenames()
        self.files = str(self.files)
        self.files = self.files.replace("(", "", 1).replace("'", '"')
        self.files = "".join(self.files.rsplit(",", 1))
        self.files = "".join(self.files.rsplit(")", 1))
        self.files = self.files.replace('"', "")
        self.set_location.set(self.files)
        pdf_location = str(self.set_location.get())
        print(pdf_location)
        return pdf_location

    def pdf_location2(self):
        self.files = filedialog.askopenfilenames()
        self.files = str(self.files)
        self.files = self.files.replace("(", "", 1).replace("'", '"')
        self.files = "".join(self.files.rsplit(",", 1))
        self.files = "".join(self.files.rsplit(")", 1))
        self.files = self.files.replace('"', "")
        self.set_location2.set(self.files)
        pdf_location = str(self.set_location2.get())
        print(pdf_location)
        return pdf_location


    def page_number(self):
        page_number = self.set_page.get()
        if self.set_page.get() == "all" or self.set_page.get() == "":
            page_number = PdfFileReader(self.set_location.get()).getNumPages()
            page_number = PdfFileReader(self.set_location2.get()).getNumPages()
        return page_number 

    def page_number_all(self):
        if self.set_page.get() == "all" or self.set_page.get() == "":
            page_number_all = True
        else:
            page_number_all = False
        return page_number_all


    def rotate_right(self):
        PDF.rotate_right()

    def rotate_left(self):
        PDF.rotate_left()
        
    def rotate_180(self):
        PDF.rotate_180()
        

    def split(self):
        PDF.split()
 

    def merge(self):
        PDF.merge()


class PDF:
    def rotate_right():
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(tkinter.pdf_location())
        if tkinter.page_number_all() == True:
            i = 0
            while i <= (tkinter.page_number() - 1):
                page_i = pdf_reader.getPage(i).rotateClockwise(90)
                pdf_writer.addPage(page_i)
                i += 1
                print(i)
        elif tkinter.page_number_all() == False:
            page_1 = pdf_reader.getPage(int(tkinter.set_page.get()) - 1).rotateClockwise(90)
            pdf_writer.addPage(page_1)
        with open(tkinter.set_location.get(), 'wb') as fh:
            pdf_writer.write(fh)
    
    def rotate_left():
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(tkinter.pdf_location())
        if tkinter.page_number_all() == True:
            i = 0
            while i <= (tkinter.page_number() - 1):
                page_i = pdf_reader.getPage(i).rotateClockwise(270)
                pdf_writer.addPage(page_i)
                i += 1
                print(i)
        elif tkinter.page_number_all() == False:
            page_1 = pdf_reader.getPage(int(tkinter.set_page.get()) - 1).rotateClockwise(270)
            pdf_writer.addPage(page_1)
        with open(tkinter.set_location.get(), 'wb') as fh:
            pdf_writer.write(fh)

    def rotate_180():

        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(tkinter.pdf_location())
        if tkinter.page_number_all() == True:
            i = 0
            while i <= (tkinter.page_number() - 1):
                page_i = pdf_reader.getPage(i).rotateClockwise(180)
                pdf_writer.addPage(page_i)
                i += 1
                print(i)
        elif tkinter.page_number_all() == False:
            page_1 = pdf_reader.getPage(int(tkinter.set_page.get()) - 1).rotateClockwise(180)
            pdf_writer.addPage(page_1)
        with open(tkinter.set_location.get(), 'wb') as fh:
            pdf_writer.write(fh)

    def split():
        pdf_reader = PdfFileReader(tkinter.pdf_location())

        i = 0
        while i <= (tkinter.page_number() - 1):
            print(i)
            pdf_writer = PdfFileWriter()
            page_i = pdf_reader.getPage(i)
            pdf_writer.addPage(page_i)
            output = f'{tkinter.set_location.get().replace(".pdf", "")}-page{i + 1}.pdf'
            with open(output, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
            i += 1

    def merge():
        pdf_reader1 = PdfFileReader(tkinter.pdf_location())
        pdf_reader2 = PdfFileReader(tkinter.pdf_location2())
        pdf_writer = PdfFileWriter()

        pdf_writer.appendPagesFromReader(pdf_reader1)
        pdf_writer.appendPagesFromReader(pdf_reader2)

        with open("merged_files.pdf", 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

if __name__ == "__main__":
    #Initiation()
    tkinter = Tkinter(root)
    root.mainloop()