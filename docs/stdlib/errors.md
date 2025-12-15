# .\errors.axec

## pub def create(msg: ref char): error

Represents some kind of error in the program.

## pub def print_self(err: error)

## pub def panic(err: error)

Stops the program with the given error message.

## pub def enforce(condition: bool, err: error)

Enforces a condition, panics if the condition is false.

## pub def enforce_raw(condition: bool, msg: ref char)

Enforces a condition, panics with the given message if the condition is false.

## def test_error(): error
