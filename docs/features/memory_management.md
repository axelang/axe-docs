# Memory Management with Arenas

Arenas provide the primary mechanism for memory management in Axe. They allow efficient allocation of memory in large contiguous blocks, which can then be used for temporary or long-lived data without relying on a garbage collector. This approach is especially useful for high-performance applications, such as parsing, string manipulation, or batch allocation of objects.

## Overview

An Arena is a memory pool that manages a pre-allocated buffer. Memory requests are fulfilled sequentially from this buffer, and allocations are aligned to 8-byte boundaries for efficiency. Unlike traditional heap allocations, individual memory blocks are not freed manually. Instead, the entire arena can be reset or destroyed when the memory is no longer needed.

Arenas are particularly suited for scenarios where the lifetime of many objects is similar. For example, when parsing a CSV document, all rows and fields can be allocated from the same arena and released together, avoiding the overhead of multiple heap allocations.

## Creating and Destroying Arenas

To use an Arena, you first create it with a specified size. The size indicates how much memory the arena will manage. Internally, Axe multiplies the requested size by 100 to ensure sufficient space for allocations.

```axe
mut arena: Arena = Arena.create(65536)
```

Once the arena is no longer needed, it can be destroyed to release its memory back to the system.

```axe
Arena.destroy(addr(arena))
```

Destroying an arena sets its buffer pointer, offset, and capacity to zero, preventing accidental use after destruction.

## Allocating Memory

Arenas provide a general-purpose allocation function that returns a pointer to a memory block of the requested size. If the requested size exceeds the remaining capacity of the arena, the allocation fails and triggers a panic.

```axe
mut buffer: ref void = Arena.alloc(addr(arena), 1024)
```

Allocations are aligned to 8-byte boundaries automatically, which ensures correct memory alignment for most data types.

For array allocations, there is a convenience function that multiplies the element size by the number of elements:

```axe
mut array: ref void = Arena.alloc_array(addr(arena), sizeof[int], 100)
```

This simplifies allocation for structured data like lists, matrices, or string buffers.

## Resetting Memory

An Arena can be reset at any time, which clears all allocations without deallocating the buffer. This is useful for reusing the arena across multiple tasks without repeatedly creating and destroying arenas.

```axe
Arena.reset(addr(arena))
```

Resetting sets the offset back to zero and fills the buffer with zeroes. All previously allocated memory is considered invalid after a reset.

## Tracking Usage

Arenas allow inspection of memory usage through two functions: `used` and `remaining`.

```axe
val used_memory: i32 = Arena.used(addr(arena))
val remaining_memory: usize = Arena.remaining(addr(arena))
```

`used` returns the total bytes allocated so far, while `remaining` indicates how much memory is left in the arena. These functions can be useful for debugging or monitoring memory usage in performance-critical applications.

## Example: CSV Parsing with Arenas

A common pattern in Axe is to parse structured data using arenas. For instance, converting a CSV document into a string can be done entirely within an arena:

```axe
mut result_data: ref char = Arena.alloc(doc.arena, estimated_size)
```

In this pattern, all intermediate allocations for rows and fields are made from the arena, and memory is released only when the arena itself is destroyed. This approach avoids repeated heap allocations and improves performance in large datasets.

## Safety Considerations

While arenas simplify memory management, they require careful use of references. Accessing memory outside the arena's allocated range, or using a reference after the arena has been reset or destroyed, leads to undefined behavior.

Using arenas is especially compatible with unsafe blocks in Axe, which allow direct memory manipulation while maintaining performance. However, it is recommended to encapsulate arena allocations in safe abstractions wherever possible, as demonstrated in CSV parsing or string handling functions.

