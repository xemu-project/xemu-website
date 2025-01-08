## Download for Windows

[Download for :fontawesome-brands-windows: Windows (x86_64)](https://github.com/xemu-project/xemu/releases/latest/download/xemu-win-x86_64-release.zip){ .md-button .md-button--secondary } [Download for :fontawesome-brands-windows: Windows (arm64)](https://github.com/xemu-project/xemu/releases/latest/download/xemu-win-aarch64-release.zip){ .md-button .md-button--secondary }

### Installation

Simply download the Zip archive release for Windows from the link above, extract the archive to a directory, then double-click on xemu.exe.

## Download for macOS

[Download for :fontawesome-brands-apple: macOS (Universal)](https://github.com/xemu-project/xemu/releases/latest/download/xemu-macos-universal-release.zip){ .md-button .md-button--secondary }

### Install Manually

Simply download the Zip archive release for macOS from the link above, extract the archive, then run the application. Optionally drag the xemu app bundle to your Applications folder.

Because the app is not signed, you will need to right-click, or hold the <kbd>control</kbd> key and click, on the app and in the context menu that appears select <kbd>Open</kbd> on first launch.

### Install via Homebrew

If you have the [Homebrew package manager](https://brew.sh) installed, you can install xemu with:

`brew install --cask xemu`

## Download for Linux

There are multiple options for running xemu on your Linux system.

### AppImage

[Download AppImage for :fontawesome-brands-linux: Linux (x86_64)](https://github.com/xemu-project/xemu/releases/download/v{{xemu_version}}/xemu-v{{xemu_version}}-x86_64.AppImage){ .md-button .md-button--secondary }

!!! info "Running the AppImage"

	The AppImage file needs to be marked executable before it can be run. You can do this in your file browser: navigate to and select the AppImage file, right-click and open file properties, navigate to permissions tab, then enable 'Allow executing file as program'. You can also do this in a terminal, simply with `chmod +x *.AppImage`. Once the AppImage is marked executable it can be 'double-clicked' on to start xemu. See [AppImage documentation](https://docs.appimage.org/user-guide/run-appimages.html#download-make-executable-run) for more information about running AppImages and further system integration.

### Flatpak

Supported architectures: x86_64 and aarch64

1. [Set up Flatpak](https://www.flatpak.org/setup/)

2. Install xemu from [Flathub](https://flathub.org/apps/details/app.xemu.xemu)

`flatpak install -y app.xemu.xemu`

3. Run xemu

`flatpak run app.xemu.xemu`

!!! warning "Accessible Directories"

	When using the flatpak installation method, only the `~/.var/app/app.xemu.xemu/data/xemu/xemu` directory can be written to by xemu. The Hard Disk image must be placed there, for example at `~/.var/app/app.xemu.xemu/data/xemu/xemu/xbox_hdd.qcow2`.
	If you want to whitelist additional directories, you can [do so with `flatseal` or `flatpak override`](troubleshooting.md#flatpak-release-will-not-load-the-hard-drive).

### Ubuntu PPA

Supported architectures: x86_64 and aarch64

Users running recent versions of Ubuntu (22.04 and newer) are recommended to install through the daily build PPA repository. At the command line, run the following:

```sh
sudo add-apt-repository ppa:mborgerson/xemu
sudo apt update
sudo apt install xemu
```

You can now launch xemu through your typical launcher, or by typing `xemu` at the command line.

### Build from source

On most Linux distributions, it is also possible to [build from source](dev/building-from-source.md#linux).

## Previous Releases

You can find older builds of xemu on the [Releases page](https://github.com/xemu-project/xemu/releases).
