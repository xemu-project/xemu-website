xemu requires game discs to be in the form of ".iso" disc images. You can
backup your legally purchased games by:

* Using a real Xbox with a custom dashboard to transfer the game files to your
  computer over FTP.
* Purchasing and using a special, reflashed DVD drive. [More details here](http://wiki.redump.org/index.php?title=Microsoft_Xbox_and_Xbox_360_Dumping_Guide).

You can create an iso image using [extract-xiso](https://github.com/XboxDev/extract-xiso) (command-line only).

### About "redump" ISOs

Redump-style ISOs contain data for both the video partition and game partition. For now,
you'll want to extract the game partition for use with xemu. You can do this by simply
extracting everything after the first 387MiB. For example, using `dd`:

```
dd if=my-redump-style-dump.iso of=my-game-partition.iso skip=387 bs=1M
```

You can then use the `my-game-partition.iso` with xemu.
