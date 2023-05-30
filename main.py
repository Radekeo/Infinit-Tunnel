import pygame as pg
import moderngl as mgl
import sys

from tunnel import *


class App:
    def __init__(self):
        pg.init()
        self.resolution = self.width, self.height = (1280, 720)
        pg.display.set_mode(self.resolution, flags=pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)

        self.ctx = mgl.create_context()

        self.clock = pg.time.Clock()
        self.time = None
        self.tunnel = Tunnel(self)

    def render(self):
        self.ctx.clear(color=(0, 1, 0.6))

        self.tunnel.update()


    def quit(self):
        self.tunnel.quit()
        pg.quit()
        sys.exit()

    def run(self):
        while True:
            self.render()
            # self.shader.run()
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.quit()

            self.clock.tick(60)
            # pg.display.set_caption(f'FPS: {self.clock.get_fps() :.2f}')


if __name__ == '__main__':
    app = App()
    app.run()
