Windows
-------

### Getting a core dump

If xemu is crashing and the reason is not clear, you can create a core dump to provide developers with to investigate. To create a core dump on Windows for crash analysis:

First, apply the registry edit script found in this Zip file: [xemu_dump_registry_config.zip](https://xemu.app/xemu_dump_registry_config.zip). This registry edit will configure Windows to create a dump whenever xemu crashes.

Then, download and run the debug build of xemu found at: https://github.com/xemu-project/xemu/releases/latest/download/xemu-win-debug.zip

The dump will be stored at `%LOCALAPPDATA%\CrashDumps`. You may notice a delay after xemu crashes while this file is saved.
