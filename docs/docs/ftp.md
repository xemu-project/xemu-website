# HDD Access via FTP

If you have an alternative dashboard that runs an FTP server (as almost all
replacement dashboards do), you can easily connect to that FTP server to read
or write files on the virtual hard disk.

## Step 1: Enable user networking

In xemu, open the Network window by navigating to
<kbd>Machine</kbd>&rarr;<kbd>Network</kbd>. If networking is currently
enabled, click <kbd>Disable</kbd>. From the "Attached To" combo box, select
"NAT", then click <kbd>Enable</kbd>.

## Step 2: Forward port 21

Because xemu is configured to use "user networking," we must configure xemu
to forward FTP traffic on the host machine to the internal network. There is
not a fancy GUI to do this yet, but we can easily do this using the monitor.

In xemu, open the Monitor window by navigating to
<kbd>Debug</kbd>&rarr;<kbd>Monitor</kbd>. In the box at the bottom of the
Monitor window, paste the following command and press <kbd>Enter</kbd>:

```
hostfwd_add xemu-netdev tcp:127.0.0.1:2121-:21
```

Now xemu will begin listening on TCP port 2121 for new connections, and forward
that traffic to the internal network.

## Step 3: Launch your alternative dashboard from disc

Assuming you have a copy of your alternative dashboard in the form of an ISO
image, load the disc image. You may need to reset the system to get it to
load. Double check the networking settings for your dashboard to make sure
that it is configured to use DHCP.

See NevolutionX for a FOSS alternative dashboard that supports FTP [here](https://github.com/dracc/NevolutionX).

## Step 4: Connect using your FTP client
The [Filezilla FTP client](https://filezilla-project.org/) is recommended. It
is an open-source client available for all major platforms. If you would
prefer to use another client, look for the respective settings in your client
mentioned in this section.

Now, assuming that you are using Filezilla, start the client. Let's first
create a new "Site" by navigating to <kbd>File</kbd> &rarr; <kbd>Site
Manager</kbd>, then in the "Site Manager" window, click the <kbd>New
Site</kbd> button.

* Enter "xemu" for the site name
* For "Host" enter `127.0.0.1` and for "Port" enter `2121`
* For "Encryption" select "Only use plain FTP (insecure)"
* For "Logon Type" select "Normal"
* Enter the appropriate "User" and "Password" (typically `xbox` for both)
* Navigate to the "Transfer Settings" tab and select "Active"
* Check "Limit number of simultaneous connections" and set Max Connections to 1
* Click <kbd>OK</kbd> when you are finished

We must configure one more additional setting.

* Navigate to the settings window via <kbd>Edit</kbd> &rarr; <kbd>Settings...</kbd>
* On the left-hand side, navigate to <kbd>Connection</kbd> &rarr; <kbd>FTP</kbd> &rarr; <kbd>Active mode</kbd>
* In the "Active mode IP" group, select "Use the following IP address:" and enter `10.0.2.2`
* **Uncheck** "Don't use external IP address on local connections."
* Click <kbd>OK</kbd> when you are finished

You can now open the "Site Manager" window again, select "xemu", and click the <kbd>Connect</kbd> button.

<details>
<summary>More details about the FTP protocol for the curious...</summary>
FTP has two modes: passive and active.

Passive mode involves the client first connecting to the server for control and
then again on another port other for data. The client first connects, then the
server gives it another address and port to connect to for data. The first
problem with this is that the server reports to the client the only IP address
that it knows (10.0.2.15) which is not correct for our needs--we need 127.0.0.1.
That's alright because we can override this in Filezilla. The second problem is
that we don't know which port the server is going to choose, so we can't forward
it ahead of time.

In active mode, the client first connects to the server, then the server
connects to the client! The client needs to give the IP address for the server
to connect to. By default, it will give your computer's IP address, but the
guest cannot connect to using that IP. So instead we need to override this
setting and provide the IP address that the guest should connect to to actually
connect to the host, which is 10.0.2.2.
</details>

Note: To prevent interference with other FTP servers that you might connect to,
you may want to adjust your settings and disable the "Active mode IP" override
when you have finished transferring files.
