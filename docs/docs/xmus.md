xemu allows inserting Xbox Memory Units, aka Memory Cards, in to controller hubs. There is not yet a convenient user interface to do this, but it can be done easily enough with a few short commands in the Monitor.

## Creating an XMU image

Like the virtual hard disk, an XMU is backed by an image file. Create an 8 MiB XMU image using one of the following commands, depending on your platform.

=== "Windows"

	```
	fsutil file createnew xmu.img 8388608
	```

=== "Linux"

	```
	fallocate -l 8388608 xmu.img
	```

	or

	```
	dd if=/dev/zero of=img.img bs=8MB count=1
	```

## Creating and "Inserting" an XMU device

Open up the Monitor, and type in these commands:

```
drive_add 0 if=none,id=usbdisk1,file="xmu.img"
stop
device_add usb-storage,drive=usbdisk1,port=1.3.2
cont
```

You may additionally change the controller you're inserting this XMU to.

Replace the value of `port` with `1.x.2` where x is one of `3, 4, 1, 2` for players `1, 2, 3, 4` respectively.
