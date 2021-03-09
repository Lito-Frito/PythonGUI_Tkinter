import tkinter as tk

window = tk.Tk()

# Exercise in learning how pack() places things
# Part a
frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
#frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
#frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
#frame3.pack()



#--------------------------------------------------------------------

# Exercise in manipulating frames with pack()
# Part b

# Fill in the x direction; will strecth frame to fill empty spaces
# Will do this dynamically if window dimensions are changed via dragging
# frame1.pack(fill=tk.X)
# frame2.pack(fill=tk.X)
# frame3.pack(fill=tk.X)

#---------------------------------------

# Exercise in manipulating frames with pack()
# Part c

# Places frames to the left like Bey and fills in the Y direction like Kyoshi
# This means they're stacked left to right, not vertically
# frame1.pack(fill=tk.Y, side=tk.LEFT)
# frame2.pack(fill=tk.Y, side=tk.LEFT)
# frame3.pack(fill=tk.Y, side=tk.LEFT)

#---------------------------------------

# Exercise in manipulating frames with pack()
# Part d

# Making each frame have fixed dimensions AND responsive to window changes
frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
