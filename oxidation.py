from manim import *
from cell import Cell
import constants


class Oxidation(Scene):
    def construct(self):
        # Pull constant scene
        cell = Cell()
        self.add(cell.cell_group)

        # Explode everything
        constants.bulk_play(self, [cell.anode.animate().move_to((0, 0, 0)),
                                   cell.cathode.animate().shift(RIGHT * 11),
                                   cell.electrolyte.animate().shift(RIGHT * 11),
                                   cell.anode_text.animate().shift(UP * 4),
                                   cell.cathode_text.animate().shift(RIGHT * 11)],
                            run_time=constants.LONG_ANIMATION_TIME * 2)

        # Resize anode to (3, 1)
        self.play(cell.anode.animate().set_height(3).set_width(1))

        # Make metal anode, particle, and text objects
        electrode = Rectangle(GRAY_A, 3, 1, fill_opacity=6)
        electrode_text = MarkupText("Li<sub>(s)</sub>", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(electrode.get_center()).shift(UP)
        electrode_group = Group(electrode, electrode_text)

        li = Circle(0.5, GRAY_C, fill_opacity=1)
        li_text = MarkupText("Li", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(li.get_center())
        li_text2 = MarkupText("Li<sup>+</sup>", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(li.get_center())
        li_group = Group(li, li_text, z_index=1).scale(0.001)

        e = Circle(0.25, BLUE_B, fill_opacity=1)
        e_text = MarkupText("e<sup>-</sup>", font_size=16, font="IBM Plex Mono", color=BLACK).move_to(e.get_center())
        e_group = Group(e, e_text)
        e_group2 = e_group.copy()

        ox_text = MarkupText("Oxidation", font_size=36, font="IBM Plex Mono", color=WHITE).shift(UP * 2)
        ox_rxn = MarkupText("2Li → 2Li<sup>+</sup> + 2e<sup>-</sup>", font_size=36, font="IBM Plex Mono", color=WHITE).shift(DOWN * 2)

        # Transform anode to metal
        self.play(Transform(cell.anode, electrode), Create(electrode_text))
        self.wait(constants.SHORT_DWELL_TIME)
        self.remove(cell.cell_group)

        # Zoom in both
        constants.bulk_play(self, [electrode_group.animate().scale(14.2),
                                   li_group.animate().scale(1000)],
                            run_time=constants.LONG_ANIMATION_TIME)
        self.play(electrode_group.animate(run_time=constants.ANIMATION_TIME,
                                      rate_func=rate_functions.ease_in_sine)
                  .shift(LEFT * 5))

        # Create electron, seperate from Li
        self.add(e, e_text)
        constants.bulk_play(self, [e_group.animate(run_time=constants.SHORT_ANIMATION_TIME).shift(UP),
                                   ReplacementTransform(li_text, li_text2),
                                   electrode_group.animate(rate_func=rate_functions.ease_out_sine).shift(LEFT * 10)],
                            run_time=constants.LONG_ANIMATION_TIME)

        self.wait(constants.SHORT_DWELL_TIME)
        li_group2 = li_group.copy()
        constants.bulk_play(self, [li_group.animate().shift(LEFT + DOWN * 0.25),
                                   li_group2.animate().shift(RIGHT + DOWN * 0.25),
                                   e_group.animate().shift(LEFT + DOWN * 0.25),
                                   e_group2.animate().shift(RIGHT + UP * 0.75)],
                            run_time=constants.SHORT_ANIMATION_TIME)

        self.play(Create(ox_text), Create(ox_rxn))
        self.wait(constants.LONG_DWELL_TIME)

        # Group everything and move it away, bring back the cell
        all_group = Group(li_group, li_group2, e_group, e_group2, ox_text, ox_rxn)
        conclusion_cell = Cell().cell_group.shift(RIGHT * 15)
        constants.bulk_play(self, [all_group.animate().shift(LEFT * 15),
                                      conclusion_cell.animate().shift(LEFT * 15)],
                            run_time=constants.LONG_ANIMATION_TIME * 2)

        self.wait(constants.SHORT_DWELL_TIME / 4)
