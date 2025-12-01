Macros are defined through use of the `macro` keyword, for example:

```axe
macro some_macro(x: untyped, y: untyped) {
    x + y;
}

def main() {
    println some_macro(1, 2);
}
```

In this case the result (3) would be printed to the standard output stream.

The heavy use of macros is generally not advisable, as it can lead to readability issues. Currently it is a stand-in for writing generic code prior to the introduction of true generics into the programming language (beyond the `overload` construct that is already present for variant behavior based on argument types).

