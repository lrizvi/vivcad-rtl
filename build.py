import setuptools, os
from pybind11.setup_helpers import Pybind11Extension, build_ext
from amaranth_boards.ice40_up5k_b_evn import ICE40UP5KBEVNPlatform
from rtl.Blinky import *

def build(setup_kwargs) -> int:
    setup_kwargs.update({
        'ext_modules': [
            Pybind11Extension(
                'ciccomp',
                [
                    'src/ciccomp/band.cpp',
                    'src/ciccomp/barycentric.cpp',
                    'src/ciccomp/cheby.cpp',
                    'src/ciccomp/eigenvalue.cpp',
                    'src/ciccomp/main.cpp',
                    'src/ciccomp/pm.cpp',
                ],
                include_dirs = [
                    'include',
                ],
                extra_compile_args = [
                    '-O3'
                ],
                extra_link_args = [
                    '-Bstatic -lgomp -lmpfr'
                ],
                language = 'c++',
                cxx_std = 11
            ),
        ],
        'cmd_class'  : {'build_ext': build_ext},
        'zip_safe'   : False,
    })
    
    # https://github.com/python-poetry/poetry/issues/2051#issuecomment-942049444
    # setuptools.setup(
    #     **setup_kwargs, 
    #     script_args = ['bdist_wheel'],
    #     options = { 
    #         'bdist_wheel': {
    #             'plat_name': os.getenv('PP_PYTHON_TARGET', 'any')
    #         }
    #     }
    # )

    ICE40UP5KBEVNPlatform().build(
        Blinky(),
        synth_opts='-abc9 -dff -spram -dsp',
        build_dir='synth',
        do_program=False,
        verbose=True,
    )
