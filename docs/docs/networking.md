# Networking

xemu emulates the Xbox network controller, and being built on top of QEMU's
robust networking support infrastructure, provides a flexible array of advanced
network configuration options. There are three network backends exposed in the
Network configuration window for xemu: NAT, UDP Tunnel, and Bridged Adapter.

## Attachments

### NAT

In this networking mode, a full TCP/IP stack is running within xemu, and network
address translation is used to route packets between the internal network and
the outside world.

### UDP Tunnel

In this networking mode, all traffic that would be sent/received by the emulated
NIC is simply encapsulated in UDP datagrams and forwarded to a remote host,
which could be another instance of xemu or perhaps a real Xbox (see
[l2tunnel](github.com/mborgerson/l2tunnel) for more information). This is useful
for quickly setting up a virtual LAN.

### Bridged Adapter

In this networking mode, the emulated NIC is bridged to one of the network
interfaces on your machine. This means that all traffic sent from the emulated
network controller will be forwarded to your selected network interface, and
xemu can receive traffic incoming on this interface. With this mode you can
easily set up a System Link session with a real Xbox by just connecting the Xbox
to your computer with an Ethernet cable. Additionally, this mode can be used to
connect with tunneling services.

## Troubleshooting

### System Link session is not joinable

* Ensure all MAC addresses are unique. If you are using an EEPROM dumped from your real Xbox, xemu and your Xbox will have the same MAC address. You'll need to change one of them. You can blank the EEPROM line in xemu's Settings window to have it generate a new one for you, or you can use the [EEPROM editor](https://github.com/Ernegien/XboxEepromEditor) to change it.
* Ensure the game versions/regions/updates between the people playing are the same.
* If you are on Windows, ensure you're using the new [npcap](https://nmap.org/npcap/), not the older WinPcap.
* Some Realtek cards have been known to be problematic. Try using an alternative adapter.

### My network adapter is not listed
* If you are on Windows, ensure you're using the new [npcap](https://nmap.org/npcap/), not the older WinPcap.

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
