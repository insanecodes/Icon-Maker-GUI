# Import Libraries
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
import os
from PIL import Image


class converter_window:
    def __init__(self, root):
        self.root = root
        # Change the title
        self.root.title("Icon Maker")
        # Change the window size
        self.root.geometry("500x240")
        # no resize for both directions
        self.root.resizable(False, False)
        # Change icon
        self.root.iconbitmap('icon.ico')

        # set gui widgets
        self.title = Label(self.root, text="Icon Maker", font=(
            'helvetica', 24), fg="blue")
        self.title.place(x=160, y=4)

        Label(self.root, text="Select Input Image", font=(
            'helvetica', 11), fg="blue").place(x=43, y=70)

        self.input = Entry(self.root, width=42, font=(
            'helvetica', 10), bg="lightgrey", relief=GROOVE, borderwidth=2)
        self.input.place(x=45, y=100, height=33)

        btn_convert = Button(self.root, relief=FLAT, text="Choose File", font=(
            'helvetica', 10, 'bold'), bg="blue", fg="white", command=self.openFile)
        btn_convert.place(x=355, y=100, width=95, height=32)

        btn_convert = Button(self.root, relief=FLAT, text="Convert to ICO", font=(
            'helvetica', 12, 'bold'), bg="blue", fg="white", command=self.convertToICO)
        btn_convert.place(x=182, y=163, width=130, height=40)

    def openFile(self):
        '''function for dialog box to select input image file'''
        global img, import_file_path
        import_file_path = tkinter.filedialog.askopenfilename(defaultextension=".png", filetypes=[(
            "PNG files", "*.png"), ("jpeg files", "*.jpg"),  ("All Files", "*.*")])
        self.input.delete(0, END)
        self.input.insert(0, import_file_path)
        img = Image.open(import_file_path)

    def convertToICO(self):
        '''function for converting input image to ico format'''
        global img, import_file_path
        print(os.path.exists(import_file_path))
        if os.path.exists(import_file_path) == True:
            if os.path.isfile(import_file_path) == True:
                export_file_path = tkinter.filedialog.asksaveasfilename(
                    defaultextension='.ico', filetypes=[("ico files", "*.ico")])
                img.save(export_file_path)
                messagebox.showinfo("Success", "File converted and saved")
        else:
            messagebox.showerror("Failed", "Image file's path does not exists")


if __name__ == "__main__":
    img = ""
    import_file_path = ""
    root = Tk()
    obj = converter_window(root)
    root.mainloop()
