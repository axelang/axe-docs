Axe's builtin lists take the form of `list(T)` in code. Lists are dynamically sized, mutable collections that track their length and allow efficient element access and modification. 

They can store any type, including primitive types, strings, and user-defined models.

You can create a new list using `list(T)`, append elements, access elements by index, and iterate over the list. Example usage is as follows:

```axe
mut numbers: list(i32);

nums = [1, 2, 3, 4, 5];

val first: i32 = numbers.data[0];
val last: i32 = numbers.data[numbers.len - 1];

numbers.data[2] = 42;

append(numbers, 6);

for mut i = 0; i < numbers.len; i++ {
    println numbers.data[i];
}
```

Lists can also store strings or other models:

```axe
mut names: list(string);

append(names, str("Diana"));

for mut i = 0; i < names.len; i++ {
    println names.data[i];
}
```

Since lists track their length explicitly via the `.len` field, loops and bounds checks are simple and safe. You can also pass lists to functions, return them from functions, and combine them with generics for flexible, reusable code.

Appending elements will automatically resize the list if necessary, so you do not need to manually manage capacity in most cases. However, for performance-critical code, preallocating lists with the expected length and using direct element assignment can reduce unnecessary memory allocations.

Lists are foundational for building arrays, AST node collections, or dynamic argument lists in Axe programs. Combined with generics and the `append` function, they allow flexible, type-safe operations over arbitrary data.
