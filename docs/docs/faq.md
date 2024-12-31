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
This is likely due to missing, mismatched, or corrupt MCPX and BIOS images. See [this page](required-files.md) for details about required files.

#### Q: Why am I getting `Please insert an Xbox disc...`? Where's the classic Xbox menu?
Unfortunately we can't legally ship the original Xbox dashboard, so what you're seeing is the placeholder. See [this page](dashboard.md) for more information about dashboards, including details on how to install the one you want.

#### Q: I loaded an ISO, but I'm still getting `Please insert an Xbox disc...`
Try restarting xemu. If you continue to get the message, your ISO may not be dumped in a compatible way. See [this page](disc-images.md) for instructions on how to create a compatible disc image.

#### Q: I loaded an ISO, but I'm getting `You need to connect the DVD Playback Kit receiver kit to a controller port to watch movies` on the Xbox dashboard.
You've loaded a "redump" style ISO. xemu does not support this format yet. You can however convert a redump style ISO to a compatible ISO. More info [here](<https://xemu.app/docs/disc-images/#about-redump-isos>).

#### Q: Does xemu support "redump" style ISOs?
No, not yet. You can however convert a redump style ISO to a compatible ISO. More info [here](<https://xemu.app/docs/disc-images/#about-redump-isos>).

#### Q: Does xemu support compressed ISO formats like "CHD"?
No, it does not. You can try enabling filesystem level compression if you'd like to save some space.

#### Q: Is there a game compatibility list?
Yes, visit https://xemu.app

#### Q: Does game `x`  work?
Possibly. [Check the compatibility list](https://xemu.app) first if you're curious, or try it out for yourself. You are invited to submit a compatibility report too.

#### Q: The compatibility list says my game is Playable, why is it not working (freezes, dirty disc)?
There are multiple reasons why a game might not work, including various system issues, corrupted cache, bad disc dump, or regression in xemu compatibility. First try [downloading the version of xemu](https://github.com/xemu-project/xemu/releases) mentioned on the compatibility page. If the old version of xemu works and the latest does not, please report the issue to us.

#### Q: Does xemu run my game's `default.xbe`?
No, not directly. xemu emulates the hardware of the system, so you'll need to have a disc image of your game backup. See [this page](disc-images.md) for instructions on how to create a compatible disc image.

#### Q: Why am I getting an `Assertion failed!` message?
When a game exercises a piece of code in xemu that has not yet been implemented or verified, xemu will `assert`  which forces execution to stop. The reason for this is that anything happening beyond that point may be unpredictable and significantly increase the debugging burden.

#### Q: How do I enable widescreen mode?
You can change the setting in your [dashboard](dashboard.md) or use the [EEPROM editor](eeprom.md) to enable widescreen. Then select 'Scale (Widescreen 16:9)' in xemu View scaling mode. Note: not all games support widescreen.

#### Q: How can I increase the resolution?
For all titles the rendering resolution can be easily scaled by navigating to View&rarr;Int. Resolution Scale. For titles that natively support higher resolutions, you can enable the associated mode in your dashboard or by using the [EEPROM editor](eeprom.md).

#### Q: What should I pick for 4k resolution?
The 'Resolution Scale' number is a scaling factor applied to rendered surface dimensions. Which factor to select for your target resolution depends on the game resolution. When the game is rendering at 480p (typical case), if you want a '4k resolution' (meaning around 4k horizontal res) you can select 6x to get a framebuffer of 3840x2880. Performance may diminish as higher factors are selected.

#### Q: Are there any plans for an Android or iOS port?
There are currently no plans for a mobile port of xemu on Android or iOS, but possibly in the future.

#### Q: Can xemu load an Xbox game disc from my computer's DVD drive?
Generally, no. You will need to create a backup of your game disc. Please [see here](disc-images.md) for more information about creating and using disc images.

#### Q: Why does xemu crash when I enable Surround Sound in my EEPROM?
This is because Surround Sound isn't implemented in xemu yet, please disable this in your [EEPROM](eeprom.md) if you have it enabled.

#### Q: Where does xemu store game saves?
Just like on a real Xbox, they are stored on the E partition of the virtual hard drive. The drive contents can be accessed with [FTP](ftp.md).

#### Q: Where does xemu store snapshot (save state) data?
Snapshot data is stored on the hard drive image, and is not easily extractible.

#### Q: How do I use my computer's microphone in game?
Xbox Live Communicator peripheral emulation is not officially supported yet, but it is in development and will be added soon.

#### Q: Can I play local multiplayer?
Yes, you can connect multiple controllers just like a real Xbox.

#### Q: Can I play local multiplayer with my friends over the Internet?
If you're looking for split-screen play over the internet, xemu itself does not support this feature. However, there are 3rd party solutions like [Parsec](https://parsec.app/local-co-op-online) which can do this.

Many Xbox games also support System Link for LAN-based multiplayer. xemu does support networking, and this is another way to play with others over the Internet. See [this page](networking.md) for details about networking xemu to other instances of xemu, or even real Xboxes.

#### Q: Why do I see a System Link lobby but can't join it?
Make sure you and the people you're playing with have the same version of a game AND each console has a unique MAC address. The console's MAC address is stored in the EEPROM, so you can edit the EEPROM or delete it to have xemu generate a new one with a randomized MAC address. Warning: Game saves may be tied to the HDD key, so create a backup before deleting the EEPROM.

#### Q: Does xemu work with Xbox Live recreation projects, like "Insignia"?
Yes. See [this page](networking.md) for details about networking. See respective project pages for details about getting set up on their network.

#### Q: Why are my game saves not working?
Some game saves are tied to the console they were created on. Try using the EEPROM from the console they were created on.
