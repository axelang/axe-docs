Axe is a system programming language that aims to be simple and easy to learn, while still being powerful and efficient.

It aims to be a language that can be used for both system programming and application development, moreover, the language is intentionally minimal to avoid bloat and unnecessary complexity.

To provide a quick overview of the language, here is the simple hello world program:

```axe
use std.io;

def main() {
    println "Hello, world";
}
```

To compile and run the program, save it as `hello.axe` and use the following command in the same directory as the saved file:

```bash
axe hello
```

This will generate an executable, that can then be run with either `./hello` or `hello.exe` depending on the platform.

If for example you want to take commandline arguments and greet whoever passed it, you can do the following:

```axe
use std.os;
use std.io;

def main() {
    println $"Hello, {get_cmdline_args()[1]}";
}
```

Bounds checking in cases like this is the responsibility of the user. And here it can be done through use of the `len` builtin.
For example:

```axe
def main() {
    val args: StringList = get_cmdline_args();
    if len(args) > 1 {
        println $"Hello, {args[1]}";
    }
}
```