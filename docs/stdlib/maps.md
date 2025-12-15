# .\maps.axec

## pub def create(arena: ref Arena, capacity: i32): ref mapname

Generic Map using memcmp for key comparison

## pub def clear(map: ref mapname)

## pub def append(map: ref mapname, arena: ref Arena, key: keytype_elem, value: valtype_elem)

## pub def add(map: ref mapname, arena: ref Arena, key: keytype_elem, value: valtype_elem)

## pub def set(map: ref mapname, arena: ref Arena, key: keytype_elem, value: valtype_elem)

## pub def get(map: ref mapname, key: keytype_elem): valtype_elem

## pub def contains(map: ref mapname, key: keytype_elem): bool

## pub def size(map: ref mapname): i32

## pub def pop(map: ref mapname, key: keytype_elem): valtype_elem

## pub def create(arena: ref Arena, capacity: i32): ref mapname

Generic StringHashMap with proper string comparison

## pub def clear(map: ref mapname)

## pub def add(map: ref mapname, arena: ref Arena, key: string, value: valtype_elem)

## pub def set(map: ref mapname, arena: ref Arena, key: string, value: valtype_elem)

## pub def get(map: ref mapname, key: string): valtype_elem

## pub def contains(map: ref mapname, key: string): bool

## pub def size(map: ref mapname): i32

## pub def pop(map: ref mapname, key: string): valtype_elem
