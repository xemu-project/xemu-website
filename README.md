xemu-website
====

This repo contains the main website contents for the xemu original Xbox emulator with accompanying documentation and title information for compatibility reporting.

### Cloning

This repository must be cloned with submodules to pull the Xbox title repository.

```sh
$ git clone git@github.com:xemu-project/xemu-website.git --recurse-submodules
```

Or if already cloned, run `git submodules update --init --recursive`

### Build

To build, simply run `rm -rf dist/ && DEV=1 ./build.sh` from within the project root.

To serve the built site, run in the `dist` directory: `python -m http.server`.

#### Ubuntu

    $ sudo apt install wget unzip git python3 pip
    $ pip install -r requirements.txt

#### Windows

Follow the Ubuntu instructions above for [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install) paired with [Docker Desktop](https://docs.docker.com/desktop/windows/wsl/)

### Tips

Switch to development mode and update the main url to your local filesystem path within `generate.py`

```
develop_mode = True
main_url_base = '{YOUR LOCAL ABSOLUTE FILESYSTEM PATH GOES HERE}/xemu-website/dist'
```

Documentation is generated via [MkDocs](https://www.mkdocs.org). The source files can be found within the `\docs\docs` folder and configured via `\docs\mkdocs.yml`
