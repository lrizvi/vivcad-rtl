from Blinky import *

from amaranth_boards.ice40_up5k_b_evn import ICE40UP5KBEVNPlatform

if __name__ == "__main__":
    ICE40UP5KBEVNPlatform().build(
        Blinky(),
        synth_opts="-abc9 -dff -spram -dsp",
        do_program=False,
        verbose=True,
    )
