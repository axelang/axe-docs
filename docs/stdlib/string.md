# .\string.axec

## pub def init(initial_capacity: usize): StringBuilder

StringBuilder for efficient string concatenation.Instead of O(n²) repeated allocations, uses amortized O(1) appends.
Creates a new StringBuilder with the specified initial capacity.


## pub def ensure_capacity(sb: ref StringBuilder, additional: usize): void

Ensures the StringBuilder has enough capacity for additional bytes.

## pub def append(sb: ref StringBuilder, s: string): void

Appends a string to the StringBuilder.

## pub def append_c(sb: ref StringBuilder, s: ref char): void

Appends a C string literal to the StringBuilder.

## pub def append_char(sb: ref StringBuilder, c: char): void

Appends a single character to the StringBuilder.Inlined capacity check for performance.


## pub def to_string(sb: ref StringBuilder): string

Converts the StringBuilder to a string.The StringBuilder remains valid and can continue to be used.


## pub def clear(sb: ref StringBuilder): void

Clears the StringBuilder without deallocating memory.

## pub def destroy(sb: ref StringBuilder): void

Destroys the StringBuilder and frees memory.

## pub def create(data: ref char): string

string model representing a dynamic string with length tracking.Creates a new string from a char pointer.


## pub def create_with_capacity(arena: ref Arena, capacity: i32): string

Creates a new empty string with specified capacity using arena allocation.

## pub def destroy(s: ref string)

## pub def replace_all(s: string, from: string, dest: string): string

Replace all non-overlapping occurrences of `from` in `s` with `to`.Optimized to use StringBuilder instead of O(n²) repeated concatenations.


## pub def i32_to_string(value: i32): string

Convert some i32 to a string.

## pub def str_len(s: string): usize

Returns the length of a string.

## pub def to_title_case(s: string): string

Convert some string to titlecase.

## pub def to_upper(s: string): string

Converts string to uppercase.

## pub def to_lower(s: string): string

Converts string to lowercase.

## pub def str_copy(src: string, desta: mut string): void

Copies source string to destination. Modifies dest in place.

## def concat_chr(a: mut string, b: char): string

Concatenates a character to the end of a string. Returns the modified string.Mut here just means that the stack instance is mutable, not that the string data itself is modified in place.


## pub def substring_se(s: string, start: i32, end: i32): string

Returns a substring from start to end (exclusive).
Optimized to use direct memory allocation instead of O(n²) concat_chr calls.


## pub def substring_scse(s: string, start: i32, end: i32): ref char

Returns a substring from start to end (exclusive).

## pub def substring_cse(s: ref char, start: i32, end: i32): ref char

Returns a substring from char* s from start to end (exclusive). Caller must free the result.


## pub def equals_c(a: string, b: ref char): bool

Compares string with char*. Returns 0 if equal.

## pub def compare(a: string, b: string): i32

Compares two strings. Returns 0 if equal.

## pub def string_equals(a: string, b: string): bool

Checks if two strings are equal. Returns true if equal.

## pub def concat_c(original: string, addon: ref char): string

Concatenates a char pointer to a string

## pub def concat(dest: string, src: string): string

Concatenates source string to destination. Returns a new string.

## pub def first_occurrence(s: string, c: i32): ref char

Finds first occurrence of character in string. Returns pointer or 0.

## pub def substring(haystack: string, needle: string): ref char

Finds first occurrence of substring in string. Returns pointer or 0.

## pub def str_contains(s: string, substr: string): bool

Checks if string contains substring.

## pub def str_contains_c(s: string, substr: ref char): bool

Checks if string contains substring.

## pub def str_to_int(s: string): i32

Converts string to integer.

## pub def str_to_long(s: ref char): i64

Converts string to long integer.

## pub def is_alpha(c: i32): i32

Checks if character is alphabetic.

## pub def is_digit(c: i32): i32

Checks if character is numeric.

## pub def is_alphanum(c: i32): i32

Checks if character is alphanumeric.

## pub def to_upper_chrptr(s: ref char): ref char

Converts char* to uppercase.

## pub def to_lower_chrptr(s: ref char): ref char

Converts char* to lowercase.

## pub def to_upper_chr(c: i32): i32

Converts character to uppercase.

## pub def to_lower_chr(c: i32): i32

Converts character to lowercase.

## pub def str_dup(s: ref char): ref char

Allocates and copies a string. Caller must free the result.

## pub def str_ncmp(s1: ref char, s2: ref char, n: i32): i32

Compares first n characters of two strings. Returns 0 if equal.

## pub def str_ncopy(dest: ref char, src: ref char, n: i32): ref char

Copies at most n characters from source to destination.

## pub def int_to_str(value: i32, buffer: ref char): ref char

Converts an integer to a string. Buffer must be at least 12 bytes.

## pub def long_to_str(value: i64, buffer: ref char): ref char

Converts a long to a string. Buffer must be at least 21 bytes.

## pub def float_to_str(value: f32, buffer: ref char): ref char

Converts a float to a string. Buffer must be at least 32 bytes.

## pub def double_to_str(value: f64, buffer: ref char): ref char

Converts a double to a string. Buffer must be at least 32 bytes.

## pub def get_char(s: string, pos: i32): char

Returns the character at position `pos` in string `s`.

## pub def find_char_from(s: string, c: char, start: usize): i32

Returns the index of the first occurrence of character `c` in `s` at or after `start`.Returns -1 if the character is not found.


## pub def find_last_char(s: string, c: char): i32

Returns the index of the last occurrence of character `c` in `s`.Returns -1 if the character is not found.


## pub def find_substr(s: string, substr: string): i32

Returns the index of the first occurrence of `substr` inside `s`, or -1 if not found.

## pub def substr(s: string, start: i32, length: i32): string

Returns a substring of `s` starting at `start` with the given `length`.If `start` is beyond the end of the string or `length` is zero, an empty string is returned.
The function clamps the requested range to the bounds of the source string.


## pub def has_prefix(s: string, prefix: string): bool

Checks if string has prefix.

## pub def has_suffix(s: string, suffix: string): bool

Checks if string has suffix.

## pub def trim_prefix(s: string, prefix: string): string

Removes prefix from string.

## pub def trim_suffix(s: string, suffix: string): string

Removes suffix from string.

## pub def lstrip(s: string): string

Strip leading whitespace from a string.

## pub def rstrip(s: string): string

Strip trailing whitespace from a string.

## pub def strip(s: string): string

String trailing and leading whitespace.

## pub def str(data: ref char): string

Convenience function to convert a char* to a string.
