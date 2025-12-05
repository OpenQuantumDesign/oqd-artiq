# AWG Controller (aqctl_awg)

Controller for Spectrum Instrumentation AWG devices.

## Usage

```bash
aqctl_awg [-h] [-d DEVICE] [-r] [--log LOG] [--bind BIND] [-p PORT] [-v] [-q]
```

### Options

- `-d`, `--device`: Path to SPCM device (default: `/dev/spcm0`)
- `-r`, `--reset`: Reset device before starting
- `--log`: Log file directory (default: `~/.oqd-spectrum-ndsp`)
- `-p`, `--port`: RPC server port (default: `3274`)
- `--bind`: Bind address (default: `::`)
- `-v`, `-q`: Increase/decrease verbosity

### Examples

Run with defaults:
```bash
aqctl_awg
```

Run as background process:
```bash
aqctl_awg &
```

Kill the background process:
```bash
pkill -f aqctl_awg
```

Restart:
```bash
pkill -f aqctl_awg; aqctl_awg &
```

## SPCM Driver Location Issue

The `spcm-core` Python package expects `libspcm_linux.so` from Spectrum Instrumentation to be installed on the system. The driver is **not** bundled with the Python package and must be installed separately.

The library is searched in the following locations (in order):

1. `/usr/lib/x86_64-linux-gnu/libspcm_linux.so`
2. `/usr/local/lib/libspcm_linux.so`
3. `/opt/spcm/drivers/linux/libspcm_linux.so`
4. System library path (`LD_LIBRARY_PATH`)

If the driver is not found, the controller will fail with:
```
OSError: libspcm_linux.so not found in common paths
```

### Resolution

Download and install the SPCM driver from the Spectrum Instrumentation website, then either:

- Copy `libspcm_linux.so` to one of the paths above, or
- Set `LD_LIBRARY_PATH` to include the directory containing the library

## Create Service File

```bash
sudo nano /etc/systemd/system/aqctl-awg.service
```

```ini
[Unit]
Description=ARTIQ AWG Controller (Spectrum NDSP)
After=network.target

[Service]
Type=simple
User=<user>
Environment="LD_LIBRARY_PATH=/opt/spcm/drivers/linux"
ExecStart=/home/<user>/.nix-profile/bin/aqctl_awg
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

!!! note
    Adjust `user`, and the `LD_LIBRARY_PATH` to match your installation.

### Enable and Start

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable on boot
sudo systemctl enable aqctl-awg

# Start service
sudo systemctl start aqctl-awg

# Check status
sudo systemctl status aqctl-awg

# Stop service
sudo systemctl stop aqctl-awg
```