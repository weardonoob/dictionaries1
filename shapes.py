import pgzrun
WIDTH=500
HEIGHT=500
TITLE = "shapes py"

RED = (255,0,0)
BOX = Rect((40,300),(100,50))
alien=Actor("pink alien img")

Blue = (0,0,255)
box1 =Rect( (50,100), (50,100))
box2 =Rect( (100,100), (100,100))
def draw():
    screen.clear()
    screen.fill("white")
    screen.draw.circle((150,250), 65,(144,120,255))
    screen.draw.filled_circle((315,250),50,(240,12,240))
    screen.draw.rect(BOX,RED)
    screen.draw.filled_rect(BOX,RED)
    #screen.draw.text("Text color", (50, 30), color="orange")
    screen.draw.text("hello",(400,300), color="orange")
    alien.draw()
    #remove bg,
    #2 rectangles 2circles 1 vierkant
    screen.draw.rect(box2,Blue)
    screen.draw.filled_rect(box1,Blue)









pgzrun.go()