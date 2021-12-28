## Binaries

Users are recommended to use the [pre-built xemu binaries](https://github.com/mborgerson/xemu/wiki#download). If you would like to build from source however, follow the instructions for your platform below.

## Windows

Windows builds are cross-compiled from Ubuntu. If you would like to build *on* Windows, you can use WSL2 and Docker. See [official Docker
documentation](https://docs.docker.com/docker-for-windows/wsl/) for how to get WSL2 and Docker set up. Make sure to remove back slashes in the build portion and make sure the build command is one line.

```bash
# Configure git and change back To true after use if needed
git config --global core.autocrlf false

# Clone and build
git clone --recurse-submodules https://github.com/mborgerson/xemu.git
docker run --rm -v $PWD/xemu:/xemu -w /xemu \
    -e CCACHE_DIR=/xemu/ccache \
    mborgerson/xemu-ubuntu-win64-cross:latest \
    ./build.sh -p win64-cross

# Run
./xemu/dist/xemu.exe
```

## macOS

First install the [Homebrew package manager](https://brew.sh/).

```bash
# Install dependencies
brew update
brew install coreutils pkg-config dylibbundler ninja

# Clone and build
git clone https://github.com/mborgerson/xemu.git
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
    sudo apt install git build-essential libsdl2-dev libepoxy-dev libpixman-1-dev libgtk-3-dev libssl-dev libsamplerate0-dev libpcap-dev ninja-build

    # Clone and build
    git clone https://github.com/mborgerson/xemu.git
    cd xemu
    ./build.sh

    # Run
    ./dist/xemu
    ```

=== "Arch Linux"

    ```bash
    # Install dependencies
    sudo pacman -S --noconfirm git base-devel sdl2 libepoxy pixman gtk3 openssl libsamplerate libpcap ninja glu

    # Clone and build
    git clone https://github.com/mborgerson/xemu.git
    cd xemu
    ./build.sh

    # Run
    ./dist/xemu
    ```

=== "Fedora"

    ```bash
    # Install dependencies
    sudo dnf install libdrm-devel libslirp-devel mesa-libGLU-devel gtk3-devel libpcap-devel libsamplerate-devel libaio-devel SDL2-devel libepoxy-devel pixman-devel gcc-c++ ninja-build openssl-devel

    # Clone and build
    git clone https://github.com/mborgerson/xemu.git
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
