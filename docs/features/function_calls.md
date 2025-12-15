It is of note that function calls have syntactic sugar that allows you to, if the argument count is exactly 1 and it is a simple literal, for example a `ref char` of value "hello", or an `i32` of value 20, omit the parenthesis.

This can be done like so, using the `println` overload from `std.io` as an example:

```
use std.io;

def main() {
    println "Hello, world.";
}
```

Notice how the parenthesis are not there. However, the compile will error if you try to have a complex expression in combination with this syntactic sugar, this is a purposeful design choice to prevent unreadable code.

Moreover, we can omit the empty parenthesis from function calls altogether if the function does not accept any arguments. Therefore, this is perfectly valid Axe code:

```
use std.io;

def main {
    println "Hi, world.";
}
```