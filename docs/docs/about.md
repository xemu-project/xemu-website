xemu is free and open-source software that emulates the [original Microsoft Xbox game console](https://en.wikipedia.org/wiki/Xbox_(console)), enabling people to play their original Xbox games on Windows, macOS, and Linux systems.

!!! warning "Disclaimer"

    This project is for educational purposes only, with the goal of researching
    and understanding the inner-workings of the original Xbox and its games, and
    then building a platform to play those legally purchased games.

    This project does not endorse or promote copyright infringement of any kind.
    Developers work with legal backups of their own physical media and encourage
    all users to do the same. Piracy is not tolerated on any communication
    channel.

## System Requirements

xemu runs on Windows, macOS, and Linux systems. An OpenGL 4.0-compatible GPU is required. Most recent integrated GPUs will work.

Operating System releases that are no longer supported by their vendor are not officially supported by xemu. This means that releases of Windows prior to Windows 10 are not officially supported for xemu. Best-effort support is provided for in-service releases.

Please note that xemu is an evolving project and, although xemu can run on large number of systems, actual game performance is in flux and will vary based on the characteristics of your system.

## Compatibility

xemu emulates the hardware of the original Xbox, and in doing so is intended to be compatible with all software that can run on real original Xbox hardware, including official release titles and homebrew applications.

The [xemu compatibility tracking system](https://xemu.app/#compatibility) tracks compatibility of official release titles. Title compatibility status is provided by volunteer reporters in the community, as the reporter experienced the title in the current version of xemu on their computer at time of reporting. As the project evolves, reports may need to be updated. You are invited to help improve the project by submitting an updated compatibility report. Join the Discord server to learn how to contribute!

## License

xemu is free and open source software. Binaries and source of xemu are made available under the terms of the GNU General Public License, version 2.

xemu depends on several great open source libraries. Each distribution of xemu includes a LICENSE.txt file which includes specific license information for relevant libraries.

## Open Source Development

xemu is developed on GitHub at https://github.com/xemu-project/xemu. Contributions are welcome! See [here](https://xemu.app/docs/dev/) for xemu development documentation.

## History

The xemu project is a continuation of the [XQEMU project](https://xqemu.com/). The XQEMU project was started by [espes](https://github.com/espes/xqemu) in 2012 with significant contributions from [Jannik Vogel (JayFoxRox)](https://github.com/JayFoxRox), [Matt Borgerson (mborgerson)](https://github.com/mborgerson), and others. The xemu project was started by Matt Borgerson in 2020 and has since also received [many contributions](https://github.com/xemu-project/xemu/pulls?q=is%3Apr) from others.

xemu is built on the excellent [QEMU generic machine emulator project](https://www.qemu.org/).
