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
