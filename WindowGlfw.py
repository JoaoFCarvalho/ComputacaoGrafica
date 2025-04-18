import glfw
from OpenGL.GL import *
import time

if not glfw.init():
    raise Exception("Falha ao inicializar GLFW")

glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)

window = glfw.create_window(800, 600, "Janela (OpenGL 2.1 Legacy)", None, None)

if not window:
    glfw.terminate()
    raise Exception("Não foi possível criar a janela OpenGL Legacy")

glfw.make_context_current(window)

print("Versão OpenGL:", glGetString(GL_VERSION).decode())

glClearColor(0.0, 0.0, 0.0, 1.0)

start = time.time()

while not glfw.window_should_close(window) and time.time() - start < 10:
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
