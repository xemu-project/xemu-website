#### Q: Can I get some help?
Of course, but first please read through the [getting started guide](getting-started.md). If you still have questions, please read the following FAQs. If you're still having problems, head to #help in the xemu Discord server.

[![Chat Badge](https://img.shields.io/badge/Chat-xemu%20Discord%20Server-7289DA?logo=Discord&logoColor=white)](https://discord.gg/ayyjsuM)

#### Q: Are there system requirements?
There are not strict requirements; most relatively modern systems should be able to run xemu. xemu runs on all major operating systems.

#### Q: What BIOS do I need to use?
Your MCPX and BIOS dump should be for a 1.0 Xbox. It's suggested that your MCPX dump be 1.0 and that a compatible BIOS image be used (users have reported success with "COMPLEX 4627").

#### Q: Do I need to have an EEPROM file?
A default one will be created if you do not provide one.

#### Q: Why am I getting `The guest has not initialized the display`
This is likely due to a mismatch of MCPX and BIOS images, or a corrupt MCPX boot ROM.

#### Q: Why am I getting `Please insert an Xbox disc...`? I already loaded an ISO.
Try restarting xemu. If you continue to get the message, your ISO may not be dumped in a compatible way. Try using `extract-xiso` to pack your ISO.

#### Q: Is there a game compatibility list?
Yes, visit https://xemu.app

#### Q: Does game `x`  work?
Possibly. Check the compatibility list first if you're curious, or try it out for yourself. You are invited to submit a compatibility report too.

#### Q: Does xemu run my game's `default.xbe`?
No, not directly. xemu emulates the hardware of the system, so you'll need to have a disc image of your game backup. You can use [extract-xiso](https://github.com/xboxdev/extract-xiso) or qwix to create an image.

#### Q: Does xemu support "redump" style ISOs?
No, not yet. You can however convert a redump style ISO to a compatible ISO. More info [here](<https://github.com/mborgerson/xemu/wiki#about-redump-isos>).

#### Q: Why am I getting an `Assertion failed!` message?
When a game exercises a piece of code in xemu that has not yet been implemented or verified, xemu will `assert`  which forces execution to stop. The reason for this is that anything happening beyond that point may be unpredictable and significantly increase the debugging burden.

#### Q: I think I've found a bug, what do I do?
Join the Discord server and chat about what you're seeing in #general, maybe it's a known issue. We can work together to get it recorded and fixed.