xemu requires game discs to be in the form of xiso images. These are generally
saved with a `.iso` extension, but are not the same as typical ISO images and
should be created following the instructions below.

!!! warning "Disclaimer"

    The xemu project does not endorse or promote piracy. We don't permit sharing
    of games on any channel. The only legal way to acquire these files is
    to dump them from your real, physical media.

## Backing Up Your Games

Fortunately games can be acquired for relatively cheap and it is very easy to
create a game backup. You can backup your legally purchased games by:

* Using your computer to connect via FTP to your real Xbox running a custom
  dashboard. You can simply insert the disc and transfer the game files from the
  `D` directory to your computer.
* Purchasing and using a special, reflashed DVD drive. [More details here](http://wiki.redump.org/index.php?title=Microsoft_Xbox_and_Xbox_360_Dumping_Guide).

## Creating XISOs

There are multiple tools available that can both create and extract XISO images.

### xdvdfs (Web or Command Line)

The recommended tool for creating and extracting XISO images is xdvdfs. This tool can run entirely locally and within your web browser.

[Open xdvdfs :fontawesome-solid-arrow-up-right-from-square:](https://xiso.antangelo.com){ .md-button .md-button--secondary target="_blank" }

!!! warning

    xdvdfs does not apply media patching to xbe
    files within the image. Some games on some
    BIOSes will not load as a result.

    For maximum compatibility, either
    apply the patch yourself, or use a BIOS
    that does this for you (such as m8plus).

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
You can do this with utilities such as `xdvdfs`, `dd`, or `fallocate` on supported systems.

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

=== "Using `fallocate`"
    This will truncate the original file in-place:
    ```
    fallocate -c -o 0 -l 387MiB game.iso
    ```

    You can then use the `game.iso` with xemu.

## Converting Digital Xbox 360 backwards compatible titles

You can use backwards compatible titles that are on the Xbox 360 digital marketplace. You cannot rip a physical original Xbox game without a mod on the Xbox 360 which won't be specified here. If you have digital versions of the original Xbox games then follow what’s below.

(Windows Requirements) You will need:

* Xbox 360 on version 17349 or later.
* USB Flash Drive formatted to FAT32 with enough storage
* [God2iso](https://github.com/raburton/god2iso/releases) 
* [Velocity](https://github.com/hetelek/Velocity/releases)
* [Xiso Creation Software](https://xemu.app/docs/disc-images/#creating-xisos)

**Note: Skip if you have external drive with backwards compatible titles already. But would be preferred if you use a fresh drive since it would be hard to tell between Xbox 360 titles and original Xbox titles at first.**

### Getting games on drive from an Xbox 360

1. Plug in your formatted flash drive or external hdd to the Xbox 360.

2. Copy the game from the dashboard under storage in settings or go to the Xbox Marketplace/Purchase History to install the game and select install.

3. Select your formatted storage device and wait until its finished.

4. Preferably with the console powered off, Unplug your external drive.


### Windows

1. Plug in drive to the computer.

**Note: If you don’t see a contents folder. Then enable Show hidden files and folders in Windows Explorer.**

2. Once you see the content folder you can copy that folder as a backup or use it in our case to get the files we need.

3. Open the content folder and folder 0000#. You should see folders with numbers and letters. 

**Note: Alternatively, you can avoid this by only storing backward compatible titles in the drive or by copying each game individually.**

4. This is your games list. To proceed, select one of the games and look for a file and a folder that ends with (.data). 

5. Open the file next to the folder with god2iso and select a save location.

6. Once you create the god2iso file, you open the new file you just made and extract it using Velocity.

Now you can use `extract-xiso` or any similar program in [Creating XISOs Section](https://xemu.app/docs/disc-images/#creating-xisos) to create a xiso for xemu or you can transfer those files to a Xbox to boot from. 

**Special thanks to the tutorial on how to convert backwards compatible original Xbox games from Xbox 360 to original Xbox that provided the basis for this [guide](https://www.reddit.com/r/originalxbox/comments/f12psc/comment/fh26eiq/)**
