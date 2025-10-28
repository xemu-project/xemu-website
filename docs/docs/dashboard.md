## What is a Dashboard?

The dashboard is the application that runs when the original Xbox is started,
which presents the main menu interface and allows device configuration and
storage management.

## Default xemu Dashboard

The [pre-formatted Xbox HDD image](required-files.md#hard-disk-image),
does not contain the official Xbox dashboard. Instead it contains a lightweight,
open source dashboard with basic functionality: [xemu-dashboard](https://github.com/xemu-project/xemu-dashboard).

It is not strictly required to replace xemu-dashboard with the official Xbox dashboard.
Games can still be launched with xemu-dashboard.

Because xemu-dashboard is unsigned, you may see an error message when
starting xemu with an unmodified retail BIOS image due to the system failing to
find a properly signed dashboard.

## Installing the Official Xbox Dashboard

If you would like to install use the official Xbox dashboard, you will first
need to download the dashboard files from your real Xbox, then transfer them to
the xemu hard disk image.

Because xemu-dashboard provides an FTP server out of the box, this can easily be
done by connecting to xemu-dashboard over FTP to store the desired dashboard files
on the virtual HDD. [See here for more details](ftp.md). Once installed, rebooting
the the desired dashboard should launch.
