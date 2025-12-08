# OQD Spectrum NDSP

ARTIQ Network Device Support Package (NDSP) for Spectrum Instrumentation AWG devices.

## Installation

```bash
pip install git+https://github.com/OpenQuantumDesign/oqd-spectrum-ndsp
```

**Requirements:** Python 3.10+, [spcm](https://github.com/SpectrumInstrumentation/spcm) driver

## Setup

Add to `experiments/device_db.py`
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

### Run the ARTIQ Experiment
```bash
cd experiments
artiq_run simple_exp.artiq.py
```

## API Overview
The driver provides methods organized by functionality:

**Card** - Card control and configuration
> `card_mode`, `start`, `stop`, `write_setup`, `timeout`

**Channels** - Output channel settings
> `channels_enable`, `channels_amp`, `channels_output_load`

**Trigger** - Trigger configuration
> `trigger_or_mask`, `trigger_ext0_mode`, `trigger_ext0_level0`, `trigger_delay`

**DDS** - DDS core control
> `reset`, `dds_trg_src`, `dds_trg_timer`, `dds_exec_at_trg`, `dds_write_to_card`

**DDS Channel** - Per-channel DDS parameters
> `dds_channel_freq`, `dds_channel_amp`, `dds_channel_phase`, `dds_channel_amplitude_slope`, `dds_channel_freq_slope`

**Clock** - Sample rate configuration
> `clock_sample_rate`

**Register** - Direct register access
> `get_i`, `get_d`, `set_i`, `set_d`

### Usage in Experiments

Methods accept strings instead of SPCM constants:

```python
# Instead of spcm.SPC_REP_STD_DDS
self.awg.card_mode("dds")

# Instead of spcm.SPC_TMASK_EXT0
self.awg.trigger_or_mask("ext0")

# Instead of spcm.SPC_TM_POS
self.awg.trigger_ext0_mode("pos")
```

## Source Structure

```
oqd-spectrum-ndsp/
├── src/artiq/
│   ├── devices/awg/
│   │   ├── driver.py           # AWGDriver - hardware interface via spcm
│   │   └── mediator.py         # AWGMediator - RPC client wrapper
│   └── frontend/
│       └── aqctl_awg.py        # Controller entry point (sipyco server)
└── experiments/
    ├── device_db.py            # Device database
    └── simple_exp.artiq.py     # Example experiment
```

## Documentation

To deploy the documentation locally, implemented with [mkdocs](https://www.mkdocs.org/), run the following commands:

```bash
pip install .[docs]
mkdocs serve
```

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.