"""Generic SVG Template Class"""

from abc import ABC, abstractmethod

from yattag import Doc

class SVGTemplate(ABC):
    width = ''
    height = ''
    border_color = ''
    label_color = ''
    background_color = ''
    render_background = False
    hold_coords = []
    label_coords = []
    label_size = '4'
    style = ''

    def build(self) -> str:
        ctx = Doc()
        doc, tag, text = ctx.tagtext()
        stag = doc.stag

        with tag('svg',
            version='1.1',
            width=str(self.width),
            height=str(self.height),
            xmlns='http://www.w3.org/2000/svg'):

            with tag('style'):
                doc.asis(f"<![CDATA[ {self.style} ]]>")

            # background
            if self.render_background:
                stag('rect', width='100%', height='100%', fill=self.background_color)

            # render drill holes
            for x, y, r in self.hole_coords:
                doc.asis(self.hole(x=x, y=y, r=r))

            # render labels
            for label_text, x, y in self.label_coords:
                doc.asis(self.label(label_text, x, y))

            doc.asis(self.body()) # can have multiple 'blocks' that can be overwritten in child templates

        return doc.getvalue()

    @abstractmethod
    def body(self) -> str: # override this in child class
        """Generate the body of the SVG"""

    # convenience methods

    def hole(self, x, y, r) -> str:
        """Render circle indicating enclosure drill hole"""
        doc, _, _ = Doc().tagtext()
        doc.stag('circle', ('stroke', 'black'), ('stroke-width', '0.5'), cx=x, cy=y, r=r, fill='transparent')
        # draw cross to indicate center of hole
        doc.stag('line', ('stroke-width', '0.5'), x1=(x-r), y1=y, x2=(x+r), y2=y, stroke='black')
        doc.stag('line', ('stroke-width', '0.5'), x1=x, y1=(y-r), x2=x, y2=(y+r), stroke='black')
        return doc.getvalue()


    def label(self, label_text, x, y) -> str:
        """Render text label"""
        doc, tag, text = Doc().tagtext()
        with tag('text', ('font-size', self.label_size), ('text-anchor', 'middle'), x=x, y=y, fill=self.label_color):
            text(label_text)
        return doc.getvalue()


    def border(self) -> str:
        """Generic border function"""
        inset = 1
        b_width = self.width - (inset * 2)
        b_height = self.height - (inset *2)
        doc, _, _ = Doc().tagtext()
        stag = doc.stag
        stag('rect',
            ('stroke-width', "1"),
            x=str(inset),
            y=str(inset),
            rx="3",
            ry="3",
            width=str(b_width),
            height=str(b_height),
            stroke=self.border_color,
            fill="transparent"
            )
        return doc.getvalue()