The EEPROM is a small chip on the Xbox that contains various settings. xemu
emulates this EEPROM and the contents are stored in a file which you can
select in the xemu Settings dialog.

When you start xemu, if you have not provided an desired EEPROM image file a
valid EEPROM image will be generated for you.

## Editing Your EEPROM

You can use the Xbox EEPROM Online editor to adjust settings in your EEPROM image from within your web browser:

[Open Xbox EEPROM Online editor :fontawesome-solid-arrow-up-right-from-square:](https://eeprom.xboxarchive.org/){ .md-button .md-button--secondary target="_blank" }

You can also use the [XboxEepromEditor](https://github.com/Ernegien/XboxEepromEditor) ([Windows Download](https://github.com/Ernegien/XboxEepromEditor/releases/latest/download/XboxEepromEditor.zip))
to adjust settings in your EEPROM image offline.

!!! warning
    xemu doesn't support surround sound at this time, do not enable this in your eeprom.
