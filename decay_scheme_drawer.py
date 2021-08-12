import os
from decay_scheme_classes import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.font_manager as font_manager
font_dir = os.getcwd() + '/fonts'
font_files = font_manager.findSystemFonts(font_dir)
for f in font_files:
    font_manager.FontManager.addfont(font_manager.fontManager, path=f)
plt.rcParams.update({"font.family": "serif", "font.serif": "Linux Libertine O", "font.cursive": "Linux Libertine O", "font.sans-serif": "Linux Libertine O", "mathtext.fontset": "custom"})

hor_padding = 0.3 # in units of length of nuclide's level lines
ver_padding = 0.3 # in units of distance between 1 MeV-separated levels
nuclide_to_inch = 1. # figwidth
MeV_to_inch = 0.25 # figheight

bracket_offset = 0.04
QEC_text_offset = 0.2
below_text_offset = 0.2
above_text_offset = 0.

mec2 = 0.51099895000

fig = plt.figure(dpi=300, constrained_layout=True)
ax = plt.gca()
rend = fig.canvas.get_renderer()

def get_text_field_dims(text_field):
    bb = text_field.get_window_extent(renderer=rend)
    transf = ax.transData.inverted()
    bb_datacoords = bb.transformed(transf)
    text_field_width = bb_datacoords.x1 - bb_datacoords.x0
    text_field_height = bb_datacoords.y1 - bb_datacoords.y0 
    return text_field_width, text_field_height

def adjust_fig_dims(left=0., right=0., bottom=0., top=0.):
    leftt, rightt = plt.xlim()
    bottomm, topp = plt.ylim()
    widthh = fig.get_figwidth()
    heightt = fig.get_figheight()
    if left:
        plt.xlim(left=leftt - left)
        fig.set_figwidth(widthh + nuclide_to_inch*left)
    if right:
        plt.xlim(right=rightt + right)
        fig.set_figwidth(widthh + nuclide_to_inch*right)
    if bottom:
        plt.ylim(bottom=bottomm - bottom)
        fig.set_figheight(heightt + MeV_to_inch*bottom)
    if top:
        plt.ylim(top=topp + top)
        fig.set_figheight(heightt + MeV_to_inch*top)

def adjust_top(text_field, top=0.):
    w, h = get_text_field_dims(text_field)
    adjust_fig_dims(top=h+top)
    
def adjust_bottom(text_field, bottom=0.):
    w, h = get_text_field_dims(text_field)
    adjust_fig_dims(bottom=h+bottom)

def adjust_left(text_field, left=0.):
    w, h = get_text_field_dims(text_field)
    adjust_fig_dims(left=w+left)
    
def adjust_right(text_field, right=0.):
    w, h = get_text_field_dims(text_field)
    adjust_fig_dims(right=w+right)

