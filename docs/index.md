# OQD Spectrum NDSP

ARTIQ Network Device Support Package for Spectrum Instrumentation AWG devices

## Overview

The package implements:

- **AWGDriver**: Direct hardware control via SPCM
- **AWGMediator**: RPC client for
- **aqctl_awg**: ARTIQ controller process

## Documentation

- [ARTIQ Integration](artiq-integration.md) - Setup and usage guide

## Installation

```bash
pip install git+https://github.com/OpenQuantumDesign/oqd-spectrum-ndsp
```

### Dependencies

- Python 3.10+
- [spcm](https://github.com/SpectrumInstrumentation/spcm) - Spectrum driver library
- [sipyco](https://github.com/m-labs/sipyco) - ARTIQ RPC framework

## Quick Start

### Create a virtual environment
```bash
python3 -m venv .
source .venv/bin/activate
```

### Install the requirements
```bash
pip3 install -r requirements.txt
```

### Add to device_db.py

```python
device_db["awg"] = {
    "type": "controller",
    "host": "::1",
    "port": 3274,
}
```

### Start the Controller

```bash
aqctl_awg -d /dev/spcm0 -p 3274
```

### Run the experiment file

```bash
cd experiments
artiq_run simple_exp.artiq.py
```
## API Quick Reference

**Card**
> `card_mode`, `write_setup`, `start`, `stop`, `timeout`, `get_i`, `get_d`, `set_i`, `set_d`, `close`

**Channels**
> `channels_enable`, `channels_amp`, `channels_output_load`

**Trigger**
> `trigger_or_mask`, `trigger_and_mask`, `trigger_delay`, `trigger_ext0_mode`, `trigger_ext0_level0`, `trigger_ext0_coupling`, `trigger_ext1_*`

**DDS**
> `reset`, `dds_data_transfer_mode`, `dds_trg_src`, `dds_trg_timer`, `dds_exec_at_trg`, `dds_write_to_card`

**DDS Channel**
> `dds_channel_freq`, `dds_channel_amp`, `dds_channel_phase`, `dds_channel_amplitude_slope`, `dds_channel_freq_slope`

**Clock**
> `clock_sample_rate`
