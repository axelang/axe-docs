from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import (
    Text,
    Comment,
    String,
    Number,
    Keyword,
    Name,
    Operator,
    Punctuation,
)

class AxeLexer(RegexLexer):
    name = "Axe"
    aliases = ["axe"]
    filenames = ["*.axe"]
    mimetypes = ["text/x-axe"]

    flags = 0

    tokens = {
        "root": [
            (r"\s+", Text),
            (r"//.*?$", Comment.Single),
            (r"/\*", Comment.Multiline, "comment"),

            (
                r"\b(raw)(\s*)(\{)",
                bygroups(Keyword, Text, Punctuation),
                "raw-block",
            ),

            (r"`", String.Backtick, "string-backtick"),
            (r'"', String.Double, "string-double"),
            (r"'", String.Single, "string-single"),

            (r"\b\d+\.\d+([eE][+-]?\d+)?\b", Number.Float),
            (r"\b\d+\b", Number.Integer),

            (
                r"\b(if|when|is|elif|else|for|in|switch|case|default|parallel|single|loop|break|continue|return|while|test|assert|use|platform|to|mod|enum|union|unsafe|opaque|extern|foreign)\b",
                Keyword.Control,
            ),

            (r"\b(and|or)\b", Operator.Word),

            (
                r"\b(pub|def|val|mut|model|macro|raw|overload|list|put)\b",
                Keyword,
            ),

            (r"\b(ref|ref_of|addr_of|cast)\b", Keyword.Declaration),

            (
                r"\b(u8|i8|u16|i16|u32|i32|u64|i64|f32|f64|bool|char|void|usize|generic|untyped)\b",
                Keyword.Type,
            ),

            (r"\bchar\*\b", Keyword.Type),

            (r"\b[A-Z][a-zA-Z0-9_]*\b", Name.Class),

            (r"\b[A-Z_][A-Z0-9_]*\b", Name.Constant),

            (r"\b(true|false)\b", Keyword.Constant),
            (r"\bnil\b", Keyword.Constant),

            (
                r"\b(def|macro)\s+([a-zA-Z_][a-zA-Z0-9_]*)",
                bygroups(Keyword, Name.Function),
            ),

            (
                r"\b([a-z_][a-zA-Z0-9_]*)(\s*)(\()",
                bygroups(Name.Function, Text, Punctuation),
            ),

            (r"==|!=|<=|>=|<|>", Operator),
            (r"[+\-*/%]", Operator),
            (r"=", Operator),
            (r"[{}\[\]();,\.]", Punctuation),
            (r"[a-z_][a-zA-Z0-9_]*", Name),
        ],


        "comment": [
            (r"\*/", Comment.Multiline, "#pop"),
            (r".|\n", Comment.Multiline),
        ],

        "string-single": [
            (r"\\.", String.Escape),
            (r"'", String.Single, "#pop"),
            (r".|\n", String.Single),
        ],

        "string-double": [
            (r"\\.", String.Escape),
            (r'"', String.Double, "#pop"),
            (r".|\n", String.Double),
        ],

        "string-backtick": [
            (r"\\.", String.Escape),
            (r"`", String.Backtick, "#pop"),
            (r".|\n", String.Backtick),
        ],

        "raw-block": [
            (r"\}", Punctuation, "#pop"),
            (r".|\n", Text),
        ],
    }
