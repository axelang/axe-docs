# Modules

Modules in Axe provide a mechanism for organizing code, managing dependencies, and controlling visibility. They establish clear boundaries between different parts of a program and enable code reuse.

## Module System Overview

Axe's module system is file-based with explicit imports. Each `.axe` or `.axec` file is a module, identified by its path relative to the project root.

```
project/
├─ main.axe              # module: main
├─ utils.axe             # module: utils
├─ src/
│  ├─ database.axe       # module: src.database
│  └─ api.axe            # module: src.api
└─ std/
   ├─ io.axec            # module: std.io
   ├─ string.axec        # module: std.string
   └─ lists.axec         # module: std.lists
```

### Module Naming Convention

Module names are derived from file paths:

- File: `src/utils/string_helpers.axe` → Module: `src.utils.string_helpers`
- File: `math.axe` → Module: `math`
- File: `std/io.axec` → Module: `std.io`

## Use Statements

Import modules and their exports with `use` statements:

```axe
// Import entire module
use std.io;

// Import specific symbols
use std.string (string, concat);

// Import from local module
use utils;

// Import multiple items
use std.lists (
    StringList,
    append,
    contains
);
```

### Use Statement Syntax

```
use <module_path> [( <symbol_list> )];
```

**Examples:**

```axe
// Import module (all public symbols available)
use std.io;
println("message");  // requires std.io.println

// Import specific symbols
use std.io (println);
println("message");  // can use directly

// Nested imports
use database (
    connect,
    disconnect,
    Connection
);

// Import from project module
use src.api (get_user, User);
```

## Public and Private Visibility

Use the `pub` keyword to make symbols public:

```axe
// Public: accessible from other modules
pub def calculate(x: i32, y: i32): i32 {
    return x + y;
}

pub model Point {
    x: i32;
    y: i32;
}

// Private: only accessible within this module
def internal_helper(): string {
    return str("internal");
}

model InternalState {
    data: string;
}
```

### Public Functions

```axe
/// Calculate the sum of two numbers
pub def add(a: i32, b: i32): i32 {
    return a + b;
}

/// Calculate the difference
pub def subtract(a: i32, b: i32): i32 {
    return a - b;
}

// Helper used only internally
def validate_numbers(a: i32, b: i32): bool {
    return a >= 0 and b >= 0;
}
```

### Public Models

```axe
/// Represents an HTTP response
pub model HttpResponse {
    status_code: i32;
    body: string;
    headers: string;
}

/// Internal cache structure
model CacheEntry {
    key: string;
    value: string;
    ttl: i32;
}
```

## Module Organization

### Single Responsibility

Each module should have a clear, focused purpose:

```
modules/
├─ http.axe           # HTTP request/response handling
├─ json.axe           # JSON encoding/decoding
├─ crypto.axe         # Cryptographic functions
├─ database.axe       # Database operations
└─ config.axe         # Configuration management
```

### File Structure

```axe
// mymodule.axe
// 1. File header with description
/// Module for managing user accounts
/// Handles authentication, profile management, and permissions

// 2. Use statements
use std.io;
use std.string;
use std.lists;

// 3. Public models and types
pub model User {
    id: i32;
    name: string;
    email: string;
    role: string;
}

pub model UserError {
    code: i32;
    message: string;
}

// 4. Internal types and globals
mut g_users: ref StringList;
mut g_max_id: i32 = 1000;

// 5. Public functions
pub def create_user(name: string, email: string): User {
    // implementation
}

pub def get_user(id: i32): User {
    // implementation
}

// 6. Private helper functions
def validate_email(email: string): bool {
    // implementation
}

def hash_password(password: string): string {
    // implementation
}

// 7. Tests
test {
    // test cases
}
```

## Creating Reusable Modules

### Module Library Structure

```
my_library/
├─ axe.mod                    # Module metadata
├─ README.md                  # Documentation
├─ src/
│  ├─ core.axe               # Core functionality
│  ├─ utils.axe              # Utilities
│  └─ api.axe                # Public API
└─ tests/
   ├─ test_core.axe
   └─ test_api.axe
```

### Example: Utility Module

```axe
/// src/utils.axe
/// Common utility functions

use std.string;
use std.io;

/// Check if a string is a valid email
pub def is_valid_email(email: string): bool {
    if find_substr(email, str("@")) < 0 {
        return false;
    }
    if find_substr(email, str(".")) < 0 {
        return false;
    }
    return true;
}

/// Trim whitespace from string
pub def trim_whitespace(s: string): string {
    mut start: i32 = 0;
    mut end: i32 = str_len(s) - 1;
    
    // Find first non-whitespace
    for mut i = 0; i < str_len(s); i++ {
        val ch: char = get_char(s, i);
        if ch != ' ' and ch != '\t' {
            start = i;
            break;
        }
    }
    
    // Find last non-whitespace
    for mut i = str_len(s) - 1; i >= 0; i = i - 1 {
        val ch: char = get_char(s, i);
        if ch != ' ' and ch != '\t' {
            end = i;
            break;
        }
    }
    
    return substring_se(s, start, end + 1);
}

/// Convert string to lowercase
pub def to_lower(s: string): string {
    mut result: string = str("");
    for mut i = 0; i < str_len(s); i++ {
        val ch: char = get_char(s, i);
        if ch >= 'A' and ch <= 'Z' {
            result = concat_c(result, ch + 32);
        } else {
            result = concat_c(result, ch);
        }
    }
    return result;
}

test {
    assert is_valid_email(str("user@example.com")), "Valid email";
    assert !is_valid_email(str("invalid-email")), "Invalid email";
}
```

