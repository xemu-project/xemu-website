xemu requires game discs to be in the form of xiso images. These are generally
saved with a `.iso` extension, but are not the same as typical ISO images and
should be created following the instructions below.

!!! warning "Disclaimer"

    The xemu project does not endorse or promote piracy. We don't permit sharing
    of games on any channel. The only legal way to acquire these files is
    to dump them from your real, physical media.

## Backing Up

Fortunately games can be acquired for relatively cheap and it is very easy to
create a game backup. You can backup your legally purchased games by:

* Using your computer to connect via FTP to your real Xbox running a custom
  dashboard. You can simply insert the disc and transfer the game files from the
  `D` directory to your computer.
* Purchasing and using a special, reflashed DVD drive. [More details here](http://wiki.redump.org/index.php?title=Microsoft_Xbox_and_Xbox_360_Dumping_Guide).

## Creating ISOs

### xdvdfs (Web or Command Line)

[xdvdfs](https://github.com/antangelo/xdvdfs)
is a tool that can manage Xbox disc images.
It is available as a [webapp](https://xiso.antangelo.com/) or as a command line tool.

!!! warning

    xdvdfs does not apply media patching to xbe
    files within the image. Some games on some
    BIOSes will not load as a result.

    For maximum compatibility, either
    apply the patch yourself, or use a BIOS
    that does this for you (such as m8plus).

### extract-xiso (Command Line)

[extract-xiso](https://github.com/XboxDev/extract-xiso) is a command-line tool
to create Xbox-compatible disc images.

!!! warning

    Use only 32-bit builds of extract-xiso. 64-bit builds can cause subtle
    issues resulting in dirty disc errors.

If you have downloaded your game files over FTP to a directory, the directory
structure will look something like this:

```
game/
  default.xbe
  data/
    image.tga
```

You can run:

```bash
extract-xiso -c game
```

game.iso will be produced. This can be used with xemu.

### Qwix (GUI)

[Qwix](https://avalaunch.net/qwix/) is a popular GUI based tool for creating
Xbox compatible ISO images.

!!! warning
    Qwix is not an open-source project, it is not maintained by the xemu project. Use at own risk.

## About "redump" ISOs

"Redump" ISOs are a full dump of the game disc. Xbox game discs contain two
partitions, the first is a video partition which you can access from a computer
or DVD player. This partition usually contains a short video instructing you to
insert the disc into an Xbox. The second partition contains the actual game
data. A "redump" ISO contains both of these partitions.

If you have used a customized DVD drive to produce a backup of your game disc,
you more than likely have this format. As a sanity check, these images are
typically ~7GB in size.

xemu is not currently compatible with this format, but you can extract the
second partition of the disc image for use with xemu.
You can do this with utilities such as `xdvdfs`, `dd`, `extract-xiso` or `fallocate` on supported systems.

=== "Using `xdvdfs`"
    The [webapp](https://xiso.antangelo.com/) tool is capable of repacking or extracting most redump ISO images
    by selecting an ISO file as the input. The output file can then be used with xemu.

    The command line tool is also able to repack or extract redump ISO images:
    ```
    xdvdfs pack game-redump.iso
    ```

    You can then use `game-redump.xiso.iso` with xemu.

=== "Using `dd`"
    ```
    dd if=game-redump.iso of=game.iso skip=387 bs=1M
    ```

    You can then use the `game.iso` with xemu.

=== "Using `extract-xiso`"
    ```
    extract-xiso -r game-redump.iso
    ```

    You can then use `game-redump.iso` with xemu. Your original will be
    `game-redump.iso.old`.

=== "Using `fallocate`"
    This will truncate the original file in-place:
    ```
    fallocate -c -o 0 -l 387MiB game.iso
    ```

    You can then use the `game.iso` with xemu.
