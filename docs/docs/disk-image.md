# Creating a Disk Image

!!! warning "Disclaimer"
    The xemu project does not endorse or promote piracy. We don't link to
    copyrighted files, or discuss how to acquire them. The only legal way to
    acquire these files is to dump them from *your real, physical Xbox*. Please
    don't ask us how to get them.

## Determining your File Type

You can determine what type of file you have by seeing if your game folder has a <kbd>default.xbe</kbd> file then you have a normal game disk, you can pack this using [Extract-Xiso](https://github.com/XboxDev/extract-xiso) ([Windows Release](https://ci.appveyor.com/api/projects/xboxdev-bot/extract-xiso/artifacts/export/Release.zip?branch=master)) or [Qwix](https://avalaunch.net/qwix/).

!!! note
    Qwix is not an open-source project, it is not maintained by the xemu project.

You can determine if your game dump is a Redump by seeing if it has a <kbd>VIDEO_TS</kbd> or a <kbd>AUDIO_TS</kbd> folder and is about 6-7 GBs in size, you can reason that this is probably a redump, you can turn this into a xemu-compatibile file format by using [Extract-Xiso](https://github.com/XboxDev/extract-xiso) ([Windows Release](https://ci.appveyor.com/api/projects/xboxdev-bot/extract-xiso/artifacts/export/Release.zip?branch=master))
