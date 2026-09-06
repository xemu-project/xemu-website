Built with SDL3, xemu supports virtually all gamepads. Connect up to 4
controllers at any time, just like a real Xbox.

!!! note "Notes & FAQ"
    * Hot plugging works on Windows and Linux. It is broken on macOS.
    * USB passthru is not supported yet, but it will be coming.
    * Only the Xbox controller is emulated. There is not (yet) support for other controllers like the Steel Batallion.

!!! bug "Input not functional on early BIOS revisions"
    Emulated gamepads may be non-functional when using early BIOS revisions
    (<4627). It is recommended to not use these early BIOS revisions,
    until this bug is fixed.


## Popular Gamepads

### Xbox One, Xbox 360 controllers

On Windows and Linux they should be supported out of the box. On macOS you will
need to install an additional driver.

* macOS: [360Controller](https://github.com/360Controller/360Controller)

### Original Xbox controllers

The original Xbox controllers are USB-compatible and can be connected to a PC
with an adapter. Please don't cut original Xbox controller cables to make an
adapter. Quality adapters [can be purchased on Amazon](https://www.amazon.com/Mcbazel-Replacement-Xbox-Controller-Adapter-Microsoft/dp/B000RT2868)
for about $12 USD or from eBay for about $8 USD, shipped globally.

Depending on your platform, you may also need to install additional drivers:

* Windows: [Xb2XInput](https://github.com/emoose/Xb2XInput)
* macOS: [360Controller](https://github.com/360Controller/360Controller)
* Linux: Usually supported out of the box (xpad).

### DualShock 4 controllers

Sony DualShock 4 controllers work, out of the box, on all platforms. No
additional installation of drivers or configuration is required.

## Custom Controllers and SDL GameControllerDB

SDL distinguishes between generic joysticks and standard gamepads. For a
controller to be recognized and available in xemu's input configuration,
SDL must have a gamepad definition that maps the controller's physical
buttons and axes to standard controls.

While many popular controllers are supported by SDL's built-in database,
yours may not be recognized by default. You can create and load custom
mappings or use the community-maintained
[SDL_GameControllerDB](https://github.com/mdqinc/SDL_GameControllerDB/).

### Configuring a Custom GameControllerDB File

xemu supports loading an external mapping database file (typically named
`gamecontrollerdb.txt`) through the `gamecontrollerdb_path` option in your
`xemu.toml` configuration file.

Add or update the `[input]` section in your `xemu.toml`:

```toml
[input]
gamecontrollerdb_path = "/path/to/gamecontrollerdb.txt"
```

* On startup, xemu will load the mappings and print a message to the
  console or `xemu.log`:
  ```
  Loaded 123 custom gamepad mapping(s) from '/path/to/gamecontrollerdb.txt'
  ```

### Obtaining or Creating Controller Mappings

1. **Download the community database:**
   The easiest option is to download the latest `gamecontrollerdb.txt` from
   the [SDL_GameControllerDB GitHub repository](https://raw.githubusercontent.com/mdqinc/SDL_GameControllerDB/master/gamecontrollerdb.txt).
   Many third-party controllers already have community-contributed mappings
   there. Save this file to a convenient location on your system and set
   `gamecontrollerdb_path` to point to it.

2. **Generate a mapping for an unlisted controller:**
   If your controller is still not recognized after loading the database,
   you can generate a custom mapping string for your specific device. See
   the instructions on the SDL_GameControllerDB site](https://github.com/mdqinc/SDL_GameControllerDB/)

!!! tip "Share your mapping upstream"
    If you created a mapping for a controller that was missing from the
    database, consider [submitting a pull request to SDL_GameControllerDB](https://github.com/mdqinc/SDL_GameControllerDB/)
    so other users and future versions of SDL can benefit from it.

## Keyboard as Gamepad

The default keyboard layout for the gamepad is:

| Keyboard  | Gamepad       | Keyboard  | Gamepad       |
|-----------|---------------|-----------|---------------|
| A         | A             | BACKSPACE | BACK          |
| B         | B             | RETURN    | START         |
| X         | X             | 1         | WHITE         |
| Y         | Y             | 2         | BLACK         |
| LEFT      | DPAD_LEFT     | 3         | LSTICK        |
| UP        | DPAD_UP       | 4         | RSTICK        |
| RIGHT     | DPAD_RIGHT    | 5         | GUIDE (xemu Nav) |
| DOWN      | DPAD_DOWN     |           |               |

```
      Left                 Right

    W = LTrig                   O = RTrig
       E                     I
    S     F               J     L
       D                     K
```
