from rtl.Blinky import *

from amaranth_boards.ice40_up5k_b_evn import ICE40UP5KBEVNPlatform

def build(setup_kwargs):
    ICE40UP5KBEVNPlatform().build(
        Blinky(),
        synth_opts="-abc9 -dff -spram -dsp",
        do_program=False,
        verbose=True,
    )
