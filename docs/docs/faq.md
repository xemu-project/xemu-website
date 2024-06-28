#### Q: Can I get some help?
Of course, but first please read through the [setup guide](download.md). If you still have questions, please read the following FAQs. If you're still having problems, head to #help in the xemu Discord server.

[Join xemu community on :fontawesome-brands-discord: Discord](https://discord.gg/ayyjsuM){ .md-button .md-button--secondary target="_blank" }

#### Q: I think I've found a bug, what do I do?
Join the Discord server and chat about what you're seeing in #general, maybe it's a known issue. We can work together to get it recorded and fixed.

#### Q: Are there system requirements?
See [here](about.md#system-requirements).

#### Q: Performance is bad...what can I do about it?
See [this page](troubleshooting.md/#windows-performance-considerations) for tips to improve performance. Note that xemu is evolving and performance is subject to change.

#### Q: What BIOS do I need to use?
Your MCPX and BIOS dump should be for a 1.0 Xbox. It's suggested that your MCPX dump be 1.0 and that a compatible BIOS image be used (users have reported success with "COMPLEX 4627").

#### Q: Do I need to have an EEPROM file?
A default one will be created if you do not provide one.

#### Q: How do I run xemu in portable mode?
Create a file named `xemu.toml` in the same directory as the executable (i.e. next to `xemu.exe` on Windows or `xemu` on Linux).

#### Q: Why am I getting `The guest has not initialized the display`
This is likely due to a mismatch of MCPX and BIOS images, or a corrupt MCPX boot ROM.

#### Q: Why am I getting `Please insert an Xbox disc...`? I already loaded an ISO.
Try restarting xemu. If you continue to get the message, your ISO may not be dumped in a compatible way. Try using [extract-xiso](https://github.com/xboxdev/extract-xiso) to pack your ISO.

#### Q: Is there a game compatibility list?
Yes, visit https://xemu.app

#### Q: Does game `x`  work?
Possibly. [Check the compatibility list](https://xemu.app) first if you're curious, or try it out for yourself. You are invited to submit a compatibility report too.

#### Q: Does xemu run my game's `default.xbe`?
No, not directly. xemu emulates the hardware of the system, so you'll need to have a disc image of your game backup. You can use [extract-xiso](https://github.com/xboxdev/extract-xiso) or qwix to create an image.

#### Q: Does xemu support "redump" style ISOs?
No, not yet. You can however convert a redump style ISO to a compatible ISO. More info [here](<https://xemu.app/docs/disc-images/#about-redump-isos>).

#### Q: Why am I getting an `Assertion failed!` message?
When a game exercises a piece of code in xemu that has not yet been implemented or verified, xemu will `assert`  which forces execution to stop. The reason for this is that anything happening beyond that point may be unpredictable and significantly increase the debugging burden.

#### Q: How do I enable widescreen mode?
You can change the setting in your [dashboard](dashboard.md) or use the [EEPROM editor](eeprom.md) to enable widescreen. Then select 'Scale (Widescreen 16:9)' in xemu View scaling mode. Note: not all games support widescreen.

#### Q: How can I increase the resolution?
For all titles the rendering resolution can be easily scaled by navigating to View&rarr;Int. Resolution Scale. For titles that natively support higher resolutions, you can enable the associated mode in your dashboard or by using the [EEPROM editor](eeprom.md).

#### Q: What should I pick for 4k resolution?
The 'Resolution Scale' number is a scaling factor applied to rendered surface dimensions. Which factor to select for your target resolution depends on the game resolution. When the game is rendering at 480p (typical case), if you want a '4k resolution' (meaning around 4k horizontal res) you can select 6x to get a framebuffer of 3840x2880. Performance may diminish as higher factors are selected.

#### Q: Are there any plans for a mobile port of xemu?
There are currently no plans for a mobile port of xemu on iOS or Android, the emulator hasn't reached the performance necessary to run well on iOS or Android at this time.

#### Q: Are there any plans for a Vulkan backend?
It is in development.

#### Q: Can xemu load an Xbox game disc from my computer's DVD drive?
Generally, no. You will need to create a backup of your game disc. Please [see here](disc-images.md) for more information about creating and using disc images.

#### Q: Why does xemu crash when I enable Surround Sound in my EEPROM?
This is because Surround Sound isn't implemented in xemu yet, please disable this in your [EEPROM](eeprom.md) if you have it enabled.

#### Q: Where does xemu store game saves?
Just like on a real Xbox, they are stored on the E partition of the virtual hard drive. The drive contents can be accessed with [FTP](ftp.md).

#### Q: Where does xemu store snapshot (save state) data?
Snapshot data is stored on the hard drive image, and is not easily extractible.
