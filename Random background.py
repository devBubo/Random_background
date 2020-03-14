from tkinter import *
from random import randint
root=Tk()
root.title('Random background')
canvas=Canvas()
canvas.pack()
colors=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
click_x=5000
click_y=5000
def ColorChange():
    global red
    global green
    global blue
    red=''
    green=''
    blue=''
    for i in range(2):
            red+=str(colors[randint(0,15)])
            green+=str(colors[randint(0,15)])
            blue+=str(colors[randint(0,15)])
def Click(coordinate):
    global click_x
    global click_y
    click_x = coordinate.x
    click_y = coordinate.y
canvas.bind('<Button 1>', Click)
ColorChange()
while True:


    canvas.create_rectangle(300,50,500,100,fill='gray')
    
    canvas.create_text(400,75,font=("Purisa", 30),text="Click me",fill='white')
    canvas.config(width=800,height=600,bg='#'+str(red)+str(green)+str(blue))
    if click_x>300 and click_x<500 and click_y>50 and click_y<100:
        ColorChange()
        click_x=5000
        click_y=5000
    root.update()
