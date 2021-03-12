import tkinter as tk

window = tk.Tk()

# Generate rows with:
for i in range(3):
    # Weight tells Tkinter how to respond as the window is resized
    # Minsize ensures that text isn't cut off
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    # Generate columns with:
    for j in range(0,3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )

        # Breaks up window into rows and columns
        frame.grid(row=i, column=j, padx=5, pady=5)

        label=tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()
