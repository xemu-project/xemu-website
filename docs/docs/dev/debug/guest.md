To debug Xbox executables themselves, enable the guest GDB server within xemu by appending `-s` to the startup commands and optionally appending `-S` to start in a paused state; this will listen on `localhost` port `1234` by default.

## Monitor

Qemu's monitor can be accessed via the backtick shortcut on your keyboard or via <kbd>Debug</kbd> &rarr; <kbd>Monitor</kbd> from within the xemu menu. It's not required to enable the GDB server to use.

To quickly diagnose a crash in guest code, one might execute the following GDB commands:

- Dump the CPU state via `info registers` to determine `EIP`
- Disassemble 20 instructions at a virtual address via `x/20i 0xADDRESS`
- Dump 100 bytes of memory from a virtual address via `x/100 0xADDRESS`

<!--
## GDB

TODO: WIP

## Ghidra

#### Installation

[Use](https://github.com/mborgerson/ghidra-xbe#how-to-install){target=_blank} the [xbe-loader extension](https://github.com/mborgerson/ghidra-xbe/){target=_blank} to load the target XBE into [Ghidra](https://github.com/NationalSecurityAgency/ghidra){target=_blank}.

#### Connect Debugger

From the Ghidra menu, navigate to <kbd>Tools</kbd> &rarr; <kbd>Run Tool</kbd> &rarr; <kbd>Debugger</kbd>, then from within the Debugger, go to <kbd>File</kbd> &rarr; <kbd>Open</kbd> and open the XBE.

TODO: WIP

-->

## IDA (Windows)

#### Load Binaries (Optional)

Open the target binary in IDA. Multiple binaries (mcpx, 1bl, 2bl, kernel, xbe) can be loaded via <kbd>File</kbd> &rarr; <kbd>Load file</kbd> &rarr; <kbd>Additional binary file...</kbd> in the case you wish to observe the full boot process.

#### Connect Debugger

In the IDA menu, go to <kbd>Debugger</kbd> &rarr; <kbd>Attach</kbd> &rarr; <kbd>Remote GDB Debugger</kbd> and specify `localhost` on port `1234`.

Underneath <kbd>Debug options</kbd> &rarr; <kbd>Set specific options</kbd> &rarr; <kbd>Memory map</kbd>, right-click <kbd>Insert</kbd> and specify `FFFFFFFE` (limitation if using the x86 version) for the end address, then click <kbd>OK</kbd> 5 times to save.

## Debug Defines

The following debug defines may be of interest when building; they'll print additional information to the console window.

#DEFINE | Source File | Purpose
--- | --- | ---
DEBUG_NV2A | hw/xbox/nv2a/debug.h | Graphics
DEBUG_NV2A_FEATURES | hw/xbox/nv2a/debug.h | Graphics
DEBUG_SMBUS | hw/i2c/smbus_slave.c | HAL
DEBUG_CUSB | hw/xbox/chihiro-usb.c | Input
DEBUG_XID | hw/xbox/xid.c | Input
DEBUG_MCPX | hw/xbox/mcpx/apu.c | Audio
DEBUG_DSP | hw/xbox/mcpx/dsp/dsp.c | Audio


## Tracing

A more advanced version of logging can be accomplished via qemu's tracing infrastructure. Review the `trace-events` files within the source tree to see what's supported. See also [QEMU user documentation](https://qemu-project.gitlab.io/qemu/devel/tracing.html){target=_blank} for more details.

#### Runtime Usage (preferred)

Launch xemu from a console window (cmd.exe, Terminal.app, bash, etc...; whichever is appropriate for your OS).

Open the monitor via <kbd>Debug</kbd> &rarr; <kbd>Monitor</kbd> in the xemu menu.

Enter `trace-event <trace_event> on` to turn on an event, `trace-event <trace_event> off` to turn one off, replacing `<trace_event>` with the name of the event you wish to toggle.

Examine the console where you launched xemu; trace messages will be written to `STDERR`.

The [nv2a events](https://github.com/xemu-project/xemu/blob/master/hw/xbox/nv2a/trace-events){target=_blank} are particularly interesting when debugging graphics issues, specifically the `nv2a_pgraph_*` subset. These may be toggled all at once using a wildcard. For example, `trace-event nv2a_pgraph_* on` will turn them all on.

### Writing Outputs of Traces to Files

Most shells have functions that allow you to control where the output streams `STDERR` or `STDOUT` are written to. Normally, they're written to the shell window, but by using certain flags, we're able to write them to files. Doing this can allow you to easily share `trace-event` logs with other developers or testers. 

!!! info "Info: Regarding examples"
    
    The following examples will show you how to route both `STDERR` **and** `STDOUT` to a file; 
    if you wish to write just one of the streams to a file, we recommend you reference 
    Output Redirection within your shell's documentation.

=== "Windows"

    With `cmd.exe`...

    `xemu.exe>output.log 2>&1`

    Command starts xemu.exe and routes `STDOUT` (`>`) to output.log; `STDERR` is redirected to `STDOUT` (`2>&1`).


    With `Powershell`...

    `Start-Process -FilePath ".\xemu.exe" -RedirectStandardOutput "output_std.log" -RedirectStandardError "output_err.log"`
    
    Command starts xemu.exe and routes output streams separately.

=== "macOS"

    With `zsh` (macOS default since 2019)...

    `./xemu.app/Contents/MacOS/xemu &> output.log`

    Command executes the binary inside of the package (`./xemu.app/Contents/MacOS/xemu`) and routes all output streams (`&>`) to output.log.

=== "Linux"

    With `zsh`/`bash`/`fish`...

    `./xemu.AppImage &> output.log`
    
    Command executes the AppImage (`./`) and routes all output streams (`&>`) to output.log.

#### Compile-Time Usage (alternate)

Append `--debug --enable-trace-backends=simple` to the xemu build args to enable.

Edit the global `/tmp/events` file with things you intend to match on.

    $ rm /tmp/events
    $ echo cd_read_sector* >> /tmp/events
    $ echo ide_* >> /tmp/events
    $ echo ide_atapi_* >> /tmp/events
    $ echo ahci* >> /tmp/events
    $ cat /tmp/events

Then append `--trace events=/tmp/events` to the xemu runtime arguments. Once finished, run `python ./scripts/simpletrace.py trace-events-all trace-####` replacing `####` with the created trace log's ID.
