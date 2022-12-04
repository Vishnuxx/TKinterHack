from tkinter import *
from tkinter.colorchooser import askcolor
from labelTool import *
from paintUtils import *
from PIL import Image, ImageDraw

class Paint:
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title("Editor")
        self.root.geometry('900x600')

        self.setupView()

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)
        self.setup()
        self.root.mainloop()

    def setupView(self):
        self.pen_button = labelTool(self.root , label='pen' , command=lambda e : self.use_pen())
        self.pen_button.grid(row=0, column=0)

        self.brush_button = labelTool(self.root, label='brush', command=lambda e :self.use_brush())
        self.brush_button.grid(row=0, column=1)

        self.color_button = labelTool(self.root, label='color', command=lambda e :self.choose_color())
        self.color_button.grid(row=0, column=2)

        self.eraser_button = labelTool(self.root, label='eraser', command=lambda e :self.use_eraser())
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.clear_button = labelTool(self.root, label='clear', command=lambda e :self.clearCanvas())
        self.clear_button.grid(row=0, column=5)

    def setup(self):
        self.old_x = 0
        self.old_y = 0
        
        self.brushHead = PhotoImage(file='./res/brush1.png' , height=100 , width=100 , gamma=1.0)
        self.isPen = True
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)


    def use_pen(self):
        self.activate_button(self.pen_button)
        self.isPen = True

    def use_brush(self):
        self.activate_button(self.brush_button)
        self.isPen = False

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def clearCanvas(self):
        self.c.delete("all")

    def export(self , name):
        image1 = Image.new("RGB", (width, height), white)
        draw = ImageDraw.Draw(image1)

    def resize(self , w , h):
        self.c.config(width=w, height=h)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event ):
        if self.isPen == True:
            self.drawWithPen(event=event)
        else:
            self.drawWithPaint(event=event)


    def drawWithPen(self , event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y



   
    def drawWithPaint(self , event):
       
        dist = distanceBetween(self.old_x ,self.old_y, event.x, event.y )
        angle = angleBetween(self.old_x ,self.old_y, event.x, event.y)
        print(self.brushHead)
        for i in range(int(dist)):
            if self.old_x and self.old_y:
                x = self.old_x + (math.sin(angle) * i)
                y = self.old_y + (math.cos(angle) * i)
                self.c.create_image(x, y,  image=self.brushHead.image, anchor='nw')
        self.old_x = event.x
        self.old_y = event.y


    def setBrushHead(self , filepath):
        self.brushHead = PhotoImage(file=filepath)
        print("brus")

    def reset(self, event):
        self.old_x, self.old_y = 0, 0


if __name__ == '__main__':
    Paint()