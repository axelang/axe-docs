Differently from foreign types, opaque types generate a typedef in the generated C code.

An example of their usage:

```
platform posix {
    opaque { dirent };
    
    extern def opendir(name: ref char): usize;
    extern def readdir(dirp: usize): usize;
    extern def closedir(dirp: usize): i32;
    extern def stat(pathname: ref char, statbuf: usize): i32;

    def dirent_d_name(entry: usize): ref char {
        unsafe {
            val d: ref dirent = entry;
            return d*.d_name;
        }
    }

    def stat_is_dir(st: usize): i32 {
        unsafe {
            val sb: $(stat) = st;
            return C.S_ISDIR(sb*.st_mode);
        }
    }
}
```