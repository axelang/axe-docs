Macros are defined through use of the `macro` keyword, for example:

```axe
macro some_macro(x: untyped, y: untyped) {
    x + y;
}

def main() {
    println(some_macro(1, 2));
}
```

In this case the result (3) would be printed to the standard output stream.

The heavy use of macros is generally not advisable, as it can lead to readability issues. Macros operate on the syntax tree rather than on evaluated values, which allows them to generate code dynamically, but also makes debugging more difficult because the code you write is not always the code that executes.

Macros can accept untyped parameters, which gives them flexibility to manipulate different kinds of expressions.

Moreover, differently from generic functions, macros can contain function definitions, this can sometimes be useful for defining numerous similar functions, where the only difference is type based, but generally this is not advisable, and it is preferred to use either overloads or generic functions.

## Syntax Tree Manipulation

Macros do not operate on the values of variables directly. Instead, they operate on the code itself before it is executed. This means that a macro can generate or transform code at compile-time. For example, you could create a macro to automatically wrap a block of code with logging statements or error handling.


## Parameters

Macros can accept both typed and untyped parameters:

* Typed parameters enforce that the macro is called with expressions of a certain type.
* Untyped parameters allow any expression to be passed, providing maximum flexibility in code generation.

Because macros receive code rather than evaluated results, untyped parameters are particularly useful for creating reusable code patterns.


## Return Values

Macros return code fragments that are inserted into the program at the call site. This is different from functions, which return evaluated values. As a result:

* The returned code must be syntactically valid.
* Errors in macro-generated code may only appear at compile-time.
* Macros can produce multiple statements or even entire function definitions.

## Use Cases

Macros are commonly used for:

* Code generation: Automating repetitive patterns to reduce boilerplate.
* Compile-time checks: Enforcing constraints before runtime.
* Domain-specific language creation: Creating specialized syntax tailored to a problem domain.
* Instrumentation: Injecting logging, tracing, or debugging code automatically.


## Caveats

While powerful, macros should be used with caution:

* Readability: Macro-heavy code can be difficult to read and understand.
* Debugging: Errors may appear in generated code, making stack traces and error messages less clear.
* Maintenance: Changes to macro definitions can have widespread, sometimes unexpected, effects.
