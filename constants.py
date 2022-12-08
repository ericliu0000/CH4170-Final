from manim import *

# Text configuration constants
TEXT_COLOR = "#ffffff"
TOP_TEXT_BUFFER = 0.5
BETWEEN_TEXT_BUFFER = 0.15

# Animation time scale constants
FAST_ANIMATION_TIME = 0.2
SHORT_ANIMATION_TIME = 0.5
ANIMATION_TIME = 0.8
LONG_ANIMATION_TIME = 1.5
SHORT_DWELL_TIME = 1
LONG_DWELL_TIME = 2.5

# Plus and minus sign scale factors
PLUS_SCALE = 0.5
MINUS_SCALE = 0.12

# Graph edge and vertex indication constants
INDICATE_COLOR = YELLOW
INDICATE_SCALE_FACTOR = 1.5

# Power level label constants
PL_CIRCLE_SIZE = 0.18
PL_FONT_SIZE = 22

# Vocabulary color constants
POSITIVE_TRIANGLE_COLOR = "foreground=\"green\""
GRAPH_COLOR = "foreground=\"red\""
SINGLE_UNDERLINE = "underline=\"single\" underline_color=\"yellow\""
DOUBLE_UNDERLINE = "underline=\"double\" underline_color=\"red\""
POWER_LEVEL_GRADIENT = "from=\"GREEN\" to=\"BLUE\""
ONE_COMPLETE_GRADIENT = "from=\"YELLOW_C\" to=\"RED\""
VERTEXIFIED_GRADIENT = "from=\"TEAL_E\" to=\"PURE_BLUE\""
MEMBERS_GRADIENT = "from=\"PINK\" to=\"GOLD_E\""


# Utility
def text_generator(text, ref, **kwargs):
    lines = text.split("\n")
    groups = []

    temp = []
    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            groups.append(temp)
            temp = []
        else:
            obj = MarkupText(line, **kwargs, color=TEXT_COLOR)

            if len(temp) == 0:
                obj.move_to(ref)
            else:
                obj.next_to(temp[-1], DOWN, buff=BETWEEN_TEXT_BUFFER)

            temp.append(obj)

    groups.append(temp)
    return groups


def bulk_play(self, *args, **kwargs):
    for arg in args:
        if type(arg) == list:
            self.play(*arg, **kwargs)
        else:
            self.play(arg, **kwargs)
