from decay_scheme import *
import matplotlib.pyplot as plt

from decay_scheme.decay_scheme_classes import Decay, FreeArrow, FreeText

plt.style.use("default")

tex_fonts = {
    # Use LaTeX to write all text
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{libertine} \usepackage{libertinust1math} \usepackage{amsmath}",
    "font.family": "libertine",
    # Use 10pt font in plots, to match 10pt font in document
    "axes.labelsize": 11,
    "font.size": 11,
    "figure.titlesize": 11,
    # Make the legend/label fonts a little smaller
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "xtick.minor.visible": True,
    "ytick.minor.visible": True
}

plt.rcParams.update(tex_fonts)

ds = DecaySchema()

he8_gs = Level(energy=10.664, spin='0', parity=Parity.UP, lw=2.0, text_below='$\mathrm{^{8}He}$', energy_format_string="2.3f", text_below_y_adjust=-0.1)
he8 = Nuclide(index=0, name="8He")
he8.add_level(he8_gs)
ds.add_nuclide(he8)

li8 = Nuclide(index=1, name="8Li")
li8_gs = Level(energy=0.0, spin='2', parity=Parity.UP, lw=2.0, text_below='$\mathrm{^{8}Li}$', text_below_y_adjust=-0.1)
li8_1 = Level(energy=0.98, spin='1', parity=Parity.UP, energy_format_string="2.2f")
li8_2 = Level(energy=3.21, spin='1', parity=Parity.UP, broad=True, width=0.5, energy_format_string="2.2f")
li8_3 = Level(energy=5.40, spin='1', parity=Parity.UP, broad=True, width=0.2, energy_format_string="2.2f")
li8_4 = Level(energy=9.67, spin='1', parity=Parity.UP, broad=True, width=0.4, energy_format_string="2.2f")
ds.add_nuclide(li8)
li8_levels = [li8_gs, li8_1, li8_2, li8_3, li8_4]
for l in li8_levels:
    li8.add_level(l)
for l in li8_levels[1:]:
    ds.add_decay(Decay(parent_nuclide=he8, parent_level=he8_gs, daughter_nuclide=li8, daughter_level=l))

li7 = Nuclide(index=2, name="7Li")
li7_gs = Level(energy=2.03, spin='3/2', parity=Parity.DOWN, lw=2.0, text_below='$\mathrm{n+ ^{7}Li}$', energy_format_string="2.2f", energy_spin_parity_below=False,  text_below_y_adjust=-0.1)
li7_1 = Level(energy=2.51, spin='1/2', parity=Parity.DOWN, energy_format_string="2.2f")
li7.add_level(li7_gs)
li7.add_level(li7_1)
ds.add_nuclide(li7)

ds.add_decay(Decay(parent_nuclide=li8, parent_level=li8_3, daughter_nuclide=li7, daughter_level=li7_1))
ds.add_decay(Decay(parent_nuclide=li8, parent_level=li8_2, daughter_nuclide=li7, daughter_level=li7_1))

#
#
ds.add_freetext(FreeText(text='$84\%$', x=0.95, y=7.8, rotation=-74))
ds.add_freetext(FreeText(text='$\sim 1\%$', x=0.9, y=10.5, rotation=-32))
fig, ax = plt.subplots(dpi=128)

man = DecaySchemeDrawer()
man.draw_decay_scheme(ds, ax=ax)
ax.set_xlim(0,3)
ax.set_ylim(0,13)
ax.axis("off")
fig.savefig("example.pdf")
plt.show()