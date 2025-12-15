Generic functions in Axe can be defined using type parameters, for example:

```axe
def some_function[T](arg: T): T {
    when T is float {
        return arg * 2.0;
    }
    when T is i32 {
        return arg + 1;
    }
    return arg;
}
```

In this case, if the callsite is `some_function(2);`, it will return the value plus one, otherwise, if it is a float, it will double the value, if the value is neither a float or a 32-bit integer, it will simply return the value as-is.

Generic `when`/`is` clauses can also be utilized in nested contexts. 

In the following example, the `list_contains` function will work both for integer lists and string lists:

```axe
def list_contains[T, T2](lst: T, value: T2): bool {
    for mut i = 0; i < lst.len; i++ {
        when T2 is i32 and T is IntList {
            if lst.data[i] == cast[i32](value) {
                return true;
            }
        } 
        when T2 is string and T is StringList {
            if compare(lst.data[i], cast[string](value)) == 0 {
                return true;
            }
        }
    }
    return false;
}
```

You will recall from earlier, in the standard library documentation, that the `IntList` and `StringList` types are specialized structures wrapping arrays of integers and strings, respectively. The `cast` operator allows safe conversion of a generic value to a concrete type when a type match is guaranteed by the `when` clause. This ensures that generic functions can operate on multiple types while maintaining type safety and avoiding unnecessary runtime checks.

Generic functions in Axe can also return different types depending on conditions. Consider the following example:

```axe
def maybe_double[T](arg: T): T {
    when T is float {
        return arg * 2.0;
    }
    when T is i32 {
        return arg * 2;
    }
    return arg;
}
```

Here, `maybe_double` will automatically infer the return type from the input type `T`, and the behavior changes accordingly. This pattern is particularly useful in numeric computations or algorithms where the same logic should apply to multiple numeric types.

Another powerful feature is that generic functions can call other generic functions with inferred type parameters. For example:

```axe
def add_or_concat[T](a: T, b: T): T {
    when T is i32 or T is float {
        return a + b;
    }
    when T is string {
        return a + b;
    }
    return a; // fallback for unsupported types
}

def process_values[T](x: T, y: T): T {
    return add_or_concat(x, y);
}
```

In this example, `process_values` does not need to know the exact type of `x` and `y`. The call to `add_or_concat` will automatically select the correct `when` clause based on the concrete type provided at the callsite.
