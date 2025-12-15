# .\regex.axec

## pub def compile(pattern: string): regex

Simple regex-like support built on substring search.Compile a pattern into a regex value.


## pub def is_match(re: regex, text: string): bool

Returns true if the given text contains the pattern as a substring.

## def match(pattern: string, text: string): bool

Returns true if the given text contains pattern as a substring.

## pub def full_match(pattern: string, text: string): bool

Convenience helper: returns true if text fully equals pattern.
