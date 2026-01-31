Like attaching an emulated controller, you can attach a virtual keyboard. A graphical interface to attach this emulated peripheral is not available yet, however you can easily add it by opening the Monitor (`~` key) and entering in the following command:

```
device_add usb-kbd,port=1.x,id=kbd
```

where the `x` after the `port` should be replaced with one of 3,4,1,2 for player 1,2,3,4 respectively.

To remove the device:

```
device_del kbd
```
