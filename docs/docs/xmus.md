xemu allows inserting XMUs (Xbox Memory Units) to controller hubs.

This is done by using a file as the storage medium. Any file bigger than 1 MiB in size should work.


## Creating the XMU

Open up the Monitor, and type in these commands:

```
drive_add 0 if=none,id=usbdisk1,file="your_filename"
stop
device_add usb-storage,drive=usbdisk1,port=1.3.2
cont
```

and replace "your_filename" with a path to your XMU file.

You may additionally change the controller you're inserting this XMU to.

Replace the value of `port` with `1.x.2` where x is one of `3, 4, 1, 2` for players `1, 2, 3, 4` respectively.

## Creating an XMU file
The XMU file may be any file that's bigger than 1 MiB. If you don't want to sacrifice another file, you may create one with tools like `fsutil` on Windows, or `dd` on Linux:

Windows:
```
fsutil file createnew filename size
```

Replace `filename` with your desired file name, and `size` with a size bigger than 1 MiB. For example, use `33554432` to create a 32 MiB file.

Linux:
```
dd if=/dev/zero of=filename bs=32MB count=1
```

Same as windows
