To dereference a pointer, either on LHS or RHS of an expression, use the `deref` construct, like so:

```axe
def worker(arena: ref Arena, value: i32): i32 {
    mut p: ref i32 = cast[ref i32](Arena.alloc(arena, sizeof(i32)));
    deref(p) = value * value;
    return deref(p);
}
```