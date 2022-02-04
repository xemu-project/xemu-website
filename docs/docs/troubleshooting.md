## Frequently Asked Questions

Please check the [list of frequently asked questions](faq.md).

## Black Screen / Failed Load / Dirty Disc

* Check your disc backup and verify that your backup is correct.
* Some games are susceptible to cache problems. Try clearing your cache, or
  simply try with a blank HDD image.

## Enabling Surround Sound in your EEPROM

* Surround Sound isn't supported in xemu yet, you should disable this in your [EEPROM](eeprom.md) if you have enabled it.

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

## Switchroot/Jetson setup

If you are running Switchroot/L4T Ubuntu on your Nintendo Switch or Jetson device, you can install
xemu from the PPA as described in in the [Download](download.md) page. However, this is generally **not recommended** for performance reasons.
Instead of using the PPA, it's recommended to install xemu via the [L4T Megascript](https://github.com/cobalt2727/L4T-Megascript/wiki)'s build script (use Option A for Switch users, or Option B for Jetson Nano/other users).
During their "initial setup" script, you'll be prompted to install SDL2 - choose yes to upgrade to newer SDL2 binaries. Afterwards, you can install xemu itself from the menu.
The Megascript's [build script](https://github.com/cobalt2727/L4T-Megascript/blob/master/scripts/games_and_emulators/xemu.sh) has been confirmed to result in a slight speed boost over the PPA, but it is not packaged by the xemu developers. Use at your own discretion.

If you see the following error, this is a [bug](https://github.com/mborgerson/xemu-website/commit/b6b8227a0b986176ae7d1d57e506751628ecceaf#commitcomment-63959699) from older releases of Switchroot's L4T Ubuntu:
```bash
dbus[12047]: arguments to dbus_message_new_method_call() were incorrect, assertion "path != NULL" failed in file ../../../dbus/dbus-message.c line 1362.
This is normally a bug in some application using the D-Bus library.

  D-Bus not built with -rdynamic so unable to print a backtrace
```

This can be fixed by building a newer SDL2 from source or pasting the following into a terminal:
```bash
# check for bad machine-id from 3.0.0 L4T Ubuntu image and fix if necessary
# also generate if user has somehow deleted their machine-id as well
if [[ $(cat /var/lib/dbus/machine-id) == "52e66c64e2624539b94b31f8412c6a7d" ]]; then
  sudo rm /var/lib/dbus/machine-id && dbus-uuidgen | sudo tee /var/lib/dbus/machine-id
elif [[ ! -f /var/lib/dbus/machine-id ]]; then
  dbus-uuidgen | sudo tee /var/lib/dbus/machine-id
fi
```
Then launch xemu by typing `./xemu` from a "dist" folder inside the git folder at `xemu/dist/` after successfully building (or if using the Megascript, simply launch Xemu from your app list).
