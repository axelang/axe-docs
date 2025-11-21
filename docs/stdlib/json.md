# .\json.axec

## def parse(json_str: string): char*

JSON value typesParse a JSON string and return a document


## def free_doc(doc: char*)

Free a JSON document

## def get_root(doc: char*): char*

Get the root value from a JSON document

## def is_null(value: char*): bool

Check if a value is null

## def is_bool(value: char*): bool

Check if a value is a boolean

## def is_num(value: char*): bool

Check if a value is a number

## def is_str(value: char*): bool

Check if a value is a string

## def is_array(value: char*): bool

Check if a value is an array

## def is_object(value: char*): bool

Check if a value is an object

## def get_bool(value: char*): bool

Get boolean value

## def get_int(value: char*): i32

Get integer value

## def get_int64(value: char*): i64

Get 64-bit integer value

## def get_real(value: char*): f64

Get floating point value

## def get_str(value: char*): string

Get string value

## def get_len(value: char*): usize

Get the length of an array or object

## def obj_get(obj: char*, key: string): char*

Get a value from an object by key

## def arr_get(arr: char*, idx: usize): char*

Get a value from an array by index

## def arr_get_first(arr: char*): char*

Get the first element in an array

## def arr_get_last(arr: char*): char*

Get the last element in an array

## def stringify(doc: char*): string

Serialize a JSON document to a string

## def stringify_val(value: char*): string

Serialize a JSON value to a string

## def stringify_pretty(doc: char*): string

Serialize with pretty formatting

## def read_file(path: string): char*

Read JSON from a file

## def write_file(path: string, doc: char*): bool

Write JSON to a file
