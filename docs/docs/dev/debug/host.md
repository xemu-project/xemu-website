Stepping through xemu's code for development or troubleshooting an issue can be done via the process outlined below. Note that any GDB-based debugger should do, but [VSCode's](https://code.visualstudio.com/docs/cpp/cpp-debug){target=_blank} ease of use and multi-platform capabilities make it a good starter.

## Setup

Install [VSCode](https://code.visualstudio.com/download){target=_blank} and the [ms-vscode.cpptools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools){target=_blank} extension.

=== "Windows"

    Map a drive to the WSL2 root or your projects folder within. The particular path can be found by viewing `\\wsl$` in File Explorer and reviewing the folders (distros) underneath. For example, `net use w: \\wsl$\Ubuntu-20.04`.

    Install [MSYS2](https://www.msys2.org/){target=_blank}, run the `MSYS2 MinGW 64-bit` shell, and install GDB.

        $ pacman -S mingw-w64-x86_64-gdb

    Create a file at `xemu\.vscode\launch.json` with the following contents.

    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "(gdb) Launch",
                "type": "cppdbg",
                "request": "launch",
                "program": "${workspaceFolder}\\dist\\xemu.exe",
                "args": [],
                "stopAtEntry": false,
                "cwd": "${workspaceFolder}\\dist",
                "environment": [],
                "externalConsole": true,
                "MIMode": "gdb",
                "miDebuggerPath": "C:\\msys64\\mingw64\\bin\\gdb.exe",
                "setupCommands": [
                    {
                        "description": "Enable pretty-printing for gdb",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": true
                    }
                ]
            }
        ]
    }
    ```

=== "Ubuntu"

    Create a file at `xemu/.vscode/launch.json` with the following contents.

    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "(gdb) Launch",
                "type": "cppdbg",
                "request": "launch",
                "program": "${workspaceFolder}/dist/xemu",
                "args": [],
                "stopAtEntry": false,
                "cwd": "${workspaceFolder}/dist",
                "environment": [],
                "externalConsole": false,
                "MIMode": "gdb",
                "setupCommands": [
                    {
                        "description": "Enable pretty-printing for gdb",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": true
                    }
                ]
            }
        ]
    }
    ```

## Build & Run

Follow the [build](../../building-from-source/) instructions appending `--debug` to the CLI arguments, open the xemu project directory in VSCode via <kbd>File</kbd> &rarr; <kbd>Open folder...</kbd>, and press `F5` to start debugging.

!!! tip "Tip: Arguments"

    Argument key-value pairs must be separated.

    ```
    "args": [
        "-machine","xbox,avpack=hdtv"
    ]
    ```

    Host and guest debugging can be used simultaneously.

    ```
    "args": [
        // enable the guest gdb server
        "-s",

        // start in a paused state
        "-S"
    ]
    ```