The `extern` feature is useful for declaring the signatures of external C/C++ functions.

An example of its usage is as follows:

```
use external("yyjson.h");

extern def yyjson_read(json: char*, size: size_t, flags: i32): char*;
extern def yyjson_doc_free(doc: char*);
extern def yyjson_doc_get_root(doc: char*): char*;
extern def yyjson_is_null(value: char*): bool;
extern def yyjson_is_bool(value: char*): bool;
extern def yyjson_is_num(value: char*): bool;
extern def yyjson_is_str(value: char*): bool;
```
