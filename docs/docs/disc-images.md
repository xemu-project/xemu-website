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
second partition of the disc image for use with xemu. Unfortunately there is not
a GUI-friendly solution for this yet. You will need to use a command-line tool.
You can do this with utilities such as `dd`, `extract-xiso` or `fallocate` on supported systems.

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

## Converting Digital Xbox 360 backwards compatible titles

You can use backwards compatible titles that are on the Xbox 360 digital marketplace. You cannot rip a physical original Xbox game without a mod on the Xbox 360 which won't be specified here. If you have digital versions of the original Xbox games then follow what’s below.

You will need (windows):
* An unmodded Xbox 360 on version 17349 or later.
* USB Flash Drive formatted to FAT32 with enough storage
* God2iso 
* Velocity
* Xiso creator program (qwix, extract-xiso, etc)

**Note: Skip if you have external drive with backwards compatible titles already. But would be preferred if you use a new drive since it would be hard to tell between Xbox 360 titles and original Xbox titles at first.**

### Getting games on drive from an Xbox 360

1. Plug in your formatted flash drive or external hdd to the Xbox 360.

2. Go to Microsoft store to install the game and select install or you can copy the game from the dashboard.

3. Select your formatted storage device.

4. Turn off console and unplug your external drive.


### Windows process

1. Plug in drive to the computer.

**Note: If you see don’t see a contents folder then enable Show hidden files and folders in Windows Explorer.**

2. Once you see the content folder you can copy that folder as a backup or use it in our case to get the files we need.

3. Open the content folder and folder 0000# you should see folders with numbers and letters. 

4. This is your games list and you should go into one of them until you see a file and a folder that ends with (.data).

5. Open the file that’s next to the folder with god2iso and choose a area to save.

6. Once the god2iso file was made you open the new file you just made and extract with velocity.

Now you can use `extract-xiso ` or similar program to create a xiso for xemu or you can transfer those files to a Xbox to boot from. 

(Special thanks for the how to convert backwards compatible original xbox games from xbox 360 to original xbox tutorial that helped shape this one: https://www.reddit.com/r/originalxbox/comments/f12psc/comment/fh26eiq/)
