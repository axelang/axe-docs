Error handling in Axe is explicit through use of error unions from returns. It is similar to Go in this regard in that there is no try/catch construct.

Creating an error can be done through use of the `std.errors` module.

```axe
use std.errors;
use std.io;

def main() {
    panic(error.create("This is some runtime error."));
    println "Will never print...";
}
```

In this case we create an error through use of the create static function on the error type. The `panic` function is used to stop the program in the case of a fatal error. Though generally it is preferred to set the return type of your function to an error union, such that error propagation is made possible. For example:

```axe
model SomeFunctionResult {
    result: union {
        err: error;
        result: string;
    }
}

pub def some_function(): SomeFunctionResult {
    
}
```

# Error Handling

Axe provides a straightforward error handling model using return values and the `error` type, combined with the `panic` function for unrecoverable errors. This approach ensures predictable, efficient error handling without exceptions or try-catch blocks.

## The Error Type

The `error` type represents an error condition with an associated message:

```axe
use std.errors (error, panic, enforce);

val my_error: error = error.create("Something went wrong");
```

### Creating Errors

Use `error.create()` to create a new error with a message:

```axe
use std.errors (error);

def validate_age(age: i32): bool {
    if age < 0 {
        val err: error = error.create("Age cannot be negative");
        panic(err);
    }
    return age >= 18;
}
```

## Return Value Based Error Handling

The idiomatic Axe approach uses return values to signal success or failure:

```axe
use std.string;
use std.io (println_str);

/// Parse an integer, returning success/failure
def parse_int(text: string): i32 {
    // Return 0 for invalid input, or parsed value for valid
    if str_len(text) == 0 {
        return 0;  // Sentinel value indicating failure
    }
    
    mut result: i32 = 0;
    for mut i = 0; i < str_len(text); i++ {
        val ch: char = get_char(text, i);
        if ch >= '0' and ch <= '9' {
            result = result * 10 + (ch - '0');
        } else {
            return 0;  // Invalid character
        }
    }
    return result;
}

// Usage with error checking
def main() {
    val num: i32 = parse_int(str("42"));
    if num == 0 {
        println_str str("Parse failed");
        return;
    }
    println_str str("Successfully parsed number");
}
```

## Using Models for Complex Results

For operations that need to return both a value and status information, use models:

```axe
use std.string;
use std.errors (error, panic);

/// Result model combining success status and value
model ParseResult {
    success: bool;
    value: i32;
    error_msg: string;
}

def try_parse_int(text: string): ParseResult {
    mut result: ParseResult;
    result.success = false;
    result.value = 0;
    result.error_msg = str("");
    
    if str_len(text) == 0 {
        result.error_msg = str("Input is empty");
        return result;
    }
    
    mut value: i32 = 0;
    for mut i = 0; i < str_len(text); i++ {
        val ch: char = get_char(text, i);
        if ch >= '0' and ch <= '9' {
            value = value * 10 + (ch - '0');
        } else {
            result.error_msg = str("Invalid character at position ");
            return result;
        }
    }
    
    result.success = true;
    result.value = value;
    return result;
}

// Usage
def main() {
    val result: ParseResult = try_parse_int(str("42"));
    if result.success {
        println_str str("Parsed successfully");
    } else {
        println_str result.error_msg;
    }
}
```

## Guard Clauses for Early Returns

Guard clauses enable clean error handling by checking conditions upfront:

```axe
use std.string;
use std.io (println_str);

def process_file(filename: string, content: string): bool {
    // Guard: validate inputs
    if str_len(filename) == 0 {
        println_str str("error: filename cannot be empty");
        return false;
    }

    if str_len(content) == 0 {
        println_str str("error: content cannot be empty");
        return false;
    }

    if str_len(content) > 1000000 {
        println_str str("error: content too large");
        return false;
    }

    // Main logic - all guards passed
    do_write_file(filename, content);
    return true;
}
```

### Benefits of Guard Clauses

- **Fail Fast**: Check for error conditions immediately
- **Reduced Nesting**: Avoid deeply nested conditional blocks
- **Clarity**: Error cases are explicit and visible
- **Maintainability**: Easy to add or remove error checks

## Panic for Unrecoverable Errors

Use `panic()` for errors from which recovery is impossible. This should be reserved for true exceptional conditions:

```axe
use std.errors (error, panic);
use std.arena (Arena);

def allocate_resources(size: usize): Arena {
    if size == 0 {
        val err: error = error.create("Cannot allocate zero bytes");
        panic(err);  // Program will terminate
    }
    
    mut arena: Arena = Arena.create(size);
    return arena;
}
```

**When to Use Panic:**

- Out of memory conditions
- Corrupted internal state
- Invariant violations that indicate program bugs
- Unsafe operation failures

**When NOT to Use Panic:**

- Expected failures (invalid user input, network issues)
- Recoverable errors (file not found, parsing failures)
- Conditions that should propagate to the caller

## Enforce for Assertions

The `enforce()` function combines a condition check with panic for assertion-like behavior:

```axe
use std.errors (error, enforce);

def divide(a: i32, b: i32): i32 {
    enforce(b != 0, error.create("Division by zero"));
    return a / b;
}

def validate_index(index: i32, size: i32) {
    enforce(index >= 0, error.create("Index cannot be negative"));
    enforce(index < size, error.create("Index out of bounds"));
}
```

### Enforce vs. Panic

- `enforce()` is more concise for simple assertions
- `panic()` is more explicit and allows complex logic
- Both terminate the program on failure

## Error Propagation Patterns

### Pattern 1: Sentinel Values

Use special return values to indicate errors:

