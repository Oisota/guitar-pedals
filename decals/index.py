from yattag import Doc

from .htmlpage import HtmlPage

class IndexPage(HtmlPage):
    title = 'Decals Woot'
    
    def body(self):
        doc, tag, text = Doc().tagtext()
        stag = doc.stag

        with tag('div', style='display: flex; justify-content: center;'):
            stag('img', src='./dod250.svg', alt="dod250", style='padding: 2rem; width: 58mm; height: 110mm')
            stag('img', src='./doublemuff.svg', alt="doublemuff", style='padding: 2rem; width: 62mm; height: 118mm')

        with tag('div', style='display: flex; justify-content: center;'):
            stag('img', src='./dual250.svg', alt="dual250", style='padding: 2rem; width: 88mm; height: 115mm')

        return doc.getvalue()