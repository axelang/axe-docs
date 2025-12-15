# .\json.axec

## def parse(json_str: string): ref char

JSON value typesParse a JSON string and return a document


## def free_doc(doc: ref char)

Free a JSON document

## def get_root(doc: ref char): ref char

Get the root value from a JSON document

## def is_null(value: ref char): bool

Check if a value is null

## def is_bool(value: ref char): bool

Check if a value is a boolean

## def is_num(value: ref char): bool

Check if a value is a number

## def is_str(value: ref char): bool

Check if a value is a string

## def is_array(value: ref char): bool

Check if a value is an array

## def is_object(value: ref char): bool

Check if a value is an object

## def get_bool(value: ref char): bool

Get boolean value

## def get_int(value: ref char): i32

Get integer value

## def get_int64(value: ref char): i64

Get 64-bit integer value

## def get_real(value: ref char): f64

Get floating point value

## def get_str(value: ref char): string

Get string value

## def get_len(value: ref char): usize

Get the length of an array or object

## def obj_get(obj: ref char, key: string): ref char

Get a value from an object by key

## def arr_get(arr: ref char, idx: usize): ref char

Get a value from an array by index

## def arr_get_first(arr: ref char): ref char

Get the first element in an array

## def arr_get_last(arr: ref char): ref char

Get the last element in an array

## def stringify(doc: ref char): string

Serialize a JSON document to a string

## def stringify_val(value: ref char): string

Serialize a JSON value to a string

## def stringify_pretty(doc: ref char): string

Serialize with pretty formatting

## def read_file(path: string): ref char

Read JSON from a file

## def write_file(path: string, doc: ref char): bool

Write JSON to a file
