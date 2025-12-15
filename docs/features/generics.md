Generic functions in Axe can be defined using type parameters, allowing a single function body to express behaviour that adapts to multiple concrete types. A simple example would look like this:

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

Here, the function’s logic is specialized at compile time based on the concrete type bound to `T`. If the callsite is `some_function(2);`, the compiler resolves `T` as `i32` and selects the corresponding branch, returning the value incremented by one. If the argument is a floating-point value, the float-specific branch applies and the value is doubled. For any other type, none of the `when` clauses match, and the function falls back to returning the argument unchanged. The important point is that the decision is driven entirely by type information, not by runtime inspection.

## `when`/`is` clauses

Generic `when`/`is` clauses can also be applied in more complex, nested contexts, where multiple type parameters interact with each other.

In the following example, the `list_contains` function is written to operate on both integer lists and string lists, even though the comparison logic differs between the two cases:

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

As noted earlier in the standard library documentation, `IntList` and `StringList` are specialized structures that wrap arrays of integers and strings, respectively. The function leverages this knowledge by pairing constraints on both the list type and the element type within the same `when` clause. The `cast` operator is used to convert a generic value into a concrete type, but only in situations where the type relationship has already been established by the `when` condition. This makes the conversion safe and explicit, while preserving static guarantees. As a result, the function can remain generic without resorting to unchecked casts or repeated runtime type tests.

Generic functions in Axe are also capable of returning values whose behavior depends on the type parameter, while still preserving a single, well-defined return type. For example:

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

In this case, `maybe_double` always returns a value of type `T`, but the computation performed varies depending on what `T` actually is. When instantiated with a floating-point type, floating-point arithmetic is used; when instantiated with a 32-bit integer, integer arithmetic applies instead. The return type is inferred directly from the input type, which makes the function predictable to use while still allowing type-specific behavior. This pattern is especially useful in numeric code, where the same conceptual operation should apply across multiple numeric representations.

Another important aspect of Axe’s generics is that generic functions can freely call other generic functions, with type parameters inferred automatically from the arguments passed. For example:

```axe
def add_or_concat[T](a: T, b: T): T {
    when T is i32 or T is float {
        return a + b;
    }
    when T is string {
        return a + b;
    }
    return a;
}

def process_values[T](x: T, y: T): T {
    return add_or_concat(x, y);
}
```

In this example, `process_values` is entirely agnostic about the concrete type of its parameters. It simply forwards them to `add_or_concat`, and the compiler determines which `when` clause applies based on the type supplied at the callsite. This allows generic abstractions to be layered without losing precision or control over behavior. 

These features make generics in Axe expressive without being opaque: type-driven specialization remains explicit in the source code, while the resulting functions behave as if they were hand-written for each supported type.
