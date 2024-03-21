from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Global variables
gamePaused = False

'''MPL Code from Lab 2: Lines 8 to 116'''
#Start of MPL
def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def draw_using_mpl(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    x0, y0 = convert_to_zone_0(zone, x0, y0)
    x1, y1 = convert_to_zone_0(zone, x1, y1)
    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    dne = 2 * dy - 2 * dx
    de = 2 * dy
    for i in range(x0, x1):
        a, b = convert_back_to_original(zone, x0, y0)
        if d >= 0:
            d = d + dne
            draw_points(a, b)
            x0 += 1
            y0 += 1
        else:
            d = d + de
            draw_points(a, b)
            x0 += 1

def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) > abs(dy): #For Zone 0, 3, 4 & 7
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else: #For zone 1, 2, 5 & 6
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6

def convert_to_zone_0(zone, x0, y0):
    if zone == 0:
        return x0, y0
    elif zone == 1:
        return y0, x0
    elif zone == 2:
        return -y0, x0
    elif zone == 3:
        return -x0, y0
    elif zone == 4:
        return -x0, -y0
    elif zone == 5:
        return -y0, -x0
    elif zone == 6:
        return -y0, x0
    elif zone == 7:
        return x0, -y0
   
def convert_back_to_original(zone, x0, y0):
    if zone == 0:
        return x0, y0
    if zone == 1:
        return y0, x0
    if zone == 2:
        return -y0, -x0
    if zone == 3:
        return -x0, y0
    if zone == 4:
        return -x0, -y0
    if zone == 5:
        return -y0, -x0
    if zone == 6:
        return y0, -x0
    if zone == 7:
        return x0, -y0
    
def draw_arrow():
    glColor3f(0.0, 1.0, 1.0)
    draw_using_mpl(500, 9000, 1000, 9000)
    draw_using_mpl(500, 9000, 750, 9250)
    draw_using_mpl(500, 9000, 750, 8750)

def draw_cross():
    glColor3f(1.0, 0.0, 0.0)
    draw_using_mpl(9000, 9250, 9500, 8750)
    draw_using_mpl(9000, 8750, 9500, 9250)

def draw_pause_button():   
    glColor3f(1.0, 1.0, 0.0)
    draw_using_mpl(4900, 9250, 4900, 8750)
    draw_using_mpl(5100, 9250, 5100, 8750)

def draw_play_button():
    glColor3f(1.0, 1.0, 0.0)
    draw_using_mpl(4800, 9250, 5200, 9000)
    draw_using_mpl(4800, 9250, 4800, 8750)
    draw_using_mpl(4800, 8750, 5200, 9000)
#End of MPL

def drawAxes():
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(5000, 0)
    glVertex2f(5000, 10000)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0, 5000)
    glVertex2f(10000, 5000)
    glEnd()

def draw_points_circle(x, y, cx, cy):
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x + cx, y + cy)  # Adjust the center coordinates
    glEnd()

def MidpointCircle(r, cx, cy):
    d = 1 - r
    x = 0
    y = r
    Circlepoints(x, y, cx, cy)
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * x - 2 * y + 5
            x += 1
            y -= 1
        Circlepoints(x, y, cx, cy)

def Circlepoints(x, y, cx, cy):
    draw_points_circle(x, y, cx, cy)
    draw_points_circle(y, x, cx, cy)
    draw_points_circle(y, -x, cx, cy)
    draw_points_circle(x, -y, cx, cy)
    draw_points_circle(-x, -y, cx, cy)
    draw_points_circle(-y, -x, cx, cy)
    draw_points_circle(-y, x, cx, cy)
    draw_points_circle(-x, y, cx, cy)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 10000, 0.0, 10000, 0.0, 1.0)
    #glOrtho(-250.0, 250, -250.0, 250, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global gamePaused
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    #drawAxes()
    MidpointCircle(300, 5000, 500)  # Set the center coordinates (50, 50)
    draw_arrow()
    draw_cross()
    if gamePaused:
        draw_play_button()
    else:
        draw_pause_button()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutMainLoop()
