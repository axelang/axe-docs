# .\time.axec

## pub def wait(ms: i32)

Represents the current date and timeSuspends the current thread for the specified number of milliseconds


## pub def now(): DateTime

Returns the current date and time

## pub def difference(dt1: DateTime, dt2: DateTime): i64

Simple and accurate epoch-based difference calculation

## pub def print_time(dt: DateTime, newline: bool)

Prints the date and time in the format "YYYY-MM-DD HH:MM:SS.mmm" with optional newline
