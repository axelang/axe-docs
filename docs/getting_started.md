# Getting Started

To get started, simply extract the zip archive from the GitHub releases page, and add the "saw" and "axe" executables to your PATH.

Saw is a build tool for Axe, similar to Cargo for Rust, or Alire for Ada.

If you wanted to initialize a new axe project, you would start by running:

```
$ saw init
```

Which would initialize a new axe.mod file. Dependencies can be added via `saw add`, and removed via `saw remove`, moreover, information about the Axe module in the current working directory can be discovered via the `saw info` command.

Further information on the Saw CLI can be found via looking at the --help page in the CLI itself.