from manim import *
import constants


class Particle(Scene):
    def construct(self):
        metal = Rectangle(GRAY_A, 3, 1, fill_opacity=6)
        metal_text = MarkupText("Li<sub>(s)</sub>", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(metal.get_center()).shift(UP)
        metal_group = Group(metal, metal_text)

        li = Circle(0.5, GRAY_C, fill_opacity=1)
        li_text = MarkupText("Li", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(li.get_center())
        li_group = Group(li, li_text).scale(0.001)
        li_group2 = li_group.copy()

        s = Circle(0.5, YELLOW_B, fill_opacity=1)
        s_text = MarkupText("S", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(s.get_center())
        s_group = Group(s, s_text).shift(DOWN * 5)
        li2s_group = Group(li_group, li_group2, s_group)
        li2s_text = MarkupText("2Li + S → Li<sub>2</sub>S", font_size=24, font="IBM Plex Mono", color=WHITE).shift(DOWN * 0.5)

        constants.bulk_play(self, Create(metal), Create(metal_text), run_time=constants.SHORT_ANIMATION_TIME)
        self.add(li, li_text)

        self.wait(constants.SHORT_DWELL_TIME)

        constants.bulk_play(self, [metal_group.animate().scale(14.2),
                                   li_group.animate().scale(1000).shift(LEFT),
                                   li_group2.animate().scale(1000).shift(RIGHT)],
                            run_time=constants.LONG_ANIMATION_TIME * 3)
        self.wait(constants.SHORT_DWELL_TIME)

        self.play(metal_group.animate(run_time=constants.LONG_ANIMATION_TIME).shift(LEFT * 15))
        constants.bulk_play(self, [li_group.animate().shift(RIGHT * 0.33),
                                   li_group2.animate().shift(LEFT * 0.33),
                                   s_group.animate().shift(UP * 4.2)],
                                   run_time=constants.LONG_ANIMATION_TIME)
        self.play(Write(li2s_text))

        self.wait(constants.SHORT_DWELL_TIME)

        self.play(li2s_group.animate(run_time=constants.SHORT_ANIMATION_TIME).shift(LEFT * 1))

        self.wait(constants.LONG_DWELL_TIME)
