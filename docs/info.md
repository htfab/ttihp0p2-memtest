<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

Implements a 128 byte memory.
When `we` is high, `mem[addr]` is set to `data_in`.
When `we` is low, `data_out` is set to `mem[addr]` and `data_out_next` is set to `mem[addr+1]`.

## How to test

Either set the inputs manually and check the outputs or use the testbench from the `test` directory.

## External hardware

None
