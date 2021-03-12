import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50)
# 4 Columns
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

# The below show how grid() can do some of what pack() does:

label1.grid(row=0, column=0)
# Spread fully on the horizontal plane
label2.grid(row=0, column=1, sticky="ew")
# Spread fully on the vertical plane
label3.grid(row=0, column=2, sticky="ns")
# Spread fully on both planes
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()
