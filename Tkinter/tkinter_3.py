#Imports necessary code to run the big tkinter, big ttk and big messagebox
import tkinter as tk
from tkinter import ttk, messagebox

#initailises the window
root = tk.Tk()
root.title("Hello")
root.geometry("500x250")
#creates a table for the entire window
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#creates a style in this example it's a background
# style = ttk.Style()
# style.configure("Aqua.TFrame", background="aqua")

#container widget to group up other items
# frame = ttk.Frame(root, padding=12, style="Aqua.TFrame") to get the colour
frame = ttk.Frame(root, padding=12)
frame.grid(row=0, column=0, sticky="NSEW")
frame.columnconfigure(1, weight=1)

#creates a text label and text input to store in name_var
#organise the items into a grid frame
id_var = tk.StringVar()

ttk.Label(frame, text ="Student ID:" ).grid(row=0, column=0, sticky="w", pady=6)
ttk.Entry(frame, textvariable=id_var).grid(row=0, column=1, sticky="EW", pady=6)

name_var = tk.StringVar()
ttk.Label(frame, text ="Name:" ).grid(row=1, column=0, sticky="w", pady=6)
ttk.Entry(frame, textvariable=name_var).grid(row=1, column=1, sticky="EW", pady=6)
#textvariable=name_var stores the text you put into name_var to print back

#strip() removes spaces at the ends or starts of strings being typed
#
def save(_event=None):
    if not id_var.get().strip().isdigit():
        messagebox.showerror("Error", "That is an invalid input student ID is in numbers")
        
    if not name_var.get().strip():
        messagebox.showerror("Error", "please input a name")
        
    if not id_var.get().strip():
        messagebox.showerror("Error", "please input a ID Number")
        
    if  name_var.get().strip().isdigit():
        messagebox.showerror("Error", "invalid input your name had no numbers in it")
        

#create buttin that invokes greet() function
ttk.Button(frame, text="Save and Greet", command=save).grid(row=2,column=0,columnspan=2,sticky="EW",pady=6,padx=6)
root.bind("<Return>", save)

#start tkinter prosceess
root.mainloop()