### Usage of Module

```axe
// main.axe
use src.utils (is_valid_email, to_lower, trim_whitespace);
use std.io (println);

def main() {
    val email: string = str("User@Example.Com");
    
    if is_valid_email(email) {
        val lower: string = to_lower(email);
        println lower;
    }
}
```

## Dependency Management

### Using axe.mod

The `axe.mod` file declares module metadata and dependencies:

```yaml
name: my-project
version: 0.1.0
entry: main.axe
license: MIT
description: Example Axe project

dependency: https://github.com/axelang/stdlib.git@abc1234
dependency: https://github.com/user/utils.git@def5678
```

### Importing Dependencies

```axe
use std.io;              // Standard library module
use my_utils;           // Local module
use external_lib (
    exported_function,
    ExportedType
);
```

## Module Best Practices

### 1. Minimize Public API

```axe
// Good: Small, focused public interface
pub def process(data: string): string {
    return do_internal_processing(data);
}

// Internal implementation details
def do_internal_processing(data: string): string {
    // complex logic
}

// Poor: Everything is public
pub def process(data: string): string { }
pub def internal_step_1(data: string): string { }
pub def internal_step_2(data: string): string { }
pub def internal_step_3(data: string): string { }
```

### 2. Document Public API

```axe
/// Process user input and return formatted result
/// 
/// Args:
///   input: raw user input string
///   
/// Returns:
///   formatted result string
///   
/// Errors:
///   Returns empty string if input is invalid
pub def process_input(input: string): string {
    if str_len(input) == 0 {
        return str("");
    }
    // implementation
}
```

### 3. Use Consistent Naming

```axe
// Good: Consistent, clear naming
pub def create_connection(host: string): Connection { }
pub def close_connection(conn: Connection): bool { }
pub def send_data(conn: Connection, data: string): bool { }

// Poor: Inconsistent naming
pub def new_conn(host: string): Connection { }
pub def kill_link(conn: Connection): bool { }
pub def transmit(conn: Connection, data: string): bool { }
```

### 4. Avoid Circular Dependencies

```
// Good: Acyclic dependency graph
core → utils → api → main
  ↓
  services

// Bad: Circular dependencies
core ↔ utils
api ↔ main
utils ↔ api
```

### 5. Group Related Functionality

```axe
//  Good: Related functions in one module
pub def create_user(name: string): User { }
pub def delete_user(id: i32): bool { }
pub def get_user(id: i32): User { }
pub def list_users(): ref StringList { }

//  Poor: Scattered related functionality
// database.axe
pub def execute_query(query: string): string { }

// user.axe
pub def create_user(name: string): User { }

// auth.axe
pub def get_user(id: i32): User { }
```

## Module Import Patterns

### Selective Imports

```axe
// Import only what you need
use std.string (concat, substr);
use std.io (println);

def process() {
    val result: string = concat(str("hello"), str(" world"));
    println result;
}
```

### Wildcard Imports

```axe
// Import all public symbols (use sparingly)
use std.io;

def process() {
    println "Using all io symbols";
}
```

### Nested Module Imports

```axe
use database.models (User, Post);
use database.queries (find_user, list_posts);

def load_user_posts(user_id: i32) {
    val user: User = find_user(user_id);
    val posts: ref StringList = list_posts(user_id);
}
```

## Common Module Patterns

### Facade Pattern

A module that simplifies access to complex subsystems:

```axe
//  Good: Simple public interface hides complexity
pub def initialize_app(config_path: string): bool {
    // Internally calls many setup functions
    if !load_config(config_path) { return false; }
    if !init_database() { return false; }
    if !init_cache() { return false; }
    if !load_plugins() { return false; }
    return true;
}

// Internal complexity hidden
def load_config(path: string): bool { }
def init_database(): bool { }
def init_cache(): bool { }
def load_plugins(): bool { }
```

### Repository Pattern

Encapsulate data access logic:

```axe
pub model User {
    id: i32;
    name: string;
    email: string;
}

pub def find_user(id: i32): User {
    // Database query logic
}

pub def save_user(user: User): bool {
    // Database insert/update logic
}

pub def delete_user(id: i32): bool {
    // Database delete logic
}

// Internal query building
def build_query(id: i32): string { }
def execute_query(query: string): string { }
```
