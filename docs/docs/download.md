## Download for Windows

[![Download](https://img.shields.io/badge/Download-Windows-blue?logo=Windows&logoColor=white)](https://github.com/mborgerson/xemu/releases/latest/download/xemu-win-release.zip)

The latest pre-built release version is recommended. Simply download the release for Windows, extract the archive, and launch xemu.exe.

## Download for macOS

[![Download](https://img.shields.io/badge/Download-macOS-blue?logo=Apple&logoColor=white)](https://github.com/mborgerson/xemu/releases/latest/download/xemu-macos-universal-release.zip)

**Note:** The above download is a Universal binary, for both x86-64 and the new Apple M1-based Macs.

The latest pre-built release version is recommended. Simply download the release for macOS, extract the archive, then run the application (optionally drag the *xemu* app to your Applications folder). Because the app is not signed, you will need to right-click, or hold the <kbd>control</kbd> key and click, on the app and in the context menu that appears select <kbd>Open</kbd> on first launch.

## Download for Linux

### Ubuntu 18.04 and newer

[![Download](https://img.shields.io/badge/Download-Ubuntu%20PPA-orange?logo=ubuntu&logoColor=white)](https://launchpad.net/~mborgerson/+archive/ubuntu/xemu)

Users running recent versions of Ubuntu (18.04 and newer) are recommended to install through the daily build PPA repository.

At the command line, run the following:

```bash
sudo add-apt-repository ppa:mborgerson/xemu
sudo apt update
sudo apt install xemu
```

You can now launch xemu through your typical launcher, or by typing `xemu` at the command line.

### Other Distributions

Users running non-Ubuntu distributions are currently recommended to [build from source](building-from-source.md#linux).
