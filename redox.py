from manim import *
from oxidation import Oxidation
from reduction import Reduction

class Redox(Scene):
    def construct(self):
        Oxidation.construct(self)
        self.remove(*self.mobjects)
        Reduction.construct(self)
