from mkdocs.plugins import BasePlugin
from pygments.lexers import _mapping
from axe_lexer import AxeLexer


class AxePygmentsPlugin(BasePlugin):
    def on_pre_build(self, config):
        lexer = AxeLexer()

        _mapping.LEXERS["Axe"] = (
            "axe_lexer",
            lexer.name,
            tuple(lexer.aliases),
            tuple(lexer.filenames),
            ()
        )
