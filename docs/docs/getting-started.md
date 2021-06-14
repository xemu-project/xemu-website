xemu is a low-level, full-system emulator which emulates the actual hardware of
the Xbox; this means that in order to actually run xemu, you must have a copy
of the stuff that a real Xbox needs when it turns on:

1. [The MCPX Boot ROM image](#mcpx-boot-rom-image)
2. [The flash ROM image (aka *BIOS*)](#flash-rom-image-aka-bioskernel)
3. [A properly-formatted hard disk drive image](#hard-disk-drive-image)
4. [Game disc image(s)](#game-disc-images)

Unfortunately, distributing some of these items would violate copyright laws, so
you'll need to acquire them on your own.

!!! warning "Disclaimer"
    The xemu project does not endorse or promote piracy. We don't link to
    copyrighted files, or discuss how to acquire them. The only legal way to
    acquire these files is to dump them from *your real, physical Xbox*. Please
    don't ask us how to get them.

## MCPX Boot ROM Image

    MD5 (mcpx_1.0.bin) = d49c52a4102f6df7bcf8d0617ac475ed

If your MCPX dump has an MD5 of `196a5f59a13382c185636e691d6c323d`, you dumped
it badly and it's a couple of bytes off. It should start with `0x33 0xC0` and end
with `0x02 0xEE`.

## Flash ROM Image (aka BIOS/Kernel)

Xbox compatible BIOS. Just like a real Xbox, running an unmodified retail BIOS will
not allow booting unofficial software.

People have reported most success using the modified retail "COMPLEX 4627" BIOS.

## Hard Disk Drive Image

You have options:

### Option 1: Use a pre-built Xbox HDD image (recommended)

You can use a pre-built 8G Xbox HDD image, free of any copyrighted content, and
only containing a dummy dashboard. [You can download this image from
here!](https://github.com/mborgerson/xemu-hdd-image/releases/latest/download/xbox_hdd.qcow2.zip)

!!! note
    By design, this particular drive image does not contain the official Xbox
    dashboard, but instead contains only a dummy dashboard. Because of this, you
    may see an error message when starting xemu with an unmodified retail BIOS
    image due to the system failing to find a properly signed dashboard.

    If you would like to change your dashboard (perhaps to the official retail
    dashboard, or any alternative dashboard), or copy additional files over to
    the Xbox HDD, you can start xemu, using a modified BIOS image, and a disc
    containing an alternative dashboard. Then you can either install that
    dashboard, or connect to xemu using FTP to transfer your desired dashboard
    files to the HDD.

### Option 2: Image your real Xbox HDD

This is the most authentic way to do it. Unlock your drive, connect it to a
computer, and `dd` the entire contents of the drive straight to a file. This
file can be used as-is with xemu.

### Option 3: Build a new HDD image from scratch

You can also create an Xbox hard-disk image using XboxHDM. Directions on how
to do this [can be found here](https://github.com/mborgerson/xemu-hdd-image).

## Game Disc Images

xemu requires game discs to be in the form of ".iso" disc images. You can
backup your legally purchased games by:

* Using a real Xbox with a custom dashboard to transfer the game files to your
  computer over FTP.
* Purchasing and using a special, reflashed DVD drive. [More details here](http://wiki.redump.org/index.php?title=Microsoft_Xbox_and_Xbox_360_Dumping_Guide).

You can create an iso image using [extract-xiso](https://github.com/XboxDev/extract-xiso) (command-line only).

### About "redump" ISOs

Redump-style ISOs contain data for both the video partition and game partition. For now,
you'll want to extract the game partition for use with xemu. You can do this by simply
extracting everything after the first 387MiB. For example, using `dd`:

```
dd if=my-redump-style-dump.iso of=my-game-partition.iso skip=387 bs=1M
```

You can then use the `my-game-partition.iso` with xemu.

I've found an issue, what do I do?
----------------------------------
Come chat on the Discord server linked at the top and we can do an early diagnosis of the issue. If necessary, we can catalog the issue for further exploration.

---
<a href="#content-top">Return to Top</a>