def draw_decay_scheme(decay_scheme, figname='decay_scheme.pdf', no_save=False, axes_on=False):
    found_index_zero = False
    for nuclide in decay_scheme:
        if nuclide.index == 0:
            found_index_zero = True
    if not found_index_zero:
        print("WARNING: Some drawing features relies on the left-most nuclide having index zero ('0').")
    min_e = 1000.
    max_e = 0.
    for nuclide in decay_scheme:
        for level in nuclide:
            if min_e > level.energy: min_e = level.energy
            if max_e < level.energy: max_e = level.energy
            if max_e < level.upper_energy: max_e = level.upper_energy
    columns = decay_scheme.num_nuclides
    total_width = columns + (columns + 1)*hor_padding
    total_height = max_e - min_e + 2*ver_padding
    fig.set_figheight(MeV_to_inch*total_height)
    fig.set_figwidth(nuclide_to_inch*total_width)
    plt.xlim(-hor_padding, total_width - hor_padding)
    plt.ylim(-ver_padding, total_height - ver_padding)

    padding = 0.
    QEC_text_width = 0.
    for nuclide in decay_scheme:
        QEC = False
        x1 = nuclide.index + padding
        x2 = nuclide.index + 1 + padding
        for level in nuclide:
            y1 = level.energy
            plt.hlines(y1, x1, x2, ls=level.ls, lw=level.lw, color=level.color)
            if level.broad:
                y2 = level.upper_energy
                plt.hlines(y2, x1, x2, ls=level.ls, lw=level.lw, color=level.color)
                plt.fill([x1, x1, x2, x2], [y1, y2, y2, y1], color='silver', lw=0.)
            if not level.hide_energy_spin_parity:
                e_string = "%2.3f" % level.energy if level.energy > 0. else "0.0"
                if not level.broad:
                    if not level.energy_spin_parity_below:
                        E_text = plt.text(x1, y1 + above_text_offset, e_string, ha='left', va='bottom')
                        plt.text(x2, y1 + above_text_offset, "$%s^{%s}$" % (level.spin, level.parity), ha='right', va='bottom')
                        if level.energy == max_e:
                            adjust_top(E_text, above_text_offset)
                    else:
                        E_text = plt.text(x1, y1 - below_text_offset, e_string, ha='left', va='top')
                        plt.text(x2, y1 - below_text_offset, "$%s^{%s}$" % (level.spin, level.parity), ha='right', va='top')
                        if level.energy == min_e:
                            adjust_bottom(E_text, below_text_offset)
                else:
                    upper_e_string = "%2.3f" % level.upper_energy
                    E_text = plt.text(x1, y2 + above_text_offset, upper_e_string, ha='left', va='bottom')
                    plt.text(x2, y2 + above_text_offset, "$%s^{%s}$" % (level.upper_spin, level.upper_parity), ha='right', va='bottom')
                    if level.upper_energy == max_e:
                        adjust_top(E_text, above_text_offset)
                    E_text = plt.text(x1, y1 - below_text_offset, e_string, ha='left', va='top')
                    plt.text(x2, y1 - below_text_offset, "$%s^{%s}$" % (level.spin, level.parity), ha='right', va='top')
                    if level.energy == min_e:
                        adjust_bottom(E_text, below_text_offset)
            if level.draw_QEC_level_below:
                plt.hlines(y1 - 2*mec2, x1, x2, ls=(1, (3, 1.3)), lw=1.0, color=level.color)
                plt.text(x2 + bracket_offset, y1 - mec2, "}", fontsize=16, va='center', ha='left')
                QEC_text = plt.text(x2 + QEC_text_offset, y1 - mec2, "$2m_{\mathrm{e}}c^2$", va='center', ha='left')
                adjust_right(QEC_text, bracket_offset+QEC_text_offset)
                QEC_text_width, h = get_text_field_dims(QEC_text)
                QEC = True
            if level.text_below:
                below_text = plt.text(x1 + 0.5, y1 - below_text_offset, level.text_below, va='top', ha='center')
                if level.energy == min_e:
                    adjust_bottom(below_text, below_text_offset)
            if level.text_above:
                if not level.broad:
                    above_text = plt.text(x1 + 0.5, y1 + above_text_offset, level.text_above, va='bottom', ha='center')
                    if level.energy == max_e:
                        adjust_top(above_text, above_text_offset)
                else:
                    above_text = plt.text(x1 + 0.5, y2 + above_text_offset, level.text_above, va='bottom', ha='center')
                    if level.upper_energy == max_e:
                        adjust_top(above_text, above_text_offset)
            if False:
                daughter_nuclices = level.decays_to[::2]
                daughter_levels = level.decays_to[1::2]
                for i in range(len(daughter_levels)):
                    dn = daughter_nuclices[i]
                    dl = daughter_levels[i]
                    x3 = dn.index*(1 + hor_padding) + 1
                    y3 = dl.energy
                    plt.annotate("", (x3, y3), (x1, y1), arrowprops=dict(arrowstyle="-|>", lw=1, color='k'))
        padding += hor_padding + QEC*(QEC_text_width + bracket_offset + QEC_text_offset)
    decays = decay_scheme.decays
    for decay in decays:
        # this part should be simple, but matplotlib's standard arrows are UGLY because their heads are drawn relative to data coordinates; "fancyarrowpatches" do not have this problem, but the variety of head shapes is limitied... so we draw the arrows ourselves
        # wip
        x1 = decay.daughter_nuclide.index*(1 + hor_padding) + 1
        y1 = decay.daughter_level.energy
        x2 = decay.parent_nuclide.index*(1 + hor_padding)
        y2 = decay.parent_level.energy
        r1 = np.array([x1, y1])
        r2 = np.array([x2, y2])
        #r = r2 - r1
        #n = r/np.linalg.norm(r)
        #v = np.arccos(np.dot(n, np.array([1, 0])))
        #dv = np.deg2rad(15)
        #plt.plot([x1, x2], [y1, y2], color='k')
        #r1, r2, r, n = ax.transAxes.inverted().transform(ax.transData.transform([r1, r2, r, n]))
        #ha = hb = np.array([1, 0])
        #Ra = np.array([[np.cos(v + dv), -np.sin(v + dv)], [np.sin(v + dv), np.cos(v + dv)]])
        #Rb = np.array([[np.cos(v - dv), -np.sin(v - dv)], [np.sin(v - dv), np.cos(v - dv)]])
        #(xa, ya) = Ra.dot(ha)
        #(xb, yb) = Rb.dot(hb)
        #plt.plot(u[0], u[1], 'o', transform=fig.dpi_scale_trans)
    freetexts = decay_scheme.freetexts
    for ftext in freetexts:
        plt.text(ftext.x, ftext.y, ftext.text, va=ftext.va, ha=ftext.ha)
    if axes_on:
        hor_sizes = [hor_padding, bracket_offset, QEC_text_offset]
        hor_sizes_strs = ["hor_padding", "bracket_offset", "QEC_text_offset"]
        ver_sizes = [ver_padding, below_text_offset, above_text_offset]
        ver_sizes_strs = ["ver_padding", "below_text_offset", "above_text_offset"]
        leftt, rightt = plt.xlim()
        bottomm, topp = plt.ylim()
        leftt += 0.1
        rightt -= 0.1
        bottomm += 0.4
        topp -= 0.4
        for i in range(len(hor_sizes)):
            plt.annotate("%s = %1.2f" % (hor_sizes_strs[i], hor_sizes[i]), (leftt, topp), (leftt + hor_sizes[i], topp), arrowprops=dict(arrowstyle="-", lw=1, color='k'), ha='left', va='center')
            topp -= 0.6
        for i in range(len(ver_sizes)):
            plt.annotate("%s = %1.2f  " % (ver_sizes_strs[i], ver_sizes[i]), (rightt, bottomm), (rightt, bottomm + ver_sizes[i]), arrowprops=dict(arrowstyle="-", lw=1, color='k', relpos=(1,1)), ha='right', va='center')
            bottomm += 0.6 + ver_sizes[i]
        plt.xlabel('nuclide.index*(1 + hor_padding)')
        plt.ylabel('level.energy')
    else:
        plt.axis('off')
    if no_save:
        plt.show()
    else:
        print("Decay scheme saved in local directory as '%s'" % figname)
        plt.savefig(figname)
    return fig, ax
