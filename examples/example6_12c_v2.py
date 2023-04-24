from decay_scheme import *

b12 = nuclide(0, "12B")
b12_gs = level(13.37, '1', '+', lw=2.0, text_below='$\mathrm{^{12}B}$', energy_format_string="%2.2f")
b12.add_level(b12_gs)

c12 = nuclide(1, "12C")
c12_0 = level(0.0, '', '', lw=2.0, text_below='$\mathrm{^{12}C}$')
c12_1 = level(4.44, '2', '+', energy_format_string="%1.2f", hide_energy_spin_parity=True)
c12_2 = level(7.65, '0', '+', energy_format_string="%1.2f", hide_energy_spin_parity=True)
c12_many = level(7.65 + (12.7 - 7.65)/3.5, '', '', many=True, upper_energy=12.7 - (12.7 - 7.65)/3.5, hide_energy_spin_parity=True)
c12_3 = level(12.7, '1', '+', energy_format_string="%2.1f", hide_energy_spin_parity=True)
c12_4 = level(15.1, '1', '+', energy_format_string="%2.1f", text_above='', hide_energy_spin_parity=True)
c12.add_level(c12_0)
c12.add_level(c12_1)
c12.add_level(c12_2)
c12.add_level(c12_many)
c12.add_level(c12_3)
c12.add_level(c12_4)

n12 = nuclide(2, "12N")
n12_gs = level(17.34, '1', '+', lw=2.0, text_below='$\mathrm{^{12}N}$', draw_QEC_level_below=True, energy_format_string="%2.2f")
n12.add_level(n12_gs)

ds = decay_scheme()
ds.add_nuclide(b12)
ds.add_nuclide(c12)
ds.add_nuclide(n12)

ds.add_decay(decay(b12, b12_gs, c12, c12_0))
ds.add_decay(decay(b12, b12_gs, c12, c12_1))
ds.add_decay(decay(b12, b12_gs, c12, c12_2))
ds.add_decay(decay(b12, b12_gs, c12, c12_many))
ds.add_decay(decay(b12, b12_gs, c12, c12_3))

ds.add_decay(decay(n12, n12_gs, c12, c12_0, color='tab:red'))
ds.add_decay(decay(n12, n12_gs, c12, c12_1))
ds.add_decay(decay(n12, n12_gs, c12, c12_2))
ds.add_decay(decay(n12, n12_gs, c12, c12_many))
ds.add_decay(decay(n12, n12_gs, c12, c12_3))
ds.add_decay(decay(n12, n12_gs, c12, c12_4))

ds.add_freetext(freetext('$\mathrm{\\beta^{-}}$', 0.9, 12.))
ds.add_freetext(freetext('$\mathrm{\\beta^{+},\,EC}$', 2.8, 15.))
ds.add_freetext(freetext('$\mathrm{94.6\%}$', 2.6, 4., color='tab:red'))

draw_decay_scheme(ds, MeV_to_inch=0.15, no_save=True)