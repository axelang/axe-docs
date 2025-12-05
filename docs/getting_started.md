# Getting Started

To get started, simply extract the zip archive from the GitHub releases page, and add the "saw" and "axe" executables to your PATH.

Saw is a build tool for Axe, similar to Cargo for Rust, or Alire for Ada.

If you wanted to initialize a new axe project, you would start by running:

```
$ saw init
```

Which would initialize a new axe.mod file. Dependencies can be added via `saw add`, and removed via `saw remove`, moreover, information about the Axe module in the current working directory can be discovered via the `saw info` command.

Further information on the Saw CLI can be found via looking at the --help page in the CLI itself.

To run an Axe program on its own, without project scaffolding, one can use the `axe` CLI, which is the Axe compiler itself.

To do this, simply create an Axe file, for example, `hello_world.axe`, and write some program into it:

```axe
use std.io;

def main() {
    println "Hello, world.";
}
```

Then save it, and run:

```
$ axe hello_world
```

With or without the .axe extension, the Axe compiler will infer, and the file will be found, compiled, and made executable. The executable will have the same base name as the source file.