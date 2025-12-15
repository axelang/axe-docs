# .\math.axec

## pub def clamp(value: i32, min: i32, max: i32): i32

Clamp integer

## pub def clamp_float(value: f64, min: f64, max: f64): f64

Clamp float

## pub def absolute(value: f64): f64

Absolute value

## pub def approx_equal(a: f64, b: f64, eps: f64): bool

Approximately equal

## pub def minimum(a: f64, b: f64): f64 { if a < b { return a; } else { return b; } }

Minimum

## pub def maximum(a: f64, b: f64): f64 { if a > b { return a; } else { return b; } }

Maximum

## pub def int_to_float(x: i32): f64

Converts an integer to a float.

## pub def floor(x: f64): f64

Floor of the number.

## pub def ceil(x: f64): f64

Ceiling of the number.

## pub def round(x: f64): f64

Round to the nearest float

## pub def mod_float(a: f64, b: f64): f64

Float modulus.

## pub def reduce_angle(x: f64): f64

Reduce angle to [0, 2PI]

## pub def sqrt(value: f64): f64

Square root (Newton)

## pub def pow(base: f64, exp: i32): f64

Integer exponent (exponentiation by squaring)

## pub def exp(x: f64): f64

Exponential series

## pub def ln(x: f64): f64

Natural logarithm

## pub def sin(x: f64): f64

Sine (reduced angle)

## pub def cos(x: f64): f64

Cosine

## pub def tan(x: f64): f64

Tangent

## pub def asin(x: f64): f64

Arcsine

## pub def acos(x: f64): f64

Arccosine

## pub def atan(x: f64): f64

Arctangent

## pub def powf(base: f64, expp: f64): f64

Float power: base^exp for non-integer exponents

## pub def atan2(y: f64, x: f64): f64

Two-argument arctangent: returns angle in radians between [-PI, PI]

## pub def atanh(x: f64): f64

Hyperbolic tangent inverse
