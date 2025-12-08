import time
from artiq.experiment import *


class SimplePulse(EnvExperiment):
    def build(self):
        self.setattr_device("awg")

    def run(self):
        self.awg.card_mode("dds")
        self.awg.channels_enable(True)
        self.awg.channels_output_load(50)
        self.awg.channels_amp(0.5)
        self.awg.trigger_or_mask("ext0")
        self.awg.trigger_ext0_mode("pos")
        self.awg.trigger_ext0_level0(0.5)
        self.awg.trigger_ext0_coupling("dc")
        self.awg.write_setup()
        self.awg.reset()
        self.awg.dds_data_transfer_mode("dma")
        self.awg.dds_trg_src("card")
        self.awg.dds_channel_freq(0, 1000)
        self.awg.dds_channel_amp(0, 0.5)
        self.awg.dds_exec_at_trg()
        self.awg.dds_write_to_card()
        self.awg.start("enable_trigger")
        time.sleep(30.0)  # Wait 30 seconds
        self.awg.stop()

