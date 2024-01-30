import setuptools, os
from amaranth_boards.ice40_up5k_b_evn import ICE40UP5KBEVNPlatform
from rtl.Blinky import *

def build(setup_kwargs) -> int:
    # https://github.com/python-poetry/poetry/issues/2051#issuecomment-942049444
    setuptools.setup(
        **setup_kwargs, 
        script_args = ['bdist_wheel'],
        options = { 
            'bdist_wheel': {
                'plat_name': os.getenv('PP_PYTHON_TARGET', 'any')
            }
        }
    )

    ICE40UP5KBEVNPlatform().build(
        Blinky(),
        synth_opts='-abc9 -dff -spram -dsp',
        build_dir='synth',
        do_program=False,
        verbose=True,
    )
