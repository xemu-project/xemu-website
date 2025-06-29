xemu is a low-level, full-system emulator which emulates the actual hardware of
the Xbox; this means that in order to actually run xemu, you must have a copy
of the stuff that a real Xbox needs when it turns on:

1. [MCPX Boot ROM Image](#mcpx-boot-rom-image)
2. [Flash ROM Image (BIOS)](#flash-rom-image-bios)
3. [Hard Disk Image](#hard-disk-image)

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

## Flash ROM Image (BIOS)

Xbox compatible BIOS. Due to key DRM functions being unimplemented, xemu is
currently unable to boot games when using an unmodified retail BIOS. You must use
either a debug BIOS or a modded retail BIOS that can boot unsigned software.

People have reported most success using the modified retail "COMPLEX 4627" BIOS.

## Hard Disk Image

You can use a pre-built 8G Xbox HDD image, free of any copyrighted content, and
only containing a dashboard with basic functionality.

[Download Pre-formatted Xbox Hard Disk Image ](https://github.com/xemu-project/xemu-dashboard/releases/latest/download/xbox_hdd.qcow2){ .md-button .md-button--secondary }

!!! note
    By design, this particular drive image does not contain the official Xbox
    dashboard, but instead contains only an **unsigned** dashboard with basic functionality to get started with xemu. [More
    information](dashboard.md)

??? "Alternative Options"
    **Alternative 1:** Image your real Xbox HDD

    This is the most authentic way to do it. Unlock your drive, connect it to a
    computer, and `dd` the entire contents of the drive straight to a file. This
    file can be used as-is with xemu.

    **Alternative 2:** Build a new HDD image from scratch

    You can also create an Xbox hard-disk image using XboxHDM. Directions on how
    to do this [can be found here](https://github.com/xemu-project/xemu-hdd-image).
    
    [FATXplorer](https://fatxplorer.eaton-works.com/2021/08/18/fatxplorer-3-0-beta-15--formatting-a-file-is-now-supported/)
    can also create an Xbox hard-disk image.
    
    Note: XboxHDM and FATXplorer are 3rd party tools and not maintained or supported directly by xemu project. Use at your own risk.
