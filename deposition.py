from manim import *
from cell import Cell
import constants
import random


class Deposition(Scene):
    def construct(self):
        text = """The lithium atom travels away 
        to perform its duties
        #
        Lithium partly becomes lithium 
        sulfide as it discharges
        #
        Lithium sulfide binds to 
        part of the electrode
        #
        So, when discharging continues, lithium 
        only comes out of these pits
        #
        The surface of the electrode degrades 
        rapidly, decreasing cycle performance
        """
        text_objects = constants.text_generator(text, (RIGHT * 4.1 + DOWN * 2.5), font="IBM Plex Mono", font_size=24)

        # Pull constant scene
        cell = Cell()
        self.add(cell.cell_group)

        # Explode everything
        constants.bulk_play(self, [cell.anode.animate().move_to((0, 0, 0)),
                                   cell.cathode.animate().shift(RIGHT * 11),
                                   cell.electrolyte.animate().shift(RIGHT * 11),
                                   cell.anode_text.animate().shift(UP * 4),
                                   cell.cathode_text.animate().shift(RIGHT * 11)],
                            run_time=constants.LONG_ANIMATION_TIME)

        # Make Li atoms and text
        li = Circle(0.4, GRAY_C, fill_opacity=1)
        li_text = MarkupText("Li", font_size=24, font="IBM Plex Mono", color=BLACK).move_to(li.get_center())
        li_group = Group(li, li_text, z_index=1)

        li_arr = [[li_group.copy()
                .move_to((col * 0.95 - 6.5 + random.random() * 0.15,
                          row * 0.95 - 3.4 + random.random() * 0.15, 0))
                for row in range(8)]
            for col in range(8)]

        # Resize anode, put in the Li
        self.play(cell.anode.animate(run_time=constants.LONG_ANIMATION_TIME).set_height(8).set_width(10).move_to((-4, 0, 0)).set_opacity(1))
        # constants.bulk_play(self, [FadeIn(obj, shift=RIGHT, scale=1.2) for line in li_arr[:4] for obj in line], run_time=constants.SHORT_ANIMATION_TIME / 2)
        # constants.bulk_play(self, *[[FadeIn(obj, shift=RIGHT, scale=1.2) for obj in line] for line in li_arr[4:]], run_time=constants.FAST_ANIMATION_TIME)
        self.add(*[obj for line in li_arr for obj in line])

        # Add text
        self.play(Create(text_objects[0][0]), Create(text_objects[0][1]))
        print(text_objects[0][0].get_center())

        # Move around Li

        self.wait(constants.LONG_DWELL_TIME)
