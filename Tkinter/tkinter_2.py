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

#creates a style in this example it's a backgrounf
style = ttk.Style()
style.configure("Magenta.TFrame", background="Magenta")

#container widget to group up other items
frame = ttk.Frame(root, padding=12, style="Magenta.TFrame")
frame.grid(row=0, column=0, sticky="NSEW")
frame.columnconfigure(1, weight=1)

#creates a text label and text input to store in name_var
#organise the items into a grid frame
name_var = tk.StringVar()
ttk.Label(frame, text ="Name:" ).grid(row=0, column=0, sticky="w", pady=6)
ttk.Entry(frame, textvariable=name_var).grid(row=0, column=1, sticky="EW", pady=6)
#textvariable=name_var stores the text you put into name_var to print back

def greet():
    """
    show info messagge box greeting user by name
    """
    # """""" makes a comment for functions in longer projects
    messagebox.showinfo("Hello", f"Hi {name_var.get().strip()}")

#create buttin that invokes greet() function
ttk.Button(frame, text="Greet", command=greet).grid(row=1,column=0,columnspan=2,sticky="EW",pady=6,padx=6)

#start tkinter prosceess
root.mainloop()