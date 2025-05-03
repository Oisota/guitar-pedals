"""Double Muff Clone"""

from yattag import Doc

from .svg_template import SVGTemplate

PRIMARY_COLOR = 'black'

class DoubleMuffSVG(SVGTemplate):
    width = 60
    height = 115
    border_color = 'black'
    label_color = 'black'
    label_size = '5'
    background_color = '#666666'
    render_background = True

    style = """
        text{
            font-family: "Bauhaus 93", Arial, sans-serif;
        }
        """

    # enclosure drill holes
    hole_coords = [
        # x     y     r
        # knob holes
        (44, 27, 4),
        (13, 27, 4),
        # switch holes
        (30, 50, 3),
        # footswitches/LEDS
        (30, 104, 7),
        (12, 104, 4),
    ]

    # control labels
    label_coords = [
        # Text    x     y
        # Knobs
        ('muff 1', 44, 11),
        ('muff 2', 13, 11),
        # switches
        ('single', 42, 54),
        ('double', 42, 48),
    ]

    def body(self):
        doc, tag, text = Doc().tagtext()
        stag = doc.stag

        doc.asis(self.border())

        # in/out/power
        with tag('text', ('font-size', "4"), ('text-anchor', "middle"), x="30", y="5", fill=PRIMARY_COLOR):
            text('9V')

        stag('polygon', points="15,5 13,2 11,5", style=f"fill: {PRIMARY_COLOR};")
        stag('polygon', points="49,2 47,5, 45, 2", style=f"fill: {PRIMARY_COLOR};")

        # logo
        stag('rect', ('stroke-width', 1), x='1.5', y='64', width='57', height='25', fill='#222222')
        with tag('text', ('font-size', '5'), ('text-anchor', 'middle'), fill='white', x='22', y='71'):
            text('Double')

        with tag('text', ('font-size', '16'), ('text-anchor', 'middle'), ('font-weight', 'bold'), fill='#A02020', x='30', y='84'):
            text('Muff')

        return doc.getvalue()