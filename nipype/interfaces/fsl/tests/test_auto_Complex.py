# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.utils import Complex
def test_Complex_inputs():
    input_map = dict(real_cartesian=dict(position=1,
    xor=['real_polar', 'real_cartesian', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge'],
    argstr='-realcartesian',
    ),
    end_vol=dict(position=-1,
    argstr='%d',
    ),
    complex_split=dict(position=1,
    xor=['real_polar', 'real_cartesian', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge'],
    argstr='-complexsplit',
    ),
    start_vol=dict(position=-2,
    argstr='%d',
    ),
    complex_cartesian=dict(position=1,
    xor=['real_polar', 'real_cartesian', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge'],
    argstr='-complex',
    ),
    real_polar=dict(position=1,
    xor=['real_polar', 'real_cartesian', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge'],
    argstr='-realpolar',
    ),
    imaginary_out_file=dict(position=-3,
    genfile=True,
    argstr='%s',
    xor=['complex_out_file', 'magnitude_out_file', 'phase_out_file', 'real_polar', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge'],
    ),
    phase_out_file=dict(position=-3,
    genfile=True,
    argstr='%s',
    xor=['complex_out_file', 'real_out_file', 'imaginary_out_file', 'real_cartesian', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge'],
    ),
    complex_merge=dict(position=1,
    xor=['real_polar', 'real_cartesian', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge', 'start_vol', 'end_vol'],
    argstr='-complexmerge',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    magnitude_out_file=dict(position=-4,
    genfile=True,
    argstr='%s',
    xor=['complex_out_file', 'real_out_file', 'imaginary_out_file', 'real_cartesian', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge'],
    ),
    args=dict(argstr='%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    complex_in_file=dict(position=2,
    argstr='%s',
    ),
    magnitude_in_file=dict(position=2,
    argstr='%s',
    ),
    complex_out_file=dict(position=-3,
    genfile=True,
    argstr='%s',
    xor=['complex_out_file', 'magnitude_out_file', 'phase_out_file', 'real_out_file', 'imaginary_out_file', 'real_polar', 'real_cartesian'],
    ),
    real_in_file=dict(position=2,
    argstr='%s',
    ),
    complex_polar=dict(position=1,
    xor=['real_polar', 'real_cartesian', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge'],
    argstr='-complexpolar',
    ),
    real_out_file=dict(position=-4,
    genfile=True,
    argstr='%s',
    xor=['complex_out_file', 'magnitude_out_file', 'phase_out_file', 'real_polar', 'complex_cartesian', 'complex_polar', 'complex_split', 'complex_merge'],
    ),
    imaginary_in_file=dict(position=3,
    argstr='%s',
    ),
    complex_in_file2=dict(position=3,
    argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    phase_in_file=dict(position=3,
    argstr='%s',
    ),
    output_type=dict(),
    )
    inputs = Complex.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Complex_outputs():
    output_map = dict(magnitude_out_file=dict(),
    phase_out_file=dict(),
    real_out_file=dict(),
    imaginary_out_file=dict(),
    complex_out_file=dict(),
    )
    outputs = Complex.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value