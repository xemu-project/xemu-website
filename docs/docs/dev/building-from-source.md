## Binaries

Users are recommended to use the [pre-built xemu binaries](https://xemu.app/docs/download/). If you would like to build from source however, follow the instructions for your platform below.

## Windows

Windows builds are cross-compiled from Ubuntu. If you would like to build *on* Windows, you can use Windows Subsystem for Linux (WSL) and podman / Docker with the xemu build container image.

See [here](https://learn.microsoft.com/en-us/windows/wsl/install) for details on how to install WSL. To install podman, run `sudo apt install podman-docker`.

```bash
# Clone and build
git clone https://github.com/xemu-project/xemu
docker run --rm -v $PWD/xemu:/xemu -w /xemu \
    -e CCACHE_DIR=/xemu/ccache \
    ghcr.io/xemu-project/xemu-win64-toolchain:latest \
    ./build.sh -p win64-cross

# Run
./xemu/dist/xemu.exe
```

### Tips

* The `docker run` command must be done from the directory containing the `xemu` clone, not from inside the clone. If running
`ls -d xemu` does not print "xemu" you will need to change directories.

* When building on Windows via WSL2, doing the `git clone` from inside WSL2 may substantially increase the build speed.

## macOS

First install the [Homebrew package manager](https://brew.sh/).

```bash
# Install dependencies
brew update
brew install coreutils pkg-config dylibbundler ninja
python3 -m pip install pyyaml

# Clone and build
git clone --recurse-submodules https://github.com/xemu-project/xemu.git
cd xemu
./build.sh

# Run
open ./dist/xemu.app
```

## Linux

=== "Debian/Ubuntu"

    ```bash
    # Install dependencies
    sudo apt update
    sudo apt install git build-essential libsdl2-dev libepoxy-dev libpixman-1-dev libgtk-3-dev libssl-dev libsamplerate0-dev libpcap-dev ninja-build python3-yaml libslirp-dev

    # Clone and build
    git clone --recurse-submodules https://github.com/xemu-project/xemu.git
    cd xemu
    ./build.sh

    # Run
    ./dist/xemu
    ```

=== "Arch Linux"

    ```bash
    # Install dependencies
    sudo pacman -S --noconfirm git base-devel sdl2 libepoxy pixman gtk3 openssl libsamplerate libpcap ninja glu python-yaml libslirp

    # Clone and build
    git clone --recurse-submodules https://github.com/xemu-project/xemu.git
    cd xemu
    ./build.sh

    # Run
    ./dist/xemu
    ```

=== "Fedora"

    ```bash
    # Install dependencies
    sudo dnf install libdrm-devel libslirp-devel mesa-libGLU-devel gtk3-devel libpcap-devel libsamplerate-devel libaio-devel SDL2-devel libepoxy-devel pixman-devel gcc-c++ ninja-build openssl-devel python3-pyyaml

    # Clone and build
    git clone --recurse-submodules https://github.com/xemu-project/xemu.git
    cd xemu
    ./build.sh

    # Run
    ./dist/xemu
    ```

=== "SteamOS 3+ (Rootless)"

    ```bash
    # Install DistroBox
    curl -s https://raw.githubusercontent.com/89luca89/distrobox/main/install | sh -s -- --prefix ~/.local && curl -s https://raw.githubusercontent.com/89luca89/distrobox/main/extras/install-podman | sh -s -- --prefix ~/.local
    
    # Go to home/deck/ and create a file named .distroboxrc and in kate add whats below.
    export PATH=$PATH:/home/deck/.local/bin/
    export PATH=$PATH:/home/deck/.local/podman/bin/
    xhost +si:localuser:$USER
    
    # Installing Container 
    distrobox-create -i docker.io/library/archlinux:latest --name arch

    # Launch arch container.
    distrobox-enter arch
    
    # Install dependencies
    sudo pacman -S --needed --noconfirm git base-devel sdl2 libepoxy pixman gtk3 openssl libsamplerate libpcap ninja glu python-yaml libslirp && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si && sudo pacman -S pipewire-pulse

    # !During pulse audio install Select wireplumber

    # Install an IDE/code editor (vscode)
    yay -S visual-studio-code-bin --noconfirm

    # export Code editor if it has a .desktop
    distrobox-export --app code

    # Clone and build
    git clone --recurse-submodules https://github.com/xemu-project/xemu.git
    cd xemu
    ./build.sh

    # Run
    ./dist/xemu
    ```

!!! tip "Tip: Building with Clang, or another specific compiler"

    If you have multiple toolchains and would like to build with specific one,
    such as clang, you can specify the compiler and linker through environment
    variables when invoking build.sh as follows:

    ```bash
    CC=clang CXX=clang++ CC_LD=lld CXX_LD=lld AR=llvm-ar ./build.sh
    ```

!!! tip "Tip: Passing build flags to the C/C++ compiler"

    Extra build flags can be passed to the C/C++ compiler by using environment
    variables in a similar manner to changing toolchains. The CFLAGS variable
    sets C compiler flags and the CXXFLAGS variable sets C++ compiler flags.
    Multiple flags can be set by separating them with a space, just be sure to
    surround it in quotations. For example, if you wanted to build xemu with
    extra optimizations for your specific CPU then you would invoke build.sh
    as follows:

    ```bash
    CFLAGS="-march=native" CXXFLAGS="-march=native" ./build.sh
    ```
