from pygments.lexers import _mapping
from axe_lexer import AxeLexer


def on_pre_build(config):
    lexer = AxeLexer()

    _mapping.LEXERS["Axe"] = (
        "axe_lexer",
        lexer.name,
        tuple(lexer.aliases),
        tuple(lexer.filenames),
        (),
    )
