import tkinter as tk

root = tk.Tk()
root.title("Checkbox Example")

var = tk.BooleanVar()   # Stores True / False

checkbox = tk.Checkbutton(root, text="Enable feature", variable=var)
checkbox.pack()

def show_state():
    print(var.get())

tk.Button(root, text="Check State", command=show_state).pack()

root.mainloop()
