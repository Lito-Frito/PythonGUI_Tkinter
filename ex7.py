import tkinter as tk


window = tk.Tk()

# Create a 3*3 grid of frames
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        # Key operative here is grid(), used to attach frames to window
        # Also pads frame in x & y direction in PIXELS
        frame.grid(row=i, column=j, padx=5, pady=5)
        # Label each sub grid by it's y,x coordinates
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")\
        # Attaches each label to its master grame
        # Also pads label in x & y direction in PIXELS
        label.pack(padx=5, pady=5)

# Insight: even though .grid() is called on each Frame object, the geometry
# manager applies to the window object

# Also, the layout of each frame is controlled with the .pack() geometry manager

window.mainloop()
