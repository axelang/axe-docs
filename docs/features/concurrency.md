# Concurrency

Axe provides straightforward concurrency support through parallel loops and OpenMP integration, enabling CPU-bound parallelism without explicit thread management or complex synchronization primitives.

## Parallel For Loops

The `parallel for` construct executes loop iterations in parallel across multiple CPU cores:

```axe
use std.arena (Arena);
use std.lists (StringList);

def process_items_parallel(items: ref StringList) {
    val count: i32 = len(deref(items));
    
    parallel for mut i = 0; i < count; i++ {
        val item: string = StringList.get(items, i);
        val result: string = expensive_operation(item);
        store_result(i, result);
    }
}
```


```axe
use std.arena (Arena);

def matrix_multiply(matrix_a: ref i32, matrix_b: ref i32, size: i32): ref i32 {
    mut result: Arena = Arena.create(size * size * 4);
    mut result_data: i32* = result.data;
    
    parallel for mut i = 0; i < size; i++ {
        for mut j = 0; j < size; j = j + 1 {
            mut sum: i32 = 0;
            for mut k = 0; k < size; k = k + 1 {
                sum = sum + (matrix_a[i * size + k] * matrix_b[k * size + j]);
            }
            result_data[i * size + j] = sum;
        }
    }
    
    return result_data;
}
```

## Parallel Patterns

### Data Parallelism

Distribute independent computations across loop iterations:

```axe
use std.lists (StringList);

def transform_all(items: ref StringList): ref StringList {
    val count: i32 = len(deref(items));
    
    parallel for mut i = 0; i < count; i++ {
        val original: string = StringList.get(items, i);
        val transformed: string = transform_string(original);
        store_transformed(i, transformed);
    }
}
```

**Characteristics:**
- Each iteration processes independent data
- No dependencies between iterations
- Perfect parallelization
- Minimal synchronization overhead

### Reduction Operations

Combine results from parallel iterations:

```axe
def sum_array_parallel(data: ref i32, size: i32): i32 {
    mut total: i32 = 0;
    
    // Note: Axe doesn't have built-in reduction syntax
    // Use atomic updates or post-merge aggregation
    parallel for mut i = 0; i < size; i++ {
        // Each thread computes partial sums
        mut partial_sum: i32 = 0;
        for mut j = i; j < size; j = j + 10 {
            partial_sum = partial_sum + data[j];
        }
        total = total + partial_sum;  // Potential race condition!
    }
    
    return total;
}
```

**Better approach - compute partials then merge:**

```axe
use std.arena (Arena);

def sum_array_safe(data: ref i32, size: i32): i32 {
    val num_threads: i32 = 4;  // Approximate
    mut partials: Arena = Arena.create(num_threads * 4);
    mut partial_sums: i32* = partials.data;
    
    parallel for mut i = 0; i < num_threads; i++ {
        mut sum: i32 = 0;
        val start: i32 = i * (size / num_threads);
        val end: i32 = start + (size / num_threads);
        for mut j = start; j < end; j = j + 1 {
            sum = sum + data[j];
        }
        partial_sums[i] = sum;
    }
    
    // Merge partials sequentially
    mut total: i32 = 0;
    for mut i = 0; i < num_threads; i++ {
        total = total + partial_sums[i];
    }
    
    Arena.destroy(addr(partials));
    return total;
}
```

### Parallel Local Variables

Use `parallel local` to declare thread-local variables:

```axe
def worker(arena: ref Arena, value: i32): i32 {
    mut p: ref i32 = (ref i32)Arena.alloc(arena, sizeof(i32));
    deref(p) = value * value;
    return deref(p);
}

def main() {
    println "Running parallel computation...";

    parallel local(mut arena: Arena) {
        arena = Arena.create(1024);
        val tid: i32 = Parallel.thread_id();
        val result: i32 = worker(addr(arena), tid);
        println $"Thread {tid} computed {result}";
        Arena.destroy(addr(arena));
    }

    println "Done.";
}
```

## Performance Considerations

### When to Use Parallel Loops

Use parallel loops when:

1. **Computation is CPU-intensive**
   ```axe
   //  Good: Expensive computation
   parallel for mut i = 0; i < 10000; i++ {
       val result: f64 = fibonacci(40 + i);
       store_result(i, result);
   }
   ```

2. **Number of iterations is large (100+)**
   ```axe
   //  Good: Sufficient work to amortize threading overhead
   parallel for mut i = 0; i < 100000; i++ {
       process_item(i);
   }
   
   //  Bad: Too few iterations
   parallel for mut i = 0; i < 10; i++ {
       println i;  // Overhead exceeds benefit
   }
   ```

3. **Iterations are independent**
   ```axe
   //  Good: No dependencies
   parallel for mut i = 0; i < size; i++ {
       data[i] = data[i] * 2;  // Independent writes
   }
   
   //  Bad: Iteration-dependent
   parallel for mut i = 1; i < size; i++ {
       data[i] = data[i-1] + data[i];  // Each depends on previous
   }
   ```

### Overhead Costs

Thread pool creation and synchronization have costs:

```
Sequential:    0         50ms       100ms
               |----------|----------|
               
Parallel (4x): 5ms  work  work  work  sync
               |---|------|------|------|
               overhead                
               
Total: ~110ms (overhead + sync can exceed sequential benefits)
```

**Minimize Overhead:**

