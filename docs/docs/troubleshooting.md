## Frequently Asked Questions

Please check the [list of frequently asked questions](faq.md).

## Black Screen / Failed Load / Dirty Disc

* Check your disc backup and verify that your backup is correct.
* Some games are susceptible to cache problems. Try clearing your cache, or
  simply try with a blank HDD image.

## Windows Performance Considerations

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
