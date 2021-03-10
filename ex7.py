import tkinter as tk


window = tk.Tk()

<<<<<<< HEAD
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
=======

frame = tk.Frame(master=window, width=150, height=150)

frame.pack()


label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")

label1.place(x=0, y=0)


label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")

label2.place(x=75, y=75)

>>>>>>> 757e9f1839baadaba1d9c99c3e11c2b45283aa7b

window.mainloop()
