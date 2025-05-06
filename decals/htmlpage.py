from abc import ABC, abstractmethod

from yattag import Doc

class HtmlPage:
    """HTML Page Template"""

    title = ''

    def build(self) -> str:
        doc, tag, text = Doc().tagtext()
        stag = doc.stag

        doc.asis('<!DOCTYPE HTML>')

        with tag('html'):
            with tag('head'):
                stag('meta', charset="utf-8")
                stag('meta', name="viewport", content="width=device-width, initial-scale=1")
                stag('meta', name="description", content="")
                with tag('title'):
                    text(self.title)

            with tag('body'):
                doc.asis(self.body())

    @abstractmethod
    def body(self) -> str:
        """Body template slot"""