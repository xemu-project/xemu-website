## What is a Dashboard?

The dashboard is the application that runs when the original Xbox is started,
which presents the main menu interface and allows device configuration and
storage management.

## Default xemu Dashboard

The [pre-formatted Xbox HDD image](required-files.md#hard-disk-image),
does not contain the official Xbox dashboard. Instead it contains only an
**unsigned** "dummy" dashboard, intended to be replaced.

It is not strictly required to replace the dummy dashboard. Games can still be
launched with the dummy dashboard installed.

Because the dummy dashboard is unsigned, you may see an error message when
starting xemu with an unmodified retail BIOS image due to the system failing to
find a properly signed dashboard.

## Installing the Official Xbox Dashboard

If you would like to install use the official Xbox dashboard, you will first
need to download the dashboard files from your real Xbox, then transfer them to
the xemu hard disk image.

This can easily be done by running an alternative dashboard which exposes
an FTP server. [See here for more details](ftp.md).

## Alternative Dashboards

It is not required to use the official Xbox dashboard. There are alternatives
available, such as the open-source dashboard
[NevolutionX](https://github.com/dracc/nevolutionx).
