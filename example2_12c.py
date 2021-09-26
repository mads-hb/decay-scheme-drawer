from decay_scheme import *

b12 = nuclide(0, "12B")
b12_gs = level(13.37, '1', '+', lw=2.0, text_below='$\mathrm{^{12}B}$', energy_format_string="%2.2f")
b12.add_level(b12_gs)

c12 = nuclide(1, "12C")
c12_0 = level(0.0, '0', '+', lw=2.0, text_below='$\mathrm{^{12}C}$')
c12_1 = level(4.44, '2', '+', energy_format_string="%1.2f")
c12_2 = level(7.65, '0', '+', energy_format_string="%1.2f", energy_spin_parity_below=True)
c12_3 = level(10., '', '', ls='--', hide_energy_spin_parity=True)
c12_4 = level(10.3, '', '', energy_format_string="%2.1f")
c12_5 = level(12.7, '1', '+', energy_format_string="%2.1f")
c12_6 = level(15.1, '1', '+', energy_format_string="%2.1f", text_above='IAS')
c12.add_level(c12_0)
c12.add_level(c12_1)
c12.add_level(c12_2)
c12.add_level(c12_3)
c12.add_level(c12_4)
c12.add_level(c12_5)
c12.add_level(c12_6)

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
ds.add_decay(decay(b12, b12_gs, c12, c12_4))
ds.add_decay(decay(b12, b12_gs, c12, c12_5))

ds.add_decay(decay(n12, n12_gs, c12, c12_0))
ds.add_decay(decay(n12, n12_gs, c12, c12_1))
ds.add_decay(decay(n12, n12_gs, c12, c12_2))
ds.add_decay(decay(n12, n12_gs, c12, c12_4))
ds.add_decay(decay(n12, n12_gs, c12, c12_5))
ds.add_decay(decay(n12, n12_gs, c12, c12_6))

ds.add_freetext(freetext('$\mathrm{\\beta^{-}}$', 0.9, 12.))
ds.add_freetext(freetext('$\sim10$', 1.3, 9.9, va='top', ha='left'))
ds.add_freetext(freetext('$(0^{+})$', 2.3, 9.9, va='top', ha='right'))
ds.add_freetext(freetext('$\mathit{Hoyle}$', 1.3 + 1/2, 9.9, va='top', ha='center'))
ds.add_freetext(freetext('$\mathrm{\\beta^{+},\,EC}$', 2.8, 15.))

draw_decay_scheme(ds, MeV_to_inch=0.15, no_save=True)