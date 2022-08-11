from manim import *

class Testing(Scene):
    def construct(self):

        name = Tex("Dinh Tien Dat").to_edge(UR, buff = 0.5)
        sq = Square(side_length = 0.5, fill_color = RED, fill_opacity = 0.5).shift(
            LEFT * 3)
        tri = Triangle().scale(3).to_edge(DL)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), runtime = 3)
        self.play(Create(tri))
        self.wait()