# .\regex.axec

## model regex

Simple regex-like support built on substring search.

## def compile(pattern: string): regex

Compile a pattern into a regex value.

## def is_match(re: regex, text: string): bool

Returns true if the given text contains the pattern as a substring.

## def match(pattern: string, text: string): bool

Returns true if the given text contains pattern as a substring.

## def full_match(pattern: string, text: string): bool

Convenience helper: returns true if text fully equals pattern.
