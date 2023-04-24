from decay_scheme import *
plt.rc("pdf", fonttype=42)

p20ne = nuclide(0, "p+20Ne")
p20ne.add_level(level(0, '0', '+', lw=2.0, text_below='$\mathrm{^{20}Ne}$'))
ne20_2plus = level(1.634, '2', '+')
p20ne.add_level(ne20_2plus)
ne20_4plus = level(4.248, '4', '+', energy_spin_parity_below=True, energy_y_adjust=+.07, spin_parity_y_adjust=+.07)
p20ne.add_level(ne20_4plus)
p20ne.add_level(level(4.967, '2', '-', energy_spin_parity_below=True, energy_y_adjust=+.07, spin_parity_y_adjust=+.07))
p20ne.add_level(level(5.621, '3', '-', energy_spin_parity_below=True, energy_y_adjust=+.07, spin_parity_y_adjust=+.07))
p20ne.add_level(level(5.788, '1', '-'))

ds = decay_scheme()
ds.add_nuclide(p20ne)

offset = 0.08
ds.add_freearrow(freearrow(0.4, 1.634, 0.4, 0.    + 1.5*offset))
ds.add_freearrow(freearrow(0.5, 4.248, 0.5, 1.634 + offset))
ds.add_freearrow(freearrow(0.6, 4.967, 0.6, 1.634 + offset))
ds.add_freearrow(freearrow(0.7, 5.621, 0.7, 1.634 + offset))

ds.add_freearrow(freearrow(0., 5.621, -0.15, 5.))
ds.add_freetext(freetext('$\\alpha$', -0.09, 6., ha='center', va='top'))

ds.add_freearrow(freearrow(1.17, 5.621+0.621, 1.01, 5.621 + offset))
ds.add_freetext(freetext('$p$', 1.09, 6.+0.621, ha='center', va='top'))

draw_decay_scheme(ds, no_save=True)