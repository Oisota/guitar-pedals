"""Double Muff Clone"""

from yattag import Doc

from .svg_template import SVGTemplate

PRIMARY_COLOR = 'black'

class DOD250SVG(SVGTemplate):
    width = 58
    height = 110
    border_color = 'black'
    label_color = 'black'
    label_size = '4'
    background_color = '#BBAA00'
    render_background = True

    style = """
        text {
            font-family: "Britannic", "Bauhaus 93", Arial, sans-serif;
        }
        """

    # enclosure drill holes
    hole_coords = [
        # x     y     r
        # knob holes
        (43, 18, 3.5),
        (15, 18, 3.5),
        # switch holes
        (29, 39, 3),
        # footswitches/LEDS
        (29, 80, 3.5),
        (29, 100, 6),
    ]

    # control labels
    label_coords = [
        # Text    x     y
        # Knobs
        ('Gain', 43, 36),
        ('Volume', 15, 36),
        # switches
        ('Mode', 29, 48),
    ]

    def body(self):
        doc, tag, text = Doc().tagtext()
        stag = doc.stag

        doc.asis(self.border())

        # logo
        with tag('text', ('font-size', '4'), fill='black', x='4', y='54'):
            text('DOM')
        with tag('text', ('font-size', '7'), fill='black', x='4', y='61'):
            text('Overdrive')
        with tag('text', ('font-size', '7'), fill='black', x='4', y='68'):
            text('Preamp')
        with tag('text', ('font-size', '7'), fill='black', x='41', y='68'):
            text('250')

        # desgin
        stag('line', x1="5", y1="70", x2="5", y2="109", stroke="black")
        stag('line', x1="9", y1="74", x2="9", y2="109", stroke="black")
        stag('line', x1="13", y1="78", x2="13", y2="109", stroke="black")
        stag('line', x1="17", y1="82", x2="17", y2="109", stroke="black")
        stag('line', x1="21", y1="86", x2="21", y2="109", stroke="black")
        stag('line', x1="25", y1="90", x2="25", y2="109", stroke="black")
        stag('line', x1="29", y1="82", x2="29", y2="109", stroke="black")
        stag('line', x1="33", y1="90", x2="33", y2="109", stroke="black")
        stag('line', x1="37", y1="86", x2="37", y2="109", stroke="black")
        stag('line', x1="41", y1="82", x2="41", y2="109", stroke="black")
        stag('line', x1="45", y1="78", x2="45", y2="109", stroke="black")
        stag('line', x1="49", y1="74", x2="49", y2="109", stroke="black")
        stag('line', x1="53", y1="70", x2="53", y2="109", stroke="black")

        return doc.getvalue()