# Networking

Xbox networking is fully supported. Connect to other instances of xemu and even
real Xboxes, locally or over the Internet.

There are three network backends available to choose from in the xemu Network
configuration dialog: NAT, UDP Tunnel, and Bridged Adapter. Which one
you should select depends on what you'd like to do.

## Attachments

### Bridged Adapter

!!! info "Useful for..."
    * Connecting to one or more real Xboxes on your local network
    * Connecting to a popular tunneling service such as Xlink Kai

In this networking mode, the emulated network device is bridged to one of the
network interfaces on your machine. This means that all traffic sent from the
emulated network controller will be forwarded to your selected network
interface, and xemu can receive traffic incoming on this interface.

With this mode you can easily set up a System Link session with a real Xbox by
just connecting the Xbox to your computer with an Ethernet cable. Additionally,
this mode can be used to connect with tunneling services.

### UDP Tunnel

!!! info "Useful for..."
    * Playing with other xemu users over the Internet

In this networking mode, all traffic that would be sent/received by the emulated
NIC is simply encapsulated in UDP datagrams and forwarded to a remote host,
which could be another instance of xemu or perhaps a real Xbox (see
[l2tunnel](https://github.com/mborgerson/l2tunnel) for more information). This is useful
for quickly setting up a virtual LAN.

The xemu project provides multiple free servers you can use to play with other
xemu users. Join the Discord community for more information.

### NAT

!!! info "Useful for..."
	* Providing Internet access to Xbox software
	* Connecting to Xbox software from your host machine

In this networking mode, a full TCP/IP stack is running within xemu, and network
address translation is used to route packets between the internal network and
the outside world.

Like a router you may have at home, you can have xemu listen on specific ports
and perform 'port forwarding' to the virtual Xbox. This can be used for example
to connect to the virtual Xbox's FTP server. Find more info about port
forwarding and FTP access [here](ftp.md).


## Troubleshooting

### System Link session is not joinable

* Ensure all MAC addresses are unique. If you are using an EEPROM dumped from your real Xbox, xemu and your Xbox will have the same MAC address. You'll need to change one of them. You can blank the EEPROM line in xemu's Settings window to have it generate a new one for you, or you can use the [EEPROM editor](https://github.com/Ernegien/XboxEepromEditor) to change it.
* Ensure the game versions/regions/updates between the people playing are the same.
* If you are on Windows, ensure you're using the new [npcap](https://nmap.org/npcap/) with WinPcap API-compatible mode, not the older WinPcap.
* Some Realtek cards have been known to be problematic. Try reinstalling your driver or use an alternative adapter.

### My network adapter is not listed
* If you are on Windows, ensure you're using the new [npcap](https://nmap.org/npcap/) with WinPcap API-compatible mode, not the older WinPcap.

### Bridged Adapter Permission Problems

**Important:** You should **never** need to run xemu as the `root` user.

#### macOS

If you get a permission error when attempting to enable Bridged Adapter,
you may need to update the `/dev/bpfX` permissions on your system. You can
work around this by opening a terminal and executing the following command:

```bash
sudo chown $(whoami):admin /dev/bpf*
```

#### Linux

If you get a permission error when attempting to enable Bridged Adapter,
you may need to update the executable capabilities to provide raw access
to your network interface. You can do so with the following command:

```bash
sudo setcap cap_net_raw,cap_net_admin=eip `which xemu`
```
