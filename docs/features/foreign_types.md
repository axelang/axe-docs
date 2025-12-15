Foreign types allow for the declaration of C types so as to bypass the Axe type system, this will lead to a compiler error if you declare a foreign type that is not linked.

Example usage is as follows:

```
pub def read_file(path: string): string {
    mut f: ref FILE = fopen(path.data, "rb");

    if (!f) {
        panic(error.create("Failed to open file"));
    }

    foreign {SEEK_END, SEEK_SET};

    C.fseek(f, 0, SEEK_END);
    val size: usize = C.ftell(f);
    C.fseek(f, 0, SEEK_SET);
    mut buf: ref char = cast[ref char](C.malloc(size + 1));

    C.fread(buf, 1, size, f);
    buf[size] = '\0';
    C.fclose(f);

    return string.create(buf);
}
```

Here the types `SEEK_END` and `SEEK_SET` are foreign C types.