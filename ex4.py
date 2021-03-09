import tkinter as tk

window = tk.Tk()

#Create entry with appropriate attributes
entry = tk.Entry(width=40, bg="white", fg="black")
entry.pack()

# 0 means to insert at the 0th position (beginning)
entry.insert(0, "What's your name? ")

window.mainloop()
