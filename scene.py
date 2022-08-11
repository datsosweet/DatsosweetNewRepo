from manim import *

class Testing(Scene):
    def construct(self):

        tri = Triangle().scale(3).to_edge(DL)

        self.play(Create(tri))
        self.wait()
