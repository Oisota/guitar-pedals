"""Dual 250 Pedal (Gray Flannel)"""

from yattag import Doc

from .svg_template import SVGTemplate

HOLE_COLOR = '#555'
PRIMARY_COLOR = '#BC0'
LABEL_COLOR = 'black'
WIDTH = 85
HEIGHT = 111

class Dual250SVG(SVGTemplate):
    width = WIDTH
    height = HEIGHT
    border_color = PRIMARY_COLOR
    label_color = LABEL_COLOR
    background_color = '#6d6d6f'
    render_background = True

    style = """
        text{
            font-family: "Britannic", "Bauhaus 93", Arial, sans-serif;
        }
        """

    # enclosure drill holes
    hole_coords = [
        # x     y     r
        # knob holes
        (72, 45, 3.5),
        (72, 17, 3.5),
        (13, 45, 3.5),
        (13, 17, 3.5),
        # switch holes
        (53.5, 45, 3),
        (53, 17, 3),
        (33, 45, 3),
        (33, 17, 3),
        # footswitches/LEDS
        (34, 101, 4),
        (51, 101, 4),
        (16, 101, 6.5),
        (69, 101, 6.5),
    ]

    # control labels
    label_coords = [
        # Text    x     y
        # Knobs
        ('Gain', 13, 60),
        ('Gain', 72, 60),
        ('Volume', 13, 32),
        ('Volume', 72, 32),
        # switches
        ('SI', 33, 55),
        ('GE', 33, 37),
        ('NO', 42.5, 46),
        ('SI', 52.5, 55),
        ('LED', 53.5, 37),
        ('Mode', 42.5, 24),
    ]

    def body(self):
        doc, tag, text = Doc().tagtext()
        stag = doc.stag

        doc.asis(self.border())

        # in/out/power
        with tag('text', ('font-size', "4"), ('text-anchor', "middle"), x="42.5", y="6", fill=PRIMARY_COLOR):
            text('9V')

        stag('polygon', points="19,6 17,3 15,6", style=f"fill: {PRIMARY_COLOR};")
        stag('polygon', points="70,3 68,6, 66, 3", style=f"fill: {PRIMARY_COLOR};")

        # middle divider
        for y1, y2 in [(9, 19), (26, 41), (49, 67), (83, 108)]:
            stag('line', x1="42.5", y1=y1, x2="42.5", y2=y2, stroke=PRIMARY_COLOR)

        # logo
        with tag('mask', id='m'):
            stag('rect', x='8', y='69', width='69', height='12', fill='white')
            with tag('text', ('font-size', '10'), ('text-anchor', 'middle'), fill='black', x='42.5', y='78'):
                text('Gray Flannel')

        stag('rect', x='8', y='69', width='69', height='12', fill=PRIMARY_COLOR, mask='url(#m)')
        stag('line', x1='3', y1='67', x2='82', y2='67', stroke=PRIMARY_COLOR)
        stag('line', x1='3', y1='83', x2='82', y2='83', stroke=PRIMARY_COLOR)

        return doc.getvalue()