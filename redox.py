from manim import *
from oxidation import Oxidation
from reduction import Reduction
from cell import Cell
import constants


class Redox(Scene):
    def construct(self):
        # Make cell
        cell = Cell()
        constants.bulk_play(self, Create(cell.anode), Create(cell.cathode), Create(cell.electrolyte), run_time=constants.SHORT_ANIMATION_TIME)
        constants.bulk_play(self, [Create(cell.anode_text), Create(cell.cathode_text)], run_time=constants.SHORT_ANIMATION_TIME)
        self.wait(constants.LONG_DWELL_TIME)

        # Play other animations
        self.remove(*self.mobjects)
        Oxidation.construct(self)
        self.remove(*self.mobjects)
        Reduction.construct(self)
        self.remove(*self.mobjects)

        self.add(*cell.cell_group)

        # Make Li, S, e-
        li1 = Circle(0.4, GRAY_C, fill_opacity=1).move_to((-3, 0.7, 0))
        li2 = li1.copy().move_to((-3, -0.7, 0))
        e1 = Circle(0.2, BLUE_B, fill_opacity=1).move_to((-2, 0.7, 0))
        e2 = e1.copy().move_to((-2, -0.7, 0))
        s = Circle(0.4, YELLOW_A, fill_opacity=1).move_to((3, 0, 0))

        li2s_text1 = MarkupText("Li<sub>2</sub>S", font_size=36, font="IBM Plex Mono").shift(DOWN * 1)
        li2s_text2 = MarkupText("E<sup>o</sup>cell ~= 2.20 V", font_size=24, font="IBM Plex Mono").next_to(li2s_text1, DOWN, buff=0.2)
        li2s_group = Group(li1, li2, s)

        self.play(FadeIn(li1, li2, e1, e2, s))

        # Move Li, S, e-
        constants.bulk_play(self, [li1.animate().shift(RIGHT * 3.5),
                                   li2.animate().shift(RIGHT * 3.5),
                                   e1.animate().shift(RIGHT * 6),
                                   e2.animate().shift(RIGHT * 6),
                                   s.animate().shift(LEFT * 2)],
                            run_time=constants.ANIMATION_TIME)
        constants.bulk_play(self, [li2s_group.animate().rotate(PI / 2).move_to((0, 0, 0)),
                                   FadeOut(e1, e2)], run_time=constants.LONG_ANIMATION_TIME)

        # Add text
        constants.bulk_play(self, Create(li2s_text1), Create(li2s_text2))
        self.wait(constants.LONG_DWELL_TIME)

        # Explode everything
        left = Group(cell.anode, cell.anode_text)
        right = Group(cell.cathode, cell.cathode_text)
        down = Group(li2s_group, li2s_text1, li2s_text2)
        constants.bulk_play(self, [left.animate().shift(LEFT * 8),
                                   right.animate().shift(RIGHT * 8),
                                   cell.electrolyte.animate().shift(UP * 8),
                                   down.animate().shift(DOWN * 6)],
                            run_time=constants.LONG_ANIMATION_TIME)
        self.wait(constants.SHORT_DWELL_TIME)
