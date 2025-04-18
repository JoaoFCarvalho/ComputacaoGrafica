import glfw
from OpenGL.GL import *
import numpy as np

def create_translation_matrix(tx, ty):
    return np.array([
        [1.0, 0.0, 0.0, tx],
        [0.0, 1.0, 0.0, ty],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)

def create_scale_matrix(s):
    return np.array([
        [s,   0.0, 0.0, 0.0],
        [0.0, s,   0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32)

glfw.init()
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
window = glfw.create_window(800, 600, "Translação e Escala com matriz", None, None)
glfw.make_context_current(window)

x_pos, y_pos = 0.0, 0.0
speed = 0.01

scale = 1.0
scale_speed = 0.01

while not glfw.window_should_close(window):
    glfw.poll_events()

    if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
        x_pos -= speed
    if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
        x_pos += speed
    if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
        y_pos += speed
    if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
        y_pos -= speed

    if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
        scale += scale_speed
    if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
        scale = max(0.1, scale - scale_speed)

    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    translation_matrix = create_translation_matrix(x_pos, y_pos)
    scale_matrix = create_scale_matrix(scale)

    transform = np.dot(translation_matrix, scale_matrix)
    glLoadMatrixf(transform.T)

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0, 1, 0)
    glVertex2f(0.5, -0.5)
    glColor3f(0, 0, 1)
    glVertex2f(0.0, 0.5)
    glEnd()

    glfw.swap_buffers(window)

glfw.terminate()
