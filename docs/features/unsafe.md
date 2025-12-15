It is of note that `unsafe` in Axe is a "special-case" construct that allows you to perform low-level operations that bypass some of the language’s safety guarantees. 

They are typically used when interacting with C libraries, performing manual memory management, or working directly with pointers.

To mark a block of code as unsafe, you use the `unsafe { ... }` construct. Inside an unsafe block, you can call C functions directly using the `C.` prefix. For example:

```axe
unsafe {
    val ptr: ref char = C.malloc(128); // Allocate 128 bytes
    if ptr != nil {
        // Use the memory...
        C.free(ptr); // Free the allocated memory
    }
}
```

Here, `C.malloc` and `C.free` are standard C library functions. The return types are C-style pointers (`ref char`, `void*`, etc.), which are not automatically managed by the Axe runtime. It is the programmer’s responsibility to ensure proper memory allocation and deallocation.

Unsafe blocks also allow explicit pointer dereferencing using the `*.` operator. For example, if you have a pointer to a structure, you can access its fields directly:

```axe
pub model Point {
    x: i32;
    y: i32;
}

unsafe {
    val p: ref Point = cast[ref Point](C.malloc(C.sizeof(Point)));
    p*.x = 10;  // Access x field through pointer
    p*.y = 20;  // Access y field through pointer
    println(p*.x, ", ", p*.y);
    C.free(p);
}
```

In this example, `p*.` tells the compiler that you intend to access the fields of the pointed-to structure directly, bypassing any automatic memory or bounds checks.

Unsafe blocks are powerful, but they come with significant risks:

* Memory leaks can occur if allocated memory is not freed.
* Pointer dereferencing can lead to undefined behavior if the pointer is invalid or null.
* Type safety is partially bypassed, so casting to the wrong type can cause crashes or data corruption.

For these reasons, unsafe blocks should be used sparingly and only when necessary, such as:

* Interfacing with C libraries.
* Implementing low-level data structures.
* Optimizing performance-critical code that cannot be expressed safely otherwise.

Outside of `unsafe`, Axe enforces strict memory and type safety, so you should confine unsafe operations to minimal, well-reviewed sections of code.

You can combine unsafe operations with models, arrays, or lists to perform advanced memory management patterns while still leveraging Axe’s standard library elsewhere.

For example, creating a manual string buffer using C memory:

```axe
unsafe {
    val buf: ref char = C.malloc(256);
    if buf != nil {
        C.memcpy(buf, str("Hello").data, 5);
        buf[5] = '\0';
        println(str(buf));
        C.free(buf);
    }
}
```

Unsafe blocks provide the bridge between Axe and the underlying system, giving you low-level control when needed while keeping most of the language safe by default.
