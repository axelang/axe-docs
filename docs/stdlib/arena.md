# .\arena.axec

## pub def create(size: usize): Arena

Arena for memory allocation.Creates a new arena with the specified size.


## pub def destroy(arena: ref Arena)

Destroys the arena and frees its memory.

## pub def alloc(arena: ref Arena, size: usize): ref void

Allocates memory from the arena, returns a proper reference pointer.

## pub def alloc_array(arena: ref Arena, element_size: usize, count: usize): ref void

Allocates memory for an array from the arena.

## pub def reset(arena: ref Arena)

Resets the arena, clearing all allocated memory.

## pub def used(arena: ref Arena): i32

Returns the amount of memory used by the arena.

## pub def remaining(arena: ref Arena): usize

Returns the amount of remaining memory in the arena.