```axe
def find_in_list(items: ref StringList, target: string): i32 {
    for mut i = 0; i < len(deref(items)); i++ {
        if equals_c(StringList.get(items, i), target) {
            return i;
        }
    }
    return -1;  // Not found sentinel
}

// Usage
val index: i32 = find_in_list(my_list, search_term);
if index < 0 {
    println_str str("Item not found");
}
```

### Pattern 2: Boolean Success Flag

```axe
def write_config(filename: string, data: string): bool {
    if !validate_config(data) {
        return false;  // Validation failed
    }
    
    if !create_backup(filename) {
        return false;  // Backup creation failed
    }
    
    if !write_file(filename, data) {
        return false;  // File write failed
    }
    
    return true;  // Success
}

// Usage
if !write_config(str("config.txt"), config_data) {
    println_str str("Failed to write configuration");
    return;
}
```

### Pattern 3: Result Model

For detailed error information, use a model containing status and details:

```axe
model FileResult {
    success: bool;
    data: string;
    error_code: i32;
    error_msg: string;
}

def read_file(path: string): FileResult {
    mut result: FileResult;
    result.success = false;
    result.data = str("");
    result.error_code = 0;
    result.error_msg = str("");
    
    // Attempt to read file
    if !file_exists(path) {
        result.error_code = 1;
        result.error_msg = str("File not found");
        return result;
    }
    
    result.data = read_file_contents(path);
    result.success = true;
    return result;
}
```

## Cleanup and Resource Management

Always clean up resources, even when errors occur. Use guard clauses to structure cleanup:

```axe
use std.arena (Arena);
use std.io (println_str);

def process_data(filename: string): bool {
    // Allocate resources
    mut arena: Arena = Arena.create(1024 * 1024);
    
    // Guard: file validation
    if !file_exists(filename) {
        println_str str("File not found");
        Arena.destroy(addr(arena));
        return false;
    }
    
    // Guard: read validation
    val content: string = read_file(filename);
    if str_len(content) == 0 {
        println_str str("File is empty");
        Arena.destroy(addr(arena));
        return false;
    }
    
    // Process data
    val result: bool = do_processing(addr(arena), content);
    
    // Cleanup (always executed)
    Arena.destroy(addr(arena));
    
    return result;
}
```

## Common Error Handling Patterns

### Validating Multiple Conditions

```axe
def create_user(name: string, email: string, age: i32): bool {
    // Validate all inputs before processing
    if str_len(name) == 0 {
        println_str str("Name cannot be empty");
        return false;
    }
    
    if str_len(email) == 0 or find_char(email, '@') < 0 {
        println_str str("Invalid email");
        return false;
    }
    
    if age < 18 {
        println_str str("User must be 18 or older");
        return false;
    }
    
    // All validations passed
    store_user(name, email, age);
    return true;
}
```

### Chaining Operations with Error Checks

```axe
def process_pipeline(input: string): bool {
    // Step 1
    val step1_result: string = validate_input(input);
    if str_len(step1_result) == 0 {
        println_str str("Validation failed");
        return false;
    }
    
    // Step 2
    if !transform_data(step1_result) {
        println_str str("Transformation failed");
        return false;
    }
    
    // Step 3
    if !store_output(step1_result) {
        println_str str("Storage failed");
        return false;
    }
    
    return true;
}
```

## Error Handling Best Practices

### 1. Use Appropriate Error Reporting

```axe
//  Good: Clear, actionable error messages
if age < 0 {
    println_str str("error: age cannot be negative");
    return false;
}

//  Poor: Vague error message
if age < 0 {
    println_str str("Invalid input");
    return false;
}
```

### 2. Validate Early

```axe
//  Good: Validate at function entry
def process(data: string): bool {
    if str_len(data) == 0 {
        return false;
    }
    // ... rest of implementation
}

//  Poor: Let invalid data propagate
def process(data: string): bool {
    val result: i32 = do_something(data);  // May fail
    // ...
}
```

### 3. Document Error Conditions

```axe
/// Process a file
/// 
/// Returns true if successful, false if:
/// - File does not exist
/// - File is unreadable
/// - Content is invalid
/// - Insufficient memory
def process_file(path: string): bool {
    // implementation
}
```

### 4. Use Models for Complex Scenarios

```axe
//  Good: Rich error information
model ApiResponse {
    success: bool;
    status_code: i32;
    data: string;
    error_msg: string;
}

//  Poor: Limited information
def call_api(url: string): i32 {
    // only returns status code
}
```

### 5. Be Consistent in Error Handling

```axe
//  Good: Consistent pattern throughout
def operation_a(): bool { /* ... */ }
def operation_b(): bool { /* ... */ }
def operation_c(): bool { /* ... */ }

//  Poor: Inconsistent approaches
def operation_a(): bool { /* ... */ }
def operation_b(): i32 { /* ... */ }
def operation_c(): Model { /* ... */ }
```

## Comparison with Other Languages

### vs. Exceptions (Java, Python, C++)

```
Axe (Return Values):           Java (Try-Catch):
├─ Explicit error handling      ├─ Exception propagation
├─ No control flow exceptions   ├─ Implicit exceptions
├─ Predictable performance      ├─ Exception handling overhead
└─ Clear error paths            └─ Multiple exception types

Axe advantages:
- No hidden control flow
- Deterministic performance
- Simpler to reason about
- No unexpected jumps

Java advantages:
- Less boilerplate for common cases
- Rich exception hierarchy
```

### vs. Go (error interface)

```
Axe:                           Go:
├─ Named return models         ├─ Multiple return values
├─ Bool/model-based errors     ├─ error interface
├─ Guard clauses               ├─ if err != nil
└─ Type-safe results           └─ Dynamic error handling

Both similar in philosophy but Axe is more type-safe.
```
