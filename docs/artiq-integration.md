# ARTIQ Integration

Guide for integrating the Spectrum AWG with ARTIQ experiments

## Prerequisites

1. ARTIQ installation with sipyco
2. Spectrum spcm driver installed
3. AWG card accessible at `/dev/spcm0` (or configured path)

## Controller Setup

Starting the Controller

### As a service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable aqctl-awg
sudo systemctl start aqctl-awg
```

### In a terminal shell:

```bash
aqctl_awg -d /dev/spcm0 -p 3274
```

**Arguments:**

- `-d, --device` - Device path (default: `/dev/spcm0`)
- `-p, --port` - RPC port (default: 3274)
- `-r, --reset` - Reset device on startup
- `--bind` - Bind address
- `-v, -vv` - Verbosity level

## Device Database

Add to `device_db.py`:

```python
device_db["awg"] = {
    "type": "controller",
    "host": "::1",
    "port": 3274,
}
```

### Remote Controller

For a controller running on another machine:

```python
device_db["awg"] = {
    "type": "controller",
    "host": "192.168.1.100",
    "port": 3274,
}
```
Where the host is the IP Address of the device connected to the Spectrum AWG.

## Experiment Usage

### Basic Example

```python
from artiq.experiment import *

class AWG_Basic(EnvExperiment):
    def build(self):
        self.setattr_device("awg")

    def run(self):
        # Configure card
        self.awg.card_mode("dds")
        self.awg.channels_enable(True)
        self.awg.channels_output_load(50)
        self.awg.channels_amp(0.5)
        
        # Setup trigger
        self.awg.trigger_or_mask("ext0")
        self.awg.trigger_ext0_mode("pos")
        self.awg.trigger_ext0_level0(0.5)
        self.awg.trigger_ext0_coupling("dc")
        
        # Write setup
        self.awg.write_setup()
        self.awg.reset()
        
        # Configure DDS
        self.awg.dds_data_transfer_mode("dma")
        self.awg.dds_trg_src("card")
        
        # Set channel parameters
        self.awg.dds_channel_freq(0, 1e6)
        self.awg.dds_channel_amp(0, 0.5)
        
        # Execute
        self.awg.dds_exec_at_trg()
        self.awg.dds_write_to_card()
        self.awg.start("enable_trigger")
```

