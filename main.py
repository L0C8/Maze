import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutInit, glutWireCube

# Initialize Pygame and GLUT
pygame.init()
glutInit()

# Create display window
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
pygame.display.set_caption("PyGame + OpenGL Cube")

# Perspective and camera setup
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (800 / 600), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -5)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 3, 1, 1)
    glutWireCube(2)
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()