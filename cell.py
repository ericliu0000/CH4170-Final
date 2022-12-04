from manim import *
import constants

class Cell(Scene):
    def __init__(self):
        super().__init__()
        self.anode = Rectangle(GRAY_B, 6, 2, fill_opacity=0.7).move_to((-4, 0, 0))
        self.cathode = Rectangle(GOLD_E, 6, 2, fill_opacity=0.7).move_to((4, 0, 0))
        self.electrolyte = Rectangle(BLUE, 7, 6, fill_opacity=0.5)

        self.anode_text = MarkupText("Anode", font_size=20, font="IBM Plex Mono").move_to(self.anode.get_center()).shift(UP * 3.25)
        self.cathode_text = MarkupText("Cathode", font_size=20, font="IBM Plex Mono").move_to(self.cathode.get_center()).shift(UP * 3.25)

        self.cell_group = Group(self.anode, self.cathode, self.electrolyte, self.anode_text, self.cathode_text)

    def construct(self):
        self.__init__()
        constants.bulk_play(self, Create(self.anode), Create(self.cathode), Create(self.electrolyte), run_time=constants.SHORT_ANIMATION_TIME)
        constants.bulk_play(self, [Create(self.anode_text), Create(self.cathode_text)], run_time=constants.SHORT_ANIMATION_TIME)
        self.wait(constants.LONG_DWELL_TIME)

