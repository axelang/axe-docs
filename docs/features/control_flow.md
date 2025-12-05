# Control Flow

Control flow statements in Axe determine the order and conditions under which code is executed. Axe provides a variety of constructs for managing program flow with clear, predictable semantics.

## Conditional Statements

### if-elif-else

The `if` statement executes a block of code if a condition is true. Use `elif` (else if) for multiple conditions and `else` for a fallback block.

```axe
val age: i32 = 25;

if age < 18 {
    println "Minor";
} elif age < 65 {
    println "Adult";
} else {
    println "Senior";
}
```

**Characteristics:**

- Conditions must be of type `bool`
- `elif` and `else` blocks are optional
- Multiple `elif` branches can be chained
- Each branch is mutually exclusive
- No implicit type coercion of conditions

### Boolean Operators

Axe supports standard boolean operators for combining conditions:

```axe
val x: i32 = 10;
val y: i32 = 20;
val valid: bool = true;

// AND operator
if x > 5 and y < 25 {
    println "Both conditions true";
}

// OR operator
if x > 15 or y > 15 {
    println "At least one condition true";
}

// NOT operator
if !valid {
    println "Not valid";
}
```

**Short-circuit Evaluation:**

- `and` operator: Returns false immediately if the left operand is false
- `or` operator: Returns true immediately if the left operand is true
- This ensures efficient evaluation and allows safe property access chains

## Loops

### Loop Statement

The `loop` statement creates an infinite loop that continues until a `break` statement is encountered.

```axe
mut counter: i32 = 0;

loop {
    if counter >= 5 {
        break;
    }
    println counter;
    counter = counter + 1;
}
```

### For Loops

Axe provides C-style `for` loops for iterating a specific number of times:

```axe
// Traditional for loop
for mut i = 0; i < 10; i++ {
    println i;
}

// Using references
val data: ref StringList = get_data();
for mut i = 0; i < len(deref(data)); i++ {
    val item: string = StringList.get(data, i);
    println item;
}
```

**For Loop Structure:**

```
for [initialization]; [condition]; [increment] {
    [body]
}
```

- **Initialization**: Declares and initializes loop variables (e.g., `mut i = 0`)
- **Condition**: Boolean expression evaluated before each iteration
- **Increment**: Expression executed after each iteration (e.g., `i++`)
- **Body**: Code executed in each iteration

### Parallel For Loops

For CPU-intensive operations, Axe supports parallel for loops using OpenMP:

```axe
parallel for mut i = 0; i < 1000; i++ {
    val result: i32 = expensive_computation(i);
    process_result(result);
}
```

**Parallel For Loop Rules:**

- Loop variable must be mutable
- Requires OpenMP support (automatically linked when detected)
- Safe for data-parallel algorithms
- Best for computationally intensive iterations
- Avoid side effects and shared state modifications

### Break and Continue

Control loop execution with `break` and `continue`:

```axe
// Using break to exit loop
for mut i = 0; i < 100; i++ {
    if should_exit(i) {
        break;
    }
    process(i);
}

// Using continue to skip to next iteration
for mut i = 0; i < 100; i++ {
    if skip_this(i) {
        continue;
    }
    process(i);
}
```

## Switch Statements

Switch statements provide efficient multi-way branching based on discrete values:

```axe
val status_code: i32 = 404;

switch status_code {
    case 200 {
        println "OK";
    }
    case 400 {
        println "Bad Request";
    }
    case 404 {
        println "Not Found";
    }
    case 500 {
        println "Server Error";
    }
    default {
        println "Unknown status";
    }
}
```

**Switch Characteristics:**

- Supports integer and string expressions
- Multiple case branches with associated blocks
- Optional `default` block (fallback)
- Each case is independent (no fall-through)
- Cases are mutually exclusive
- Efficient for many conditions

### Default Case

The `default` case is optional and executes if no case matches:

```axe
val command: string = get_user_input();

switch command {
    case "start" {
        initialize();
    }
    case "stop" {
        shutdown();
    }
    default {
        println "Unknown command";
    }
}
```

## Guard Clauses

Guard clauses are early returns used to exit functions when conditions aren't met, improving code readability:

```axe
def validate_input(data: string): bool {
    // Guard: check empty
    if str_len(data) == 0 {
        println "error: empty input";
        return false;
    }

    // Guard: check length
    if str_len(data) > 1000 {
        println "error: input too long";
        return false;
    }

    // Guard: check format
    if !is_valid_format(data) {
        println "error: invalid format";
        return false;
    }

    // Main logic here - all guards passed
    process_data(data);
    return true;
}
```

**Benefits of Guard Clauses:**

- Reduces nesting and improves readability
- Makes error cases explicit
- Follows the "fail fast" principle
- Reduces cognitive complexity

## Pattern Matching

While Axe doesn't have built-in pattern matching, similar functionality can be achieved with switch statements and conditional checks:

```axe
model Result {
    success: bool;
    value: i32;
    error_msg: string;
}

def handle_result(result: Result) {
    if result.success {
        println concat(str("Success: "), i32_to_string(result.value));
    } else {
        println concat(str("Error: "), result.error_msg);
    }
}
```

## Control Flow Best Practices

### 1. Minimize Nesting

```axe
//  Avoid deep nesting
if condition1 {
    if condition2 {
        if condition3 {
            do_something();
        }
    }
}

//  Use guard clauses
if !condition1 {
    return;
}
if !condition2 {
    return;
}
if !condition3 {
    return;
}
do_something();
```

### 2. Use Switch for Multiple Cases

```axe
//  Many if-elif chains
if type == 1 {
    handle_type_one();
} elif type == 2 {
    handle_type_two();
} elif type == 3 {
    handle_type_three();
}

//  Use switch
switch type {
    case 1 { handle_type_one(); }
    case 2 { handle_type_two(); }
    case 3 { handle_type_three(); }
}
```

### 3. Clear Loop Intent

```axe
//  Clear loop intention
for mut i = 0; i < items.len; i++ {
    val item: string = StringList.get(items, i);
    if should_skip(item) {
        continue;
    }
    process(item);
}
```

### 4. Parallel Loops Only Where Beneficial

```axe
//  Use parallel for CPU-intensive work
parallel for mut i = 0; i < 10000; i++ {
    val result: f64 = complex_math_operation(i);
    store_result(i, result);
}

//  Avoid for simple operations
parallel for mut i = 0; i < 10; i++ {
    println i;  // Too much overhead
}
```

## Performance Considerations

### Loop Unrolling

For simple, repetitive operations, the compiler may optimize loops:

```axe
// Compiler may optimize this
for mut i = 0; i < items.len; i++ {
    process_simple(items.data[i]);
}
```

### Parallel Loop Overhead

Parallel loops have overhead costs. Use them only when:

- Loop body is computationally intensive
- Number of iterations is sufficiently large (typically 100+)
- Data dependencies allow parallelization

### Break Performance

Breaking out of loops early can significantly improve performance:

```axe
//  Early termination for searches
for mut i = 0; i < large_array.len; i++ {
    if found_target(large_array.data[i]) {
        return i;  // Exit early
    }
}
```
