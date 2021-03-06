from tkinter import *

canvas_width = 500
canvas_height = 150

def paint( event ):
   global python_green
   python_green =("#80DEEA")
   x1, y1 = ( event.x - 2 ), ( event.y - 2 )
   x2, y2 = ( event.x + 2 ), ( event.y + 2 )
   w.create_oval( x1, y1, x2, y2, fill = ("#80DEEA"))

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
m

mainloop()