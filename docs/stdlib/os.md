# .\os.axec

## def exec_from_string(cmd: string): i32

Execute a shell command. Returns exit status.

## def exec(cmd: char*): i32

Execute a shell command with raw C string.Returns exit status.


## def file_exists(path: string): bool

Check if a file exists.

## def read_file(path: string): string

Read entire file into a newly allocated string.

## def write_file(path: string, contents: string): bool

Write a string to a file, replacing its contents.Returns true on success.


## def is_directory(path: string): bool

Determine if a path is a directory.

## def is_file(path: string): bool

Determine if a path is a regular file.

## def is_symbolic_link(path: string): bool

Determine if a path is a symbolic link.This always returns false on Windows.


## def delete_file(path: string): bool

Delete a file.

## def rm_dir(path: string): bool

Delete some directory. It must be empty.

## def rm_dir_recursive(path: string): bool

Delete some directory, it does NOT have to be empty.Use with caution.


## def collect_files_recursive(path: string, result: ref StringList, arena: ref Arena)

Internal helper to collect files recursively into a StringList.

## def list_files_recursive(path: string, arena: ref Arena): ref StringList

List all regular files recursively under `path`.

## def get_cmdline_args(arena: ref Arena): ref StringList

Get commandline args
