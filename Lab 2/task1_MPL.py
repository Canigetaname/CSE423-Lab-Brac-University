from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
#inZoneZero = True
zone = 0

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def checkZone(dx, dy):
    global zone
    if dx>0 and dy>0:
        if abs(dx) > abs(dy):
            zone = 0
            #isZoneZero = True
        else:
            zone = 1
    elif dx<0 and dy>0:
        if abs(dx)>abs(dy):
            zone = 3
        else:
            zone = 2
    elif dx<0 and dy<0:
        if abs(dx)>abs(dy):
            zone = 4
        else:
            zone = 5
    elif dx>0 and dy<0:
        if abs(dx)>abs(dy):
            zone = 7
        else:
            zone = 6
    return zone

def draw_line(x1, y1, x2, y2):
    global zone
    #draw_points(x1, y1)
    #draw_points(x2, y2)
    dx = x2 - x1
    dy = y2 - y1
    zone = checkZone(dx, dy)
    if zone==0:
        if x2 >= x1:
            use_mpl(x1, y1, x2, y2, dx, dy)
        else:
            use_mpl(x2, y2, x1, y1, dx, dy)
    else:
        x1, y1 = convert_to_zone(x1, y1)
        x2, y2 = convert_to_zone(x2, y2)
        dx = x2 - x1
        dy = y2 - y1
        if x2 >= x1:
            use_mpl(x1, y1, x2, y2, dx, dy)
        else:
            use_mpl(x2, y2, x1, y1, dx, dy)

def convert_to_zone(x, y):
    global zone
    if zone==1:
        x, y = y, x
    elif zone==2:
        x, y = -y, x
    elif zone==3:
        x, y = -x, y
    elif zone==4:
        x, y = -x, -y
    elif zone==5:
        x, y = -y, -x
    elif zone==6:
        x, y = y, -x
    elif zone==7:
        x, y = x, -y
    return x, y

def loop_of_mpl(x, y, dx, dy, res1, res2, d):
    if d>0:
        d = d + res2
        x+=1
        y+=1
    else:
        d = d + res1
        x+=1
    return x, y, d

def use_mpl(x1, y1, x2, y2, dx, dy):
    x = x1
    y = y1
    #res1 = 2dy
    res1 = 2*dy
    #res2 = 2dy - 2dx = res1 - 2dx
    res2 = res1 - 2*dx
    d = res1 - dx
    while x<=x2 and y<=y2:
        x, y, d = loop_of_mpl(x, y, dx, dy, res1, res2, d)
        if zone==0:
            draw_points(x,y)
        else:
            x_new, y_new = convert_to_zone(x,y)
            draw_points(x_new, y_new)

def drawAxes():
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(250,0)
    glVertex2f(-250,0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0,250)
    glVertex2f(0,-250)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250.0, 250.0, -250.0, 250.0, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    #draw_points(250, 250)
    drawAxes()
    #Checking code with different inputs
    #draw_line(0, 2, 70, 52)
    #draw_line(70, 52, 0, 2)
    #draw_line(-30, 20, 90, 40)
    #draw_line(20, -30, 40, 90)
    #draw_line(-10, -20, -20, 70) 
    #draw_line(-100, 100, 200, 200) #zone 0
    #draw_line(100, -200, 200, -100) #zone 1
    #draw_line(-200, 100, -100, 200) #zone 2
    #draw_line(-100, -200, -200, -100) #zone 3 (problem)
    #draw_line(200, -100, 100, -200) #zone 4
    #draw_line(-200, -100, -100, -200) #zone 5 (problem)
    #draw_line(100, 200, 200, 100) #zone 6 (problem)
    #raw_line(-100, 200, -200, 100) #zone 7
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(display)
glutMainLoop()