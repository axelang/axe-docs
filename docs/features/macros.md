Macros are defined through use of the `macro` keyword, for example:

```axe
macro some_macro(x: untyped, y: untyped) {
    x + y;
}

def main() {
    println(some_macro(1, 2));
}
```

In this case the result (3) would be printed to the standard output stream.

The heavy use of macros is generally not advisable, as it can lead to readability issues. Macros operate on the syntax tree rather than on evaluated values, which allows them to generate code dynamically, but also makes debugging more difficult because the code you write is not always the code that executes.

Macros can accept untyped parameters, which gives them flexibility to manipulate different kinds of expressions.