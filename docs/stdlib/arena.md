# .\arena.axec

## model Arena

Arena for memory allocation.

## def create(size: i32): Arena

Creates a new arena with the specified size.

## def destroy(arena: ref Arena)

Destroys the arena and frees its memory.

## def alloc(arena: ref Arena, size: i32): ref void

Allocates memory from the arena, returns a proper reference pointer.

## def alloc_array(arena: ref Arena, element_size: i32, count: i32): ref void

Allocates memory for an array from the arena.

## def reset(arena: ref Arena)

Resets the arena, clearing all allocated memory.

## def used(arena: ref Arena): i32

Returns the amount of memory used by the arena.

## def remaining(arena: ref Arena): i32

Returns the amount of remaining memory in the arena.
