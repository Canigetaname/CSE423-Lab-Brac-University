from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

#Global variables
gamePaused = False
score = 0
cx = 5000
gameOver= False
bubble_positions = []
bubble_speed = 80  # Speed of bubbles falling
bubble_radius = 250   # Radius of bubbles
num_bubbles = 5  # Number of bubbles to create
bubble_creation_delay = 0.5
circles = []
lives = 3
last_bubble_creation_time = time.time()

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

def initialize_bubbles():
    global bubble_positions
    bubble_positions = []
    for i in range(num_bubbles):
        x = random.randint(bubble_radius, 10000 - bubble_radius) 
        y = 10000 + i * 200
        bubble_positions.append((x, y))

def draw_bubbles():
    glColor3f(1.0, 1.0, 0.0)
    for pos in bubble_positions:
        MidpointCircle(bubble_radius, pos[0], pos[1])

def update_bubbles():
    global bubble_positions, lives, cx
    for i in range(len(bubble_positions)):
        bubble_positions[i] = (bubble_positions[i][0], bubble_positions[i][1] - bubble_speed)
        if bubble_positions[i][0]>cx-200 and bubble_positions[i][0]<cx+200 and bubble_positions[i][1]>800 and bubble_positions[i][1]<1000:
            game_over()
        if bubble_positions[i][1] < bubble_radius:
            if lives>1:
                lives-=1
                print("Lives remaining:", lives)
            else:
                game_over()
            bubble_positions[i] = (random.randint(bubble_radius, 10000 - bubble_radius), 10000 + bubble_radius)

def game_over():
    global score, gameOver
    print("Game Over!")
    print("Lives remaining: 0")
    print("Score:", score)
    print("Thanks for playing!")
    gameOver = True
    glutLeaveMainLoop()

def create_new_bubble():
    global bubble_positions, last_bubble_creation_time
    current_time = time.time()
    if current_time - last_bubble_creation_time >= bubble_creation_delay:
        last_bubble_creation_time = current_time
        x = random.randint(bubble_radius, 10000 - bubble_radius)
        y = 10000 + bubble_radius
        while any(((x - bubble[0]) ** 2 + (y - bubble[1]) ** 2) ** 0.5 <= 2 * bubble_radius for bubble in bubble_positions):
            y += 2 * bubble_radius
        bubble_positions.append((x, y))

def check_collisions():
    global circles, bubble_positions, score
    for i in range(len(circles)):
        circle_x, circle_y = circles[i]['x'], circles[i]['y']
        for j in range(len(bubble_positions)):
            bubble_x, bubble_y = bubble_positions[j][0], bubble_positions[j][1]
            distance = ((circle_x - bubble_x) ** 2 + (circle_y - bubble_y) ** 2) ** 0.5
            if distance <= bubble_radius + 50:
                del circles[i]
                bubble_positions.pop(j)
                score += 1
                print("Score:", score)
                create_new_bubble()
                return

def draw_points_circle(x, y, cx, cy):
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x + cx, y + cy) 
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

def keyboardListener(key, x, y):
    global cx, circles
    if not gamePaused:
        if cx>=500:
            if key==b'a':
                cx-=250
        if cx<=9500:
            if key==b'd':
                cx+=250
        if key == b' ': 
            circles.append({'x': cx, 'y': 800, 'velocity_y': 600})  # Adjust velocity as needed
    glutPostRedisplay()

def restartGame():
    global score, cx, circles, bubble_positions
    score = 0
    cx = 5000
    circles = []
    bubble_positions = []
    print("Starting over!")
    glutPostRedisplay()

def mouseInput(button, state, x, y):
    global gamePaused, gameOver, printed, score
    if button == GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        if x>=20 and x<= 50 and y>= 30 and y<= 60:
            restartGame()
        if x>=245 and x<=265 and y>=25 and y<=65:
            if not gamePaused:
                gamePaused = True
            else:
                gamePaused = False
        if x>=420 and x<= 490 and y>= 20 and y<= 80:
            printed = True
            print("Goodbye")
            print("Score:", score)
            gameOver = True
            glutLeaveMainLoop()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 10000, 0.0, 10000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def animate():
    global fall, gameOver, speed, height_decrease, gamePaused
    if not gameOver:
        glutPostRedisplay()
        if not gamePaused:
            update_bubbles()

def showScreen():
    global gamePaused, cx, circles, bubble_positions, num_bubbles
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    draw_bubbles()
    MidpointCircle(300, cx, 500)
    draw_arrow()
    draw_cross()
    if gamePaused:
        draw_play_button()
    else:
        draw_pause_button()
    glColor3f(1.0, 1.0, 0.0)  
    for circle in circles:
        MidpointCircle(50, circle['x'], circle['y']) 
        circle['y'] += circle['velocity_y']
    if len(bubble_positions)<num_bubbles:
        create_new_bubble()
    glutSwapBuffers()
    check_collisions()

glutInit()
initialize_bubbles()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseInput)
glutIdleFunc(animate)
glutMainLoop()
