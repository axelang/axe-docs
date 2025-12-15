Strings in Axe are represented using a dedicated `string` model and a `StringBuilder` for efficient concatenation. Unlike simple C-style strings, these models track the length and capacity explicitly, allowing safe and performant operations.

`StringBuilder` is useful when you need to build up a string incrementally. Repeated concatenation using regular strings can be inefficient because each operation may require a new allocation and copy. `StringBuilder` amortizes this cost by preallocating a buffer that grows as needed. You can create a `StringBuilder` using `StringBuilder.init`, specifying an initial capacity, and then append strings or characters with `append`, `append_c`, or `append_char`.

```
mut sb: StringBuilder = StringBuilder.init(128);
StringBuilder.append(sb, str("Hello, "));
StringBuilder.append(sb, str("world!"));
val result: string = StringBuilder.to_string(sb);
```

After building a string, `to_string` produces a `string` containing the concatenated data. The `StringBuilder` remains valid and can be reused. You can reset it using `clear`, which does not deallocate memory, or free resources entirely with `destroy`.

The `string` model represents immutable strings with length tracking. You can create a string from a C-style char pointer using `string.create` or from a preallocated arena using `string.create_with_capacity`. These functions allocate memory and copy data safely. Strings also track capacity, which can be useful for operations that append additional data without reallocating every time.

```axe
val s1: string = string.create(str("Hello"));
val s2: string = string.create_with_capacity(arena, 64);
```

The `destroy` method frees a string's memory and resets its fields, making it safe to reuse the variable.

For multiline strings, backticks allow you to define a string spanning multiple lines:

```axe
val multi: string = str(`This is
a multiline
string`);
```

Regular strings are defined using double quotes:

```axe
val single: string = str("Hello, world.");
```

`StringBuilder` and `string` provide the foundation for safe, efficient string operations in Axe. Use `StringBuilder` for performance-sensitive concatenations, and rely on the `string` model for standard immutable strings with predictable memory management.

You can also combine `StringBuilder` with generic functions to build strings dynamically based on different input types, making it flexible for templating or logging utilities.
