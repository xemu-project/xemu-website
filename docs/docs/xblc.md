There is preliminary support for Xbox Live Communicator emulation, for voice communication in games that support it. A graphical interface to attach this emulated peripheral is not available yet, however you can easily add it by opening the Monitor (`~` key) and entering in the following command:

```
device_add usb-xblc,port=1.x.2,id=xblc
```

where x = 3,4,1,2 for player 1,2,3,4 respectively.

To remove the device:

```
device_del xblc
```