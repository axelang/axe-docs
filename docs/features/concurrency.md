# Concurrency

Axe provides straightforward concurrency support through various parallel constructs, enabling CPU-bound parallelism without explicit thread management or complex synchronization primitives.

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
    mut result_data: ref i32 = result.data;
    
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


### Reduction Operations

Below is a clean, documentation-style explanation of what this Axe code does and how each construct behaves.

---

### **Example: Parallel Loop With Reduction**

This example demonstrates how to use a **parallel `for` loop** with a **reduction** operation in Axe. A reduction allows multiple parallel iterations to safely update a shared variable using an associative operator—such as `+`—without causing data races.


```axe
use std.io;

def main() {
    println "Testing parallel for with reduction:";
    
    mut sum: i32 = 0;
    mut n: i32 = 100;
    
    parallel for mut i = 0 to n reduce(+:sum) {
        sum += i;
    }
    
    println "Sum from 0 to 99 = ";
    println sum;
    println "Expected: 4950";
}
```

### **Parallel Loop**

```axe
parallel for mut i = 0 to n reduce(+:sum) {
    sum += i;
}
```

This construct launches a **parallelized** loop:

* `mut i = 0 to n`
  Creates a loop variable `i` that iterates from `0` to `n - 1`.

* `parallel for`
  Instructs the runtime to distribute iterations across multiple threads or processing units.

* `reduce(+:sum)`
  Specifies a **reduction clause**, telling the compiler that:

  * Each thread should maintain its own local copy of `sum`.
  * The `+` operator is used to combine those local values at the end.
  * The final combined value is written back into the shared `sum` variable.

This ensures that the operation is thread-safe and deterministic, even though the loop body runs in parallel.

#### Loop Body

```axe
sum += i;
```

Each iteration contributes the current index `i` to the thread-local accumulator.

### **Output**

After all parallel iterations are completed and the reduction is applied, the program prints:

* The computed sum (`sum`)
* The expected value for validation: `4950`
  (the sum of integers from `0` to `99`)

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

## Notes

### Profile Before Parallelizing

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

### Test Correctness First

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

### Future Enhancements

- Task-based parallelism
- Custom thread pool configuration
- Fine-grained synchronization primitives
- GPU acceleration support
- Further explicit synchronization primitives
- More control over thread pool size
- Work stealing and task scheduling
