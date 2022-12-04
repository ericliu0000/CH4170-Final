from manim import *

# Text configuration constants
TEXT_COLOR = "#edcaeb"
TOP_TEXT_BUFFER = 0.5
BETWEEN_TEXT_BUFFER = 0.25

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
def text_generator(text, ref):
    lines = text.split("\n")
    groups = []

    temp = []
    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            groups.append(temp)
            temp = []
        else:
            obj = MarkupText(line, color=TEXT_COLOR)

            if len(temp) == 0:
                obj.next_to(ref, DOWN, buff=TOP_TEXT_BUFFER)
            else:
                obj.next_to(temp[-1], DOWN, buff=BETWEEN_TEXT_BUFFER)

            temp.append(obj)

    groups.append(temp)

    return groups


def bulk_play(self, *args, **kwargs):
    for arg in args:
        if type(arg) == list:
            self.play(*arg)
        else:
            self.play(arg, **kwargs)


def bulk_indicate(self, graph, edges, color=INDICATE_COLOR, include_vertices=True, **kwargs):
    actions = []

    # Get vertices from unique parts of edges
    vertices = list(set([edge[0] for edge in edges] + [edge[1] for edge in edges]))

    for edge in edges:
        actions.append(Indicate(graph.edges[edge], color=color, scale_factor=INDICATE_SCALE_FACTOR, **kwargs))

    if include_vertices:
        for vertex in vertices:
            actions.append(Indicate(graph.vertices[vertex], color=color, scale_factor=INDICATE_SCALE_FACTOR, **kwargs))

    bulk_play(self, actions)


def bulk_indicate_vertices(self, graph, vertices, color=INDICATE_COLOR, **kwargs):
    actions = []

    for vertex in vertices:
        actions.append(Indicate(graph.vertices[vertex], color=color, scale_factor=INDICATE_SCALE_FACTOR, **kwargs))

    bulk_play(self, actions)


def recolor(self, graph, edges, color):
    actions = []

    for edge in edges:
        actions.append(graph.edges[edge].animate(run_time=SHORT_ANIMATION_TIME).set_color(color))

    bulk_play(self, actions)