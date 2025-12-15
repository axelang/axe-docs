Overloads allow for variant behaviour based on the argument types. A common example is the `println` overload from Axe's own standard library:

```
overload println(x: generic) {
    string => print_str;
    i32    => println_i32;
    char   => println_char;
    f32    => println_f32;
    f64    => println_f64;
    i64    => println_i64;
    bool   => println_bool;
}(x);
```

This essentially maps the argument types to the functions that handle them. Each case specifies the exact type of the argument and the corresponding function that will be called.

## Comparison with Generic Functions

Generally, it is preferred to use generic functions over overloads because of:

* Maintainability: Generics often reduce duplication by allowing a single implementation to work with multiple types.
* Readability: Overloads can become verbose and harder to track, especially when many argument types are supported.
* Extensibility: Adding new types to an overload requires modifying the overload itself, while generic constraints can often handle new types automatically.

However, overloads are still useful when different argument types require entirely distinct logic that cannot be captured by generics, you want explicit control over which function is called for a particular type, or performance optimization is needed for specific types.

## Syntax

The typical structure of an overload is:

```axe
overload function_name(argument: type) {
    type_1 => handler_1;
    type_2 => handler_2;
    ...
}(argument);
```

* Each `type => handler` mapping defines which implementation is used for which argument type.
* The final `(argument)` applies the overload to the provided value.

## Caveats

* Overloads are resolved at **compile-time**, not runtime. The compiler selects the appropriate implementation based on the static type of the argument.
* Ambiguous overloads (e.g., two handlers for the same type) can result in compilation errors.
* Overuse of overloads can lead to code that is harder to maintain and extend compared to using generics.
