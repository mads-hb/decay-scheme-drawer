from decay_scheme import *

ds = decay_scheme()

he8 = nuclide(0, "8He")
he8_gs = level(10.664, '0', '+', lw=2.0, text_below='$\mathrm{^{8}He}$', energy_format_string="%2.3f")
he8.add_level(he8_gs)
ds.add_nuclide(he8)

li8 = nuclide(1, "8Li")
li8_gs = level(0.0, '2', '+', lw=2.0, text_below='$\mathrm{^{8}Li}$')
li8_1 = level(0.98, '1', '+', energy_format_string="%2.2f")
li8_2 = level(3.21, '1', '+', broad=True, upper_energy=3.21+0.5, energy_format_string="%2.2f")
li8_3 = level(5.40, '1', '+', broad=True, upper_energy=5.40+0.325, energy_format_string="%2.2f")
li8_4 = level(9.67, '1', '+', broad=True, upper_energy=9.67+0.5, energy_format_string="%2.2f")
ds.add_nuclide(li8)
li8_levels = [li8_gs, li8_1, li8_2, li8_3, li8_4]
for l in li8_levels:
    li8.add_level(l)
for l in li8_levels[1:]:
    ds.add_decay(decay(he8, he8_gs, li8, l))

li7 = nuclide(2, "7Li")
li7_gs = level(2.03, '3/2', '-', lw=2.0, text_below='$\mathrm{n+ ^{7}Li}$', energy_format_string="%2.2f", energy_spin_parity_below=True)
li7_1 = level(2.51, '1/2', '-', energy_format_string="%2.2f")
li7.add_level(li7_gs)
li7.add_level(li7_1)
ds.add_nuclide(li7)

he5 = nuclide(3, "5He")
he5_gs = level(5.2, '3/2', '-', broad=True, upper_energy=5.2+0.4, lw=2.0, text_above='$\mathrm{t+ ^{5}He}$', energy_format_string="%2.1f")
he5.add_level(he5_gs)
he5.add_level(level(5.2-0.735, '', '', text_below='$\mathrm{t+ \\alpha + n}$', energy_spin_parity_below=True, energy_format_string="%2.1f"))
ds.add_nuclide(he5)
ds.add_decay(decay(li8, li8_4, he5, he5_gs))

li6 = nuclide(2.3, "6Li", skip_hor_padding=True)
li6_2n = level(9.284, '1', '+', lw=0.7, ls=(0.5, (3.1, 3)), text_below='$\mathrm{2n+ ^{6}Li}$', energy_format_string="%2.2f", energy_spin_parity_below=True)
li6_d = level(10.664-0.882, '0', '+', lw=0.7, ls=(0.5, (3.1, 3)), text_above='$\mathrm{d+ ^{6}He}$', energy_format_string="%2.2f")
li6.add_level(li6_2n)
li6.add_level(li6_d)

ds.add_nuclide(li6)

#ds.add_freetext(freetext('$\Lsh$', 4.55, 3.7, rotation=180.))
#ds.add_freetext(freetext('$\mathrm{α+n}; Q=735\,\mathrm{keV}$', 4.6, 3.45, ha='left'))

draw_decay_scheme(ds, MeV_to_inch=0.15, no_save=True)