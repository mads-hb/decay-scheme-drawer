# overview of level distributions, as reported in ENSDF jan 2015, relevant to B+ decay of 21Mg
from decay_scheme import *

ds = decay_scheme()

Ea17f = 6.561
a17f = nuclide(0, "a+17F")
a17f.add_level(level(Ea17f, '5/2', '+', lw=2.0, text_below='$\mathrm{\\alpha+^{17}F}$', draw_reference_line=True))
a17f.add_level(level(Ea17f+0.495, '1/2', '+'))

Ep20ne = 2.431
p20ne = nuclide(1, "p+20Ne")
p20ne.add_level(level(Ep20ne, '0', '+', lw=2.0, text_below='$\mathrm{p+^{20}Ne}$', draw_reference_line=True))
p20ne.add_level(level(Ep20ne+1.633, '2', '+'))
p20ne.add_level(level(Ep20ne+4.247, '4', '+'))
p20ne.add_level(level(Ep20ne+4.966, '2', '-', energy_spin_parity_below=True, energy_y_adjust=+0.08, spin_parity_y_adjust=+0.08))
p20ne.add_level(level(Ep20ne+5.621, '3', '-', energy_spin_parity_below=True))
p20ne.add_level(level(Ep20ne+5.787, '1', '-'))

na21 = nuclide(2, "21Na")
na21.add_level(level(0., '3/2', '+', lw=2.0, text_below='$\mathrm{^{21}Na}$', energy_spin_parity_below=True))
na21.add_level(level(0.332, '5/2', '+', color='C0'))
na21.add_level(level(1.716, '7/2', '+', energy_spin_parity_below=True, color='C0'))
na21.add_level(level(2.424, '1/2', '+', energy_spin_parity_below=True))
na21.add_level(level(2.798, '1/2', '-', lw=0.5, energy_spin_parity_below=True, energy_y_adjust=+0.05, spin_parity_y_adjust=+0.05))
na21.add_level(level(2.829, '9/2', '+', lw=0.5, color='C0'))

na21.add_level(level(3.544, '', '', many=True, upper_energy=4.468, hide_energy_spin_parity=True))
ds.add_freetext(freetext('$\\leftarrow$', x=4.1, y=3.544+(4.468-3.544)/2 - 0.3))
ds.add_freetext(freetext('4.468 $3/2^{+}$, ' +
                         '4.294 $5/2^{+}$, ' +
                         '4.170 $3/2^{-}$\n' +
                         '3.862 $5/2^{-}$, ' +
                         '3.679 $3/2^{-}$, ' +
                         '3.544 $5/2^{+}$', x=4.2, y=3.544+(4.468-3.544)/2 - 0.55, ha='left', va='center'))

na21.add_level(level(4.419, '(11/2)', '(+)', energy_spin_parity_below=True, color='C0', lw=0.5, hide_energy_spin_parity=True))

na21.add_level(level(4.984, '', '', many=True, upper_energy=5.457, hide_energy_spin_parity=True))
ds.add_freetext(freetext('$\\nwarrow$', x=4.1, y=4.984+(5.457-4.984)/2 - 0.2, rotation=20.))
ds.add_freetext(freetext('5.457 $1/2^{+}$, ' +
                         '5.380 $I_{\pm}$\n' +
                         '5.020 $I_{\pm}$,     ' +
                         '4.984 $1/2^{-}$', x=4.2, y=4.984+(5.457-4.984)/2 - 0.65, ha='left', va='center'))

na21.add_level(level(5.770, '', '', many=True, upper_energy=6.468, hide_energy_spin_parity=True))
ds.add_freetext(freetext('$\\leftarrow$', x=4.1, y=5.770+(6.468-5.770)/2 + 0.25))
ds.add_freetext(freetext('6.468 $3/2^{+}$, ' +
                         '6.341 $I_{\pm}$,     ' +
                         '6.165 $I_{\pm}$\n' +
                         '6.070 $\\widetilde{I}_\pm$,    ' +
                         '5.979 $I_{\pm}$,     ' +
                         '5.884 $I_{\pm}$\n' +
                         '5.828 $3/2^{-}$, ' +
                         '5.815 $7/2^{-}$, ' +
                         '5.770 $I_{\pm}$', x=4.2, y=5.770+(6.468-5.770)/2 - 0.25, ha='left', va='center'))

na21.add_level(level(6.879, '', '', many=True, upper_energy=7.253, hide_energy_spin_parity=True))
ds.add_freetext(freetext('$\\leftarrow$', x=4.1, y=6.879+(7.253-6.879)/2 - 0.1))
ds.add_freetext(freetext('7.253   $1/2^{+}$, ' +
                         '6.992 $7/2^{-}$, ' +
                         '6.879 $3/2^{-}$', x=4.2, y=6.879+(7.253-6.879)/2 - 0.1, ha='left', va='center'))

na21.add_level(level(7.571, '', '', many=True, upper_energy=7.609, hide_energy_spin_parity=True, lw=0.2))
ds.add_freetext(freetext('$\\leftarrow$', x=4.1, y=7.571+(7.609-7.571)/2 - 0.))
ds.add_freetext(freetext('7.609? $3/2^{+}$, ' +
                         '7.575 $1/2^{-}$, ' +
                         '7.571 $3/2^{-}$', x=4.2, y=7.571+(7.609-7.571)/2 - 0., ha='left', va='center'))

na21.add_level(level(7.930, '', '', many=True, upper_energy=8.960, hide_energy_spin_parity=True, lw=0.6))
ds.add_freetext(freetext('$\\swarrow$', x=4.1, y=7.930+(8.960-7.930)/2 + 0.5))
ds.add_freetext(freetext('8.960 $1/2^{+}$, ' +
                         '8.827   $5/2^{+}$, ' +
                         '8.742 $1/2^{+}$\n' +
                         '8.738 $3/2^{-}$, ' +
                         '8.715   $3/2^{+}$, ' +
                         '8.624 $1/2^{-}$\n' +
                         '8.595 $5/2^{+}$, ' +
                         '8.562? $3/2^{+}$, ' +
                         '8.554 $1/2^{+}$\n' +
                         '8.464 $3/2^{+}$, ' +
                         '8.397   $3/2^{+}$, ' +
                         '8.388 $1/2^{+}$\n' +
                         '8.303 $I_\pm$,    ' +
                         '8.135   $5/2^{+}$, ' +
                         '8.097 $3/2^{-}$\n' +
                         '7.960 $1/2^{-}$, ' +
                         '7.946   $7/2^{-}$, ' +
                         '7.930 $5/2^{-}$', x=4.2, y=7.930+(8.960-7.930)/2 + 1.9, ha='left', va='center'))

na21.add_level(level(8.973, '5/2', '+', text_above='IAS', draw_reference_line=True, lw=1., color='C2'))

mg21 = nuclide(3, "21Mg")
mg21_gs = level(13.095, '5/2', '+', lw=2.0, draw_QEC_level_below=True, text_below='$\mathrm{^{21}Mg}$')
mg21.add_level(mg21_gs)

ds.add_nuclide(na21)
ds.add_nuclide(mg21)
ds.add_nuclide(a17f)
ds.add_nuclide(p20ne)

ds.add_freetext(freetext('$I_\pm=$"$(3/2,5/2,7/2)^{+}$"\n' +
                         '$\\widetilde{I}_\pm=$"$(5/2,7/2)^{-}$"', x=4.35, y=0.3, ha='left', va='center'))

draw_decay_scheme(ds, no_save=True, MeV_to_inch=0.35, hor_padding=0.5)