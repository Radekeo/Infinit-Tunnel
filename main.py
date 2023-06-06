import sys

import pygame as pg
import moderngl as mgl
import numpy as np
import glm


WIN_SIZE = WIDTH, HEIGHT = (1280, 720)
IMG = pg.image.load('img.jpg')
PI = glm.pi()

class App:
    def __init__(self):
        pg.init()

        self.resolution = glm.vec2(WIN_SIZE)
        self.screen = pg.display.set_mode(WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF| pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.ctx = mgl.create_context()
        self.time = 0

        self.shader = self.load_program()
        self.vbo = self.get_buffer()
        self.vao = self.ctx.vertex_array(self.shader, [(self.vbo, '3f 2f', 'in_position', 'in_texcoord_0')])

        self.texture = pg.transform.flip(IMG.convert(), flip_x=False, flip_y=True)
        self.on_init()

    def on_init(self):
        self.texture = self.ctx.texture(size=self.texture.get_size(), components=3, data=pg.image.tostring(self.texture, 'RGB'))

        # Uniforms
        self.shader['u_texture_0'] = 0
        self.texture.use(0)
        self.shader['PI'] = PI
        self.shader['iRes'] = self.resolution



    def load_program(self):
        with open('shader.vert') as f:
            vs = f.read()
        with open('shader.frag') as f:
            fs = f.read()

        program = self.ctx.program(vertex_shader=vs, fragment_shader=fs)

        return program

    def get_buffer(self):
        vertex_data = (-1.0, 1.0, 0.0, 0.0, 0.0,    #topleft
                        1.0, 1.0, 0.0, 0.0, 1.0,    #topright
                        -1.0, -1.0, 0.0, 1.0, 0.0,  #bottomleft
                        1.0, -1.0, 0.0, 1.0, 1.0,   #bottomright
                    )
        vertex_data = np.array(vertex_data, dtype='f4')
        buffer = self.ctx.buffer(vertex_data)
        return buffer

    def quit(self):
        self.vao.release()
        self.vbo.release()
        self.texture.release()
        self.shader.release()
        pg.quit()
        sys.exit()

    def run(self):
        while True:
            self.ctx.clear(color=(0.08, 0.16, 0.18))

            self.time = pg.time.get_ticks() * 0.001 #time in seconds
            self.shader['u_time'].value = self.time

            self.vao.render(mode=mgl.TRIANGLE_STRIP)

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.quit()

            self.clock.tick(60)
            pg.display.flip()
            pg.display.set_caption('PyTunnel')


if __name__ == '__main__':
    app = App()
    app.run()
