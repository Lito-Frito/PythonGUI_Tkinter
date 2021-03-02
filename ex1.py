import tkinter as tk

#Create window obj using Tk class
window = tk.Tk()
#Display text using Label
label = tk.Label(text="Python rocks!")
#"Pack" label into window
label.pack()

#Display window and disable prompt until window closed (for user interaction)
window.mainloop()
