from manim import *
from cell import Cell
import constants


class Reduction(Scene):
    def construct(self):
        # Pull constant scene
        cell = Cell()
        self.add(cell.cell_group)

        # Explode everything
        constants.bulk_play(self, [cell.anode.animate().shift(LEFT * 11),
                                   cell.cathode.animate().move_to((0, 0, 0)),
                                   cell.electrolyte.animate().shift(LEFT * 11),
                                   cell.anode_text.animate().shift(LEFT * 11),
                                   cell.cathode_text.animate().shift(UP * 4)],
                            run_time=constants.LONG_ANIMATION_TIME * 2)

        # Resize cathode to (3, 1)
        self.play(cell.cathode.animate().set_height(3).set_width(1))

        # Make metal cathode, particle, and text objects
        electrode = Rectangle(GOLD_E, 3, 1, fill_opacity=6)
        electrode_text = MarkupText("C/S", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(electrode.get_center()).shift(UP)
        electrode_group = Group(electrode, electrode_text)

        s = Circle(0.5, YELLOW_A, fill_opacity=1)
        s_text = MarkupText("S", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(s.get_center())
        s_text2 = MarkupText("S<sup>2-</sup>", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(s.get_center())
        s_group = Group(s, s_text, z_index=1).scale(0.001)

        e = Circle(0.25, BLUE_B, fill_opacity=1)
        e_text = MarkupText("e<sup>-</sup>", font_size=16, font="IBM Plex Mono", color=BLACK).move_to(e.get_center())
        e_group = Group(e, e_text)
        e_group2 = e_group.copy()
        e_group, e_group2 = e_group.shift(UP + LEFT), e_group2.shift(UP + RIGHT)

        red_rxn = MarkupText("S + 2e<sup>-</sup> → S<sup>2-</sup>", font_size=36, font="IBM Plex Mono", color=WHITE).shift(DOWN * 2)

        # Transform cathode to metal
        self.play(Transform(cell.cathode, electrode), Create(electrode_text))
        self.wait(constants.SHORT_DWELL_TIME)
        self.remove(cell.cell_group)

        # Zoom in both
        constants.bulk_play(self, [electrode_group.animate().scale(14.2),
                                   s_group.animate().scale(1000),
                                   FadeIn(e_group, e_group2)],
                            run_time=constants.LONG_ANIMATION_TIME)
        self.play(electrode_group.animate(run_time=constants.ANIMATION_TIME,
                                      rate_func=rate_functions.ease_in_sine)
                  .shift(RIGHT * 5))

        # Create electron, seperate from Li
        self.add(e, e_text)
        constants.bulk_play(self, [e_group.animate(run_time=constants.SHORT_ANIMATION_TIME).shift(DOWN + RIGHT), 
                                    e_group2.animate(run_time=constants.SHORT_ANIMATION_TIME).shift(DOWN + LEFT),
                                   ReplacementTransform(s_text, s_text2),
                                   electrode_group.animate(rate_func=rate_functions.ease_out_sine).shift(RIGHT * 10)],
                            run_time=constants.LONG_ANIMATION_TIME)
        
        self.remove(e_group, e_group2)
        self.play(Create(red_rxn))
        self.wait(constants.LONG_DWELL_TIME)

        # Group everything and move it away, bring back the cell
        all_group = Group(s_group, red_rxn)
        conclusion_cell = Cell().cell_group.shift(LEFT * 15)
        constants.bulk_play(self, [all_group.animate().shift(RIGHT * 15),
                                      conclusion_cell.animate().shift(RIGHT * 15)],
                            run_time=constants.LONG_ANIMATION_TIME * 2)

        self.wait(constants.SHORT_DWELL_TIME)
