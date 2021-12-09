from decay_scheme import *

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

ds.add_decay(decay(mg21, mg21_gs, na21, na21_ias))

ds.add_decay_to_coordinate(decay_to_coordinate(na21, na21_ias, 2.4, 8.))
ds.add_decay_to_coordinate(decay_to_coordinate(na21, na21_ias, 2.4, 7.))
ds.add_decay_to_coordinate(decay_to_coordinate(na21, na21_ias, 2.4, 6.))
ds.add_decay_to_coordinate(decay_to_coordinate(na21, na21_ias, 2.4, 5.))

ds.add_freetext(freetext('$5\sim6$', 2.6, 4.95, ha='left', va='top'))
ds.add_freetext(freetext('$(3/2,5/2,7/2)^{+}$', 3.6+0.26, 4.9, ha='right', va='top'))
ds.add_freetext(freetext('$\mathrm{β^{+}}$', 3.75, 12.))
ds.add_freetext(freetext('$\mathrm{p}$', 2.45, 8.8))

draw_decay_scheme(ds, figname='21mg_v3.png') 
