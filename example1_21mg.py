from decay_scheme_drawer import *

# Uncomment the following print statements to see "the API"
#print("A decay_scheme has the following fields:")
#print(vars(decay_scheme()), "\n")
#print("A nuclide, contained in a decay_scheme, has the following fields:")
#print(vars(nuclide(0, "235U")), "\n")
#print("A level, contained in a nuclide, has the following fields:")
#print(vars(level(0., '7/2', '-')), "\n")
#print("A decay, contained in a decay_scheme, has the following fields:")
#print(vars(decay(nuclide(1, "235U"), level(0., '7/2', '-'), nuclide(0, "231Th"), level(0.205, '(7/2)', '-'))), "\n")
#print("A decay_to_coordinate, contained in a decay_scheme, has the following fields:")
#print(vars(decay_to_coordinate(nuclide(1, "235U"), level(0., '7/2', '-'), 1.2, 0.205)), "\n")
#print("A freetext, contained in a decay_scheme, has the following fields:")
#print(vars(freetext("some text", 2.66, 8.33)))
#print("\n\n")

a17f = nuclide(0, "a+17F")
a17f_gs = level(6.561, '5/2', '+', lw=2.0, text_below='$\mathrm{\\alpha+^{17}F}$', draw_reference_line=True)
a17f.add_level(a17f_gs)

p20ne = nuclide(1, "p+20Ne")
p20ne.add_level(level(2.431, '0', '+', lw=2.0, text_below='$\mathrm{p+^{20}Ne}$', draw_reference_line=True))
ne20_2plus = level(4.065, '2', '+')
p20ne.add_level(ne20_2plus)
ne20_4plus = level(6.679, '4', '+')
p20ne.add_level(ne20_4plus)
p20ne.add_level(level(7.398, '2', '-'))
p20ne.add_level(level(8.053, '3', '-'))
p20ne.add_level(level(9.436, '4', '-'))

na21 = nuclide(2, "21Na")
na21.add_level(level(0., '3/2', '+', lw=2.0, text_below='$\mathrm{^{21}Na}$', energy_spin_parity_below=True))
na21.add_level(level(0.332, '5/2', '+'))
na21.add_level(level(1.716, '7/2', '+'))
na21.add_level(level(5.020, '', '', many=True, upper_energy=5.979, hide_energy_spin_parity=True))
na21_32plus = level(8.397, '3/2', '+', energy_y_adjust=-0.05, spin_parity_y_adjust=-0.05)
na21.add_level(level(8.303, '(3/2,5/2,7/2)', '+', energy_spin_parity_below=True, spin_parity_x_adjust=+0.26))
na21.add_level(na21_32plus)
na21_ias = level(8.973, '5/2', '+', text_above='IAS')
na21.add_level(na21_ias)

mg21 = nuclide(3, "21Mg")
mg21_gs = level(13.095, '5/2', '+', lw=2.0, draw_QEC_level_below=True, text_below='$\mathrm{^{21}Mg}$')
mg21.add_level(mg21_gs)



ds = decay_scheme()
ds.add_nuclide(na21)
ds.add_nuclide(mg21)
ds.add_nuclide(a17f)
ds.add_nuclide(p20ne)
print(ds)

ds.add_decay(decay(na21, na21_ias, p20ne, ne20_2plus))
ds.add_decay(decay(na21, na21_ias, p20ne, ne20_4plus))

ds.add_decay_to_coordinate(decay_to_coordinate(na21, na21_32plus, 2.32, 5.5))

ds.add_level_connection(level_connection(mg21, mg21_gs, na21, na21_ias))

ds.add_freetext(freetext('$5\sim6$', 2.6, 4.95, ha='left', va='top'))
ds.add_freetext(freetext('$(3/2,5/2,7/2)^{+}$', 3.6+0.26, 4.9, ha='right', va='top'))

#draw_decay_scheme(ds)
draw_decay_scheme(ds, no_save=True)
#draw_decay_scheme(ds, no_save=True, axes_on=True)
#draw_decay_scheme(ds, figname='output.jpg')
#draw_decay_scheme(ds, figname='output.pdf')
#draw_decay_scheme(ds, figname='output.svg') # can add some final touches e.g. in Inkscape from here
