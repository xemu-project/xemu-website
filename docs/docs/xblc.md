There is preliminary support for Xbox Live Communicator emulation, for voice communication in games that support it. A graphical interface to attach this emulated peripheral is not available yet, however you can easily add it by opening the Monitor (`~` key) and entering in the following command:

```
device_add usb-xblc,port=1.x.2,id=xblc
```

where the `x` after the `port` should be replaced with one of 3,4,1,2 for player 1,2,3,4 respectively.

To remove the device:

```
device_del xblc
```

## Troubleshooting

* You may only attach a Communicator to controllers that do not have an MMU assigned in the first expansion slot. Attempting to do so will print an error like `Error: usb port 1.3.2 (bus usb-bus.1) not found (in use?)`. Simply remove the MMU in xemu's `Input` settings page (or you may move it to the second expansion slot).
* You can use `info usb` to print information about the attached devices to verify that the Communicator was added correctly.
  
