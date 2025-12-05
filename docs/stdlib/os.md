# .\os.axec

## def dirent_d_name(entry: usize): char*

Execute a shell command. Returns exit status.Execute a shell command with raw C string.
Returns exit status.
Execute a shell command and capture stdout/stderr output.
Returns exit status and output string.
Execute a shell command and capture stdout/stderr output.

Returns exit status and output string.
Quit with some code.
Check if a file exists.
Read entire file into a newly allocated string.
Write a string to a file, replacing its contents.
Returns true on success.
Determine if a path is a directory.
Determine if a path is a regular file.
Determine if a path is a symbolic link.
This always returns false on Windows.
Delete a file.
Delete some directory. It must be empty.


## def stat_is_dir(st: usize): i32

## def finddata_name(data: usize): char*

## def finddata_is_dir(data: usize): i32

## def stat_is_reg(st: usize): i32

Delete some directory, it does NOT have to be empty.Use with caution.

