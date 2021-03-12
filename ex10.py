import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 4], minsize=100)

label1 = tk.Label(text="A")
# Sets Label1 to stick to Northern border
label1.grid(row=0, column=0, sticky="n")

label2 = tk.Label(text="B")
# Sets Label2 to stick to Northern border
label2.grid(row=1, column=0, sticky="n")

label3 = tk.Label(text="C")
# Sets Label3 to stick to Northeastern border
label3.grid(row=1, column=0, sticky="ne")

label4 = tk.Label(text="D")
# Sets Label4 to stick to Southwestern border
label4.grid(row=1, column=0, sticky="sw")


window.mainloop()
