The xemu source tree can be quite intimidating at first due to its qemu roots, but the majority of Xbox-specific code is confined to the `xemu/hw/xbox/` folder where the rest can be disregarded.

The basic principles are to emulate an original Xbox system at the hardware level via qemu intercepting memory-mapped IO (MMIO) intended for devices and re-implementing functionality as close to the original as possible. In the case of the NV2A GPU, these MMIO get translated to equivalent OpenGL instructions.

Debug builds can be created by appending `--debug` to the build command arguments.