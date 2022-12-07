from tkinter import *

root = Tk()
root.title("MY WEB")
root.geometry("500x500")

# Frames
top_frame = Frame(root)

txtlbl = Label(top_frame, text="Top Frame")
txtlbl.pack()

top_frame.grid(row=0, column=0, columnspan=1)

frame_1 = Frame(root)
txtlbl = Label(top_frame, text="1 Frame")
txtlbl.pack()

frame_1.grid(row=1, column=0)

frame_2 = Frame(root)
txtlbl = Label(top_frame, text="2 Frame")
txtlbl.pack()

frame_2.grid(row=1, column=1)

frame_3 = Frame(root)
txtlbl = Label(top_frame, text="3 Frame")
txtlbl.pack()
frame_3.grid(row=1, column=2)


root.mainloop()
