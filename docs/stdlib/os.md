# .\os.axec

## pub def exec_from_string(cmd: string): i32

Execute a shell command. Returns exit status.

## pub def exec(cmd: ref char): i32

Execute a shell command with raw C string.Returns exit status.


## pub def exec_capture(cmd: string): ExecResult

Execute a shell command and capture stdout/stderr output.Returns exit status and output string.
Execute a shell command and capture stdout/stderr output.

Returns exit status and output string.


## pub def quit(code: i32)

Quit with some code.

## pub def file_exists(path: string): bool

Check if a file exists.

## pub def read_file(path: string): string

Read entire file into a newly allocated string.

## pub def write_file(path: string, contents: string): bool

Write a string to a file, replacing its contents.Returns true on success.


## pub def is_directory(path: string): bool

Determine if a path is a directory.

## pub def is_file(path: string): bool

Determine if a path is a regular file.

## pub def is_symbolic_link(path: string): bool

Determine if a path is a symbolic link.This always returns false on Windows.


## pub def delete_file(path: string): bool

Delete a file.

## pub def rm_dir(path: string): bool

Delete some directory. It must be empty.

## def dirent_d_name(entry: usize): ref char

## def stat_is_dir(st: usize): i32

## def finddata_name(data: usize): ref char

## def finddata_is_dir(data: usize): i32

## pub def rm_dir_recursive(path: string): bool

Delete some directory, it does NOT have to be empty.Use with caution.


## def stat_is_reg(st: usize): i32

## pub def collect_files_recursive(path: string, result: ref StringList, arena: ref Arena)

Internal helper to collect files recursively into a StringList.

## pub def list_files_recursive(path: string, arena: ref Arena): ref StringList

List all regular files recursively under `path`.

## pub def get_user_home_dir(): string

Get the user's home directory

## pub def get_env(name: string): string

Get an environment variable by name

## pub def get_cmdline_args(arena: ref Arena): ref StringList

Get commandline args

## pub def get_cwd(): string

## pub def get_executable_path(): string

Get the path to the currently running executable

## pub def get_executable_dir(): string

Get the directory containing the currently running executable

## pub def get_short_filename(path: string): string

Extracts the filename from a path string.
Handles both forward and backward slashes.

