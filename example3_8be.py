from decay_scheme import *

p7li = nuclide(0, "p+7Li")
p7li_gs = level(17.25, '3/2', '-', lw=2.0, text_below='$\mathrm{p+^{7}Li}$')
p7li.add_level(p7li_gs)

aa = nuclide(1, "a+a")
aa_gs = level(-0.092, '', '', lw=2.0, text_below='$\mathrm{\\alpha+\\alpha}$')
aa.add_level(aa_gs)

be8 = nuclide(2, "8Be")
be8_gs = level(0.0, '0', '+', lw=2.0, text_below='$\mathrm{^{8}Be}$')
be8.add_level(be8_gs)
be8_broad = level(3.03, '2', '+', broad=True, upper_energy=3.03+0.75, energy_format_string='%2.2f')
be8.add_level(be8_broad)
be8_166 = level(16.6, '2', '+', energy_format_string='%2.1f', energy_spin_parity_below=True, energy_y_adjust=+0.15, spin_parity_y_adjust=+0.15)
be8.add_level(be8_166)
be8_169 = level(16.9, '2', '+', energy_format_string='%2.1f')
be8.add_level(be8_169)
be8_176 = level(17.6, '1', '+', energy_format_string='%2.1f')
be8.add_level(be8_176)
be8.add_level(level(18.15, '1', '+', energy_format_string='%2.2f'))

b8 = nuclide(3, "8B")
b8_gs = level(17.98, '2', '+', draw_QEC_level_below=True, lw=2.0, text_below='$\mathrm{^{8}B}$')
b8.add_level(b8_gs)

ds = decay_scheme()
ds.add_nuclide(p7li)
ds.add_nuclide(aa)
ds.add_nuclide(be8)
ds.add_nuclide(b8)

ds.add_decay_to_coordinate(decay_to_coordinate(p7li, p7li_gs, 1.4, 3.))
ds.add_decay_to_coordinate(decay_to_coordinate(p7li, p7li_gs, 2.2, 18. - 9.))

ds.add_decay(decay(be8, be8_gs, aa, aa_gs))
ds.add_decay_to_coordinate(decay_to_coordinate(be8, be8_broad, 2.3, 1.))
ds.add_decay_to_coordinate(decay_to_coordinate(be8, be8_166, 2.3, 4.1))
ds.add_decay_to_coordinate(decay_to_coordinate(be8, be8_169, 2.3, 5.1))
ds.add_decay_to_coordinate(decay_to_coordinate(be8, be8_176, 2.3, 6.1))

ds.add_decay(decay(b8, b8_gs, be8, be8_broad))
ds.add_decay(decay(b8, b8_gs, be8, be8_166))
ds.add_decay(decay(b8, b8_gs, be8, be8_169))

ds.add_freetext(freetext('Direct $\mathrm{\\alpha+\\alpha}$', 1.3, 14.6 - 9., rotation=-75.))
ds.add_freetext(freetext('Resonant', 1.6, 17.9 - 9., rotation=10.))
ds.add_freetext(freetext('$\mathrm{\\alpha}$', 2.35, 2.1))
ds.add_freetext(freetext('$\mathrm{\\beta^{+},\,EC}$', 4.0, 15. - 9.))

draw_decay_scheme(ds, exclude_y=[4., 13.], MeV_to_inch=0.3, no_save=True)