```axe
//  Good: Amortize threading overhead with large workload
parallel for mut i = 0; i < 1000000; i++ {
    val result: f64 = complex_calculation(i);
    store_result(i, result);
}

//  Bad: Overhead dominates
parallel for mut i = 0; i < 20; i++ {
    val x: i32 = i * 2;
    println i32_to_string(x);
}
```

### Memory Coherence

Ensure threads don't interfere via memory:

```axe
//  Bad: False sharing and cache coherence issues
parallel for mut i = 0; i < 1000000; i++ {
    shared_counter = shared_counter + 1;  // Race condition!
}

//  Good: Independent memory access
parallel for mut i = 0; i < 1000000; i++ {
    result[i] = compute(i);  // Each thread touches different memory
}
```

## Common Patterns

### Image Processing

Process image data in parallel:

```axe
use std.arena (Arena);

def apply_filter(image: ref i32, width: i32, height: i32, filter: ref i32) {
    val size: i32 = width * height;
    
    parallel for mut i = 0; i < size; i++ {
        val pixel: i32 = image[i];
        val filtered: i32 = apply_kernel(pixel, i, width, height, filter);
        image[i] = filtered;
    }
}
```

### Scientific Computing

Distribute numerical computations:

```axe
use std.arena (Arena);

def monte_carlo_pi(samples: i32): f64 {
    mut inside: i32 = 0;
    
    parallel for mut i = 0; i < samples; i++ {
        val x: f64 = random_float();
        val y: f64 = random_float();
        val distance_sq: f64 = x * x + y * y;
        
        if distance_sq <= 1.0 {
            inside = inside + 1;
        }
    }
    
    return 4.0 * cast[f64](inside) / cast[f64](samples);
}
```

### Batch Processing

Process items in batches across threads:

```axe
use std.lists (StringList);

def process_file_list(files: ref StringList) {
    val count: i32 = len(deref(files));
    
    parallel for mut batch = 0; batch < count; batch = batch + 10 {
        val end: i32 = batch + 10;
        val limit: i32 = if end > count { count } else { end };
        
        for mut i = batch; i < limit; i++ {
            val filename: string = StringList.get(files, i);
            process_file(filename);
        }
    }
}
```

## Thread Safety

### Safe Operations

These operations are safe in parallel loops:

```axe
//  Safe: Reading shared data
parallel for mut i = 0; i < size; i++ {
    val value: i32 = read_only_data[i];
    compute(value);
}

//  Safe: Independent writes
parallel for mut i = 0; i < size; i++ {
    output[i] = input[i] * 2;
}

//  Safe: Thread-local state
parallel local {
    mut thread_state: i32 = 0;
}
parallel for mut i = 0; i < size; i++ {
    thread_state = thread_state + 1;  // Each thread has own copy
}
```

### Unsafe Operations

Avoid these in parallel loops:

```axe
//  Unsafe: Unsynchronized shared writes
parallel for mut i = 0; i < size; i++ {
    counter = counter + 1;  // Race condition
}

//  Unsafe: Data dependencies between iterations
parallel for mut i = 1; i < size; i++ {
    data[i] = data[i-1] + input[i];  // Depends on previous iteration
}

//  Unsafe: Potential deadlock
parallel for mut i = 0; i < size; i++ {
    mutex_lock();  // Could deadlock with thread pool
    shared_list.add(i);
    mutex_unlock();
}
```

## Compiler Support

### Detection

The Axe compiler automatically detects parallel constructs:

```axe
// Compiler analyzes AST for:
// - parallel for loops
// - parallel local blocks
// - Imports of std.parallelism

def has_parallel_constructs() {
    parallel for mut i = 0; i < 100; i++ {
        compute(i);
    }
}
```

### Linking

When parallel constructs are detected:

```
1. Compile C code with parallel directives
2. Detect usage in AST
3. Add -fopenmp flag to clang
4. Link against system OpenMP library
```

## Best Practices

### 1. Profile Before Parallelizing

```axe
//  Good: Only parallelize after profiling shows bottleneck
def slow_operation() {
    // Profile shows this loop is 80% of execution time
    // Parallelization reduces it to 25% - worthwhile
    parallel for mut i = 0; i < 1000000; i++ {
        expensive_computation(i);
    }
}
```

### 2. Keep Loop Bodies Simple

```axe
//  Good: Simple, focused operations
parallel for mut i = 0; i < size; i++ {
    result[i] = input[i] * factor;
}

//  Poor: Complex operations with many branches
parallel for mut i = 0; i < size; i++ {
    if complex_condition(i) {
        val x: i32 = compute_x(i);
        val y: i32 = compute_y(i);
        val z: i32 = compute_z(x, y, i);
        store_result(i, z);
    }
}
```

### 3. Test Correctness First

```axe
//  Good: Test sequential version first
def compute_sequential() {
    for mut i = 0; i < size; i++ {
        result[i] = expensive_operation(i);
    }
}

// Then parallelize after correctness is verified
def compute_parallel() {
    parallel for mut i = 0; i < size; i++ {
        result[i] = expensive_operation(i);
    }
}
```

## Limitations and Future Directions

### Current Limitations

- No explicit synchronization primitives (locks, semaphores)
- Limited control over thread pool size
- No work stealing or task scheduling
- Parallel loops only for data parallelism

### Future Enhancements

- Task-based parallelism
- Custom thread pool configuration
- Fine-grained synchronization primitives
- GPU acceleration support

## See Also

- [Control Flow](control_flow.md) - Loop structures
- [Error Handling](error_handling.md) - Error handling in parallel contexts
- [Modules](modules.md) - std.parallelism module
