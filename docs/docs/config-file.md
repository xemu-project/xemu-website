## Paths

The default xemu configuration file can be found at the following locations after first run:

| OS | Path |
|----|------|
| Linux | `~/.local/share/xemu/xemu/xemu.ini` |
| macOS |  |
| Windows |  |


## Default `xemu.ini` File

The default configuration file looks like this:

```ini
[system]
flash_path = 
bootrom_path = 
hdd_path = 
eeprom_path = 
dvd_path = 
memory = 64
shortanim = false
hard_fpu = true
[audio]
use_dsp = false
[display]
scale = scale
ui_scale = 1
render_scale = 1
[input]
controller_1_guid = 
controller_2_guid = 
controller_3_guid = 
controller_4_guid = 
[network]
enabled = false
backend = user
local_addr = 0.0.0.0:9368
remote_addr = 1.2.3.4:9368
pcap_iface = 
[misc]
user_token = 
check_for_update = 
```
