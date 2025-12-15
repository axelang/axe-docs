hljs.registerLanguage("axe", function (hljs) {
  return {
    name: "Axe",
    keywords: {
      keyword:
        "if when is elif else for in switch case default parallel single loop break continue return while test assert use platform and or to mod enum union unsafe opaque extern foreign pub def val mut model macro raw overload list put",
      literal: "true false nil",
      type:
        "u8 i8 u16 i16 u32 i32 u64 i64 f32 f64 bool char void usize generic untyped",
    },
    contains: [
      hljs.C_LINE_COMMENT_MODE,
      hljs.C_BLOCK_COMMENT_MODE,

      {
        className: "string",
        variants: [
          hljs.QUOTE_STRING_MODE,
          hljs.APOS_STRING_MODE,
          { begin: "`", end: "`" },
        ],
      },

      {
        className: "number",
        variants: [
          { begin: /\b\d+\.\d+([eE][+-]?\d+)?\b/ },
          { begin: /\b\d+\b/ },
        ],
      },

      {
        className: "constant",
        begin: /\b[A-Z_][A-Z0-9_]*\b/,
      },

      {
        className: "function",
        begin: /\b(def|macro)\s+[a-zA-Z_][a-zA-Z0-9_]*/,
        keywords: "def macro",
      },

      {
        className: "function",
        begin: /\b[a-z_][a-zA-Z0-9_]*\s*(?=\()/,
      },

      {
        className: "operator",
        begin: /==|!=|<=|>=|<|>|\+|\-|\*|\/|%|=/,
      },

      {
        className: "keyword",
        begin: /\b(ref|ref_of|addr_of|cast)\b/,
      },

      {
        className: "meta",
        begin: /\braw\s*\{/,
        end: /\}/,
        contains: [hljs.C_LINE_COMMENT_MODE, hljs.C_BLOCK_COMMENT_MODE],
      },

      {
        className: "type",
        begin: /\b[A-Z][a-zA-Z0-9_]*\b/,
      },
    ],
  };
});
