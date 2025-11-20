# .\math.axec

## def clamp(value: i32, min: i32, max: i32): i32

Clamp integer

## def clamp_float(value: f64, min: f64, max: f64): f64

Clamp float

## def absolute(value: f64): f64

Absolute value

## def approx_equal(a: f64, b: f64, eps: f64): bool

Approximately equal

## def minimum(a: f64, b: f64): f64 { if a < b { return a; } else { return b; } }

Minimum

## def maximum(a: f64, b: f64): f64 { if a > b { return a; } else { return b; } }

Maximum

## def int_to_float(x: i32): f64

Converts an integer to a float.

## def floor(x: f64): f64

Floor of the number.

## def ceil(x: f64): f64

Ceiling of the number.

## def round(x: f64): f64

Round to the nearest float

## def mod_float(a: f64, b: f64): f64

Float modulus.

## def reduce_angle(x: f64): f64

Reduce angle to [0, 2PI]

## def sqrt(value: f64): f64

Square root (Newton)

## def pow(base: f64, exp: i32): f64

Integer exponent (exponentiation by squaring)

## def exp(x: f64): f64

Exponential series

## def ln(x: f64): f64

Natural logarithm

## def sin(x: f64): f64

Sine (reduced angle)

## def cos(x: f64): f64

Cosine

## def tan(x: f64): f64

Tangent

## def asin(x: f64): f64

Arcsine

## def acos(x: f64): f64

Arccosine

## def atan(x: f64): f64

Arctangent

## def powf(base: f64, expp: f64): f64

Float power: base^exp for non-integer exponents

## def atan2(y: f64, x: f64): f64

Two-argument arctangent: returns angle in radians between [-PI, PI]

## def atanh(x: f64): f64

Hyperbolic tangent inverse
