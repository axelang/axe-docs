# .\string.axec

## def concat_chr(a: mut string, b: char): string

StringBuilder for efficient string concatenation.Instead of O(n²) repeated allocations, uses amortized O(1) appends.
Creates a new StringBuilder with the specified initial capacity.
Ensures the StringBuilder has enough capacity for additional bytes.
Appends a string to the StringBuilder.
Appends a C string literal to the StringBuilder.
Appends a single character to the StringBuilder.
Inlined capacity check for performance.
Converts the StringBuilder to a string.
The StringBuilder remains valid and can continue to be used.
Clears the StringBuilder without deallocating memory.
Destroys the StringBuilder and frees memory.
string model representing a dynamic string with length tracking.
Creates a new string from a char pointer.
Creates a new empty string with specified capacity using arena allocation.
Replace all non-overlapping occurrences of `from` in `s` with `to`.
Optimized to use StringBuilder instead of O(n²) repeated concatenations.
Convert some i32 to a string.
Returns the length of a string.
Convert some string to titlecase.
Converts string to uppercase.
Converts string to lowercase.
Copies source string to destination. Modifies dest in place.
Concatenates a character to the end of a string. Returns the modified string.
Mut here just means that the stack instance is mutable, not that the string data itself is modified in place.

