## Frequently Asked Questions

Please check the [list of frequently asked questions](faq.md).

## Black Screen / Failed Load / Dirty Disc

* Check your disc backup and verify that your backup is correct.
* Some games are susceptible to cache problems. Try clearing your cache, or
  simply try with a blank HDD image.
    * You can use the `Flush Cache Partitions` utility in [LithiumX](https://github.com/Ryzee119/LithiumX/) to clear your cache.
    * You can also use the `Clear Cache` function in the [xemu-dashboard](https://github.com/xemu-project/xemu-dashboard) included with the default xemu harddrive image.

## Enabling Surround Sound in your EEPROM

* Surround Sound isn't supported in xemu yet, you should disable this in your [EEPROM](eeprom.md) if you have enabled it.

## Flatpak release will not load the Hard Drive

As explained in the [readme](https://github.com/flathub/app.xemu.Xemu?tab=readme-ov-file#usage): Only `$HOME/.var/app/app.xemu.xemu/data/xemu/xemu` can be written by xemu. The Hard Disk image has to be placed there, for example, at `$HOME/.var/app/app.xemu.xemu/data/xemu/xemu/xbox_hdd.qcow2`. To enable write permissions for the xbox_hdd.qcow2 hard drive file located outside xemu's flatpak system directory, you must grant xemu access to write in an alternative directory. This can be accomplished using either flatpak or flatseal.

Note: This step is not necessary for other system files, such as the BIOS or the MCPX ROM.

### Flatpak
1. `flatpak override app.xemu.xemu --user --filesystem="$HOME/savedgames/xemu/`

### Flatseal
1. Install [Flatseal](https://flathub.org/apps/details/com.github.tchx84.Flatseal)
2. Select <kbd>app.xemu.xemu</kbd>
3. In the <kbd>Filesystem</kbd> section, allow access to the folders your BIOS / MCPX / Hard Drive Image are in

## Windows Compatibility Issues

### Windows 11

**Crash on startup after configuration:** On Windows 11 Insider 23H2, there is an issue with Control Flow Guard being mistakenly enabled. See issue description and workaround [filed here](https://github.com/xemu-project/xemu/issues/1486#issuecomment-1647132796).

### Windows 7

!!! warning "Windows 7 is not officially supported"

    Windows 7 is no longer officially supported. xemu is not officially supported on Windows 7.

That said, xemu has been run on Windows 7 in the past. If you simply must run xemu on Windows 7, here are some tips that may help you:

**api-ms-win-core-path-l1-1-0.dll:** If you get a message for this missing DLL, see the workaround [filed here](https://github.com/xemu-project/xemu/issues/1482).

## Windows Performance Considerations

### Powersave vs Performance Power Management Profile

Ensure your computer is using a Performance power management profile. If you are using a laptop, connect your AC adapter to prevent throttling.

### Background Processes

Ensure any background processes are not consuming your system resources by checking the system task manager.

### Integrated vs Discrete GPU

In some systems you may have both integrated and discrete GPUs. By default, xemu
will request the high-performance discrete GPU. However, system configuration
and your graphics driver ultimately decide which GPU xemu is initialized with.

In Windows, you can specify which GPU should be used for a particular
application by navigating to <kbd>Display settings</kbd>&rarr;<kbd>Graphics settings</kbd>.

You can confirm which GPU xemu is actually using by looking at the "xemu.log"
file.

### Nvidia Settings

It is recommended to **disable** "Multi-threaded Optimizations" in the nVidia
Control Panel. This feature has been known to negatively impact xemu
performance.

## Linux Performance Considerations

### CPU Performance Scaling

You may want to check that your CPU scaling governor is set to `performance`.
In a terminal enter the following command to see current governor state:

```bash
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

If you see `powersave` printed, you may wish to switch to the `performance`
profile. To select the `performance` profile:

```bash
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

## Switchroot

If you are running switchroot Linux on your Nintendo Switch, you can install
xemu from the PPA as described in in the [Download](download.md) page. However,
when running xemu you may see the following error:

```
dbus[12047]: arguments to dbus_message_new_method_call() were incorrect, assertion "path != NULL" failed in file ../../../dbus/dbus-message.c line 1362.
This is normally a bug in some application using the D-Bus library.

  D-Bus not built with -rdynamic so unable to print a backtrace
```

To fix this you can build and install SDL from source:

```bash
sudo apt install cmake build-essential
git clone https://github.com/libsdl-org/SDL && cd SDL
mkdir build && cd build
cmake ..
make -j4
sudo make install
```

Then launch xemu `LD_LIBRARY_PATH=/usr/local/lib xemu`
