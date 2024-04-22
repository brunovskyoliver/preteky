import tkinter, random

screen_width = 750
screen_height = 450

t = tkinter.Tk()
c = tkinter.Canvas(width=screen_width,height=screen_height,bg="white")
c.pack()

c.create_rectangle(0,0,100,100)


t.mainloop()
