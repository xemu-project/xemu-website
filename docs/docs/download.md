## Download for Windows

[Download for :fontawesome-brands-windows: Windows](https://github.com/mborgerson/xemu/releases/latest/download/xemu-win-release.zip){ .md-button .md-button--secondary }

### Installation

Simply download the Zip archive release for Windows from the link above, extract the archive to a directory, then double-click on xemu.exe.

## Download for macOS

[Download for :fontawesome-brands-apple: macOS](https://github.com/mborgerson/xemu/releases/latest/download/xemu-macos-universal-release.zip){ .md-button .md-button--secondary }

!!! check ":fontawesome-brands-apple: Apple M1 Compatibility Note"

	This download is a "Universal" binary, and will work on both Intel x86-64 and the new Apple M1-based Macs.

### Install Manually

Simply download the Zip archive release for macOS from the link above, extract the archive, then run the application. Optionally drag the xemu app bundle to your Applications folder.

Because the app is not signed, you will need to right-click, or hold the <kbd>control</kbd> key and click, on the app and in the context menu that appears select <kbd>Open</kbd> on first launch.

### Install via Homebrew

If you have the [Homebrew package manager](https://brew.sh) installed, you can install xemu with:

`brew install --cask xemu`

## Download for Linux

### Ubuntu PPA (20.04 and newer)

Users running recent versions of Ubuntu (20.04 and newer) are recommended to install through the daily build PPA repository. At the command line, run the following:

```sh
sudo add-apt-repository ppa:mborgerson/xemu
sudo apt update
sudo apt install xemu
```

You can now launch xemu through your typical launcher, or by typing `xemu` at the command line.

### Flatpak

1. [Set up Flatpak](https://www.flatpak.org/setup/)

2. Install xemu from [Flathub](https://flathub.org/apps/details/app.xemu.xemu)

`flatpak install -y app.xemu.xemu`

3. Run xemu

`flatpak run app.xemu.xemu`

!!! warning "Accessible Directories"

	When using the flatpak installation method, only the `~/.var/app/app.xemu.xemu/data/xemu/xemu` directory can be written to by xemu. The Hard Disk image must be placed there, for example at `~/.var/app/app.xemu.xemu/data/xemu/xemu/xbox_hdd.qcow2`.
	
	If you want to whitelist additional directories, you can [do so with Flatseal](troubleshooting.md#flatpak-release-will-not-load-bios-mcpx-rom-hard-drive).

### Build from source

On most Linux distributions, it is also possible to [build from source](building-from-source.md#linux).
