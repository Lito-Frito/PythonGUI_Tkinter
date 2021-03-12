import tkinter as tk

window = tk.Tk()

# Only 1 row, hence 0
window.columnconfigure(0, minsize=250)
# Two columns though, so we specify with [0,1]
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0)

label2 = tk.Label(text="B")
label2.grid(row=1, column=0)

window.mainloop()
