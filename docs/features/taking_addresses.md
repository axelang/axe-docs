To take the address of some pointer, simply use the `addr(...)` construct, like so:

```axe
val link_libs: ref StringList = StringList.create(addr(arena), 16);
```