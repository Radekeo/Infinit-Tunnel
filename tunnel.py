import pygame as pg
import moderngl as mgl

import glm
import numpy as np

WIN_SIZE = (1280,720)

class Tunnel:
    def __init__(self,app):
        self.app = app
        self.ctx = app.ctx
        self.resolution = glm.vec2(self.app.resolution)
        self.time = pg.time.get_ticks() / 1000.0
        self.shader = self.load_program()
        self.oninit()

    def oninit(self):
        self.shader['resolution'].value = self.resolution
        self.shader['time'].value = self.time

    def load_program(self):
        with open('shader.vert') as f:
            vs = f.read()
        with open('shader.frag') as f:
            fs = f.read()
        shader_program = self.ctx.program(vertex_shader=vs, fragment_shader=fs)

        return shader_program

    def update(self):
        # use the shader program
        self.shader.use()
        
        # Render a quad covering the entire window
        self.ctx.screen.vertex_attrib_pointer(0, 2, 0, 0)
        self.ctx.screen.enable_vertex_attrib_array(0)
        self.ctx.screen.draw_arrays(mgl.TRIANGLE_STRIP, vertices=(-1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 1.0))

    def quit():
        self.shader.release()
