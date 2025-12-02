Error handling in Axe is explicit through use of error unions from returns. It is similar to Go in this regard in that there is no try/catch construct.

Creating an error can be done through use of the `std.errors` module.

```axe
use std.errors;
use std.io;

def main() {
    panic(error.create("This is some runtime error."));
    println "Will never print...";
}
```

In this case we create an error through use of the create static function on the error type. The `panic` function is used to stop the program in the case of a fatal error. Though generally it is preferred to set the return type of your function to an error union, such that error propagation is made possible. For example:

```axe
model SomeFunctionResult {
    result: union {
        err: error;
        result: string;
    }
}

pub def some_function(): SomeFunctionResult {
    
}
```