import os

from decay_scheme_classes import *
import numpy as np
import matplotlib as mpl
from matplotlib.path import Path
from matplotlib.markers import MarkerStyle
from matplotlib import transforms
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
font_dir = os.getcwd() + '/fonts'
font_files = font_manager.findSystemFonts(font_dir)
for f in font_files:
    font_manager.FontManager.addfont(font_manager.fontManager, path=f)
plt.rcParams.update({"font.family": "serif", "font.serif": "Linux Libertine O", "font.cursive": "Linux Libertine O", "font.sans-serif": "Linux Libertine O", "mathtext.fontset": "custom"})

hor_padding = 0.3 # in units of length of nuclide's level lines
ver_padding = 0.3 # in units of distance between 1 MeV-separated levels
#nuclide_to_inch = 1. # figwidth
#MeV_to_inch = 0.25 # figheight

bracket_offset = 0.04
QEC_text_offset = 0.2
below_text_offset = 0.2
above_text_offset = 0.

mec2 = 0.51099895000

fig = plt.figure(dpi=300, constrained_layout=True)
ax = plt.gca()
rend = fig.canvas.get_renderer()

arrowhead_vertices = np.loadtxt('arrowhead_vertices.dat')
arrowhead_vertices[:, 0] = arrowhead_vertices[:, 0] - np.min(arrowhead_vertices[:, 0])
arrowhead_vertices[:, 1] = arrowhead_vertices[:, 1] - np.mean(arrowhead_vertices[:, 1]) - 0.05
arrowhead_codes = np.loadtxt('arrowhead_codes.dat')
arrowhead = Path(arrowhead_vertices, arrowhead_codes)

def get_text_field_dims(text_field):
    bb = text_field.get_window_extent(renderer=rend)
    transf = ax.transData.inverted()
    bb_datacoords = bb.transformed(transf)
    text_field_width = bb_datacoords.x1 - bb_datacoords.x0
    text_field_height = bb_datacoords.y1 - bb_datacoords.y0 
    return text_field_width, text_field_height

def adjust_fig_dims(nuclide_to_inch, MeV_to_inch, left=0., right=0., bottom=0., top=0.):
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

def adjust_top(text_field, nuclide_to_inch, MeV_to_inch, top=0.):
    w, h = get_text_field_dims(text_field)
    adjust_fig_dims(nuclide_to_inch, MeV_to_inch, top=h+top)
    
def adjust_bottom(text_field, nuclide_to_inch, MeV_to_inch, bottom=0.):
    w, h = get_text_field_dims(text_field)
    adjust_fig_dims(nuclide_to_inch, MeV_to_inch, bottom=h+bottom)

def adjust_left(text_field, nuclide_to_inch, MeV_to_inch, left=0.):
    w, h = get_text_field_dims(text_field)
    adjust_fig_dims(nuclide_to_inch, MeV_to_inch, left=w+left)
    
def adjust_right(text_field, nuclide_to_inch, MeV_to_inch, right=0.):
    w, h = get_text_field_dims(text_field)
    adjust_fig_dims(nuclide_to_inch, MeV_to_inch, right=w+right)

class UnsizedMarker(MarkerStyle):
    def _set_custom_marker(self, path):
        self._transform = transforms.IdentityTransform()
        self._path = path

def draw_arrow(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], 'k-', lw=0.5)

    r1 = np.array([x1, y1])
    r2 = np.array([x2, y2])
    r = r2 - r1
    n = r / np.linalg.norm(r)
    leftt, rightt = plt.xlim()
    bottomm, topp = plt.ylim()
    a = (topp - bottomm)/(rightt - leftt)
    b = fig.get_figheight() / fig.get_figwidth()
    n[0] *= a/b
    angle = np.arctan2(n[1], n[0]) + np.deg2rad(180.)

    tr = transforms.Affine2D().rotate(angle)
    m = UnsizedMarker(arrowhead.transformed(tr))
    plt.scatter(x2, y2, marker=m, s=0.3, color='k')

def calculate_arrow_offsets(x1, y1, x2, y2, nuclide_to_inch, MeV_to_inch):
    # index offset
    if x1 < x2:
        x1 += 1
    else:
        x2 += 1

    # arrowhead offset
    dx = 0.02 * nuclide_to_inch
    dy = 0.12 * MeV_to_inch * abs(y1 - y2)
    if x1 < x2:
        x2 -= dx
    else:
        x2 += dx
    if y1 < y2:
        y2 -= dy
    else:
        y2 += dy

    return x1, y1, x2, y2


def draw_decay_scheme(decay_scheme, figname='decay_scheme.pdf', no_save=False, axes_on=False, nuclide_to_inch=1., MeV_to_inch=0.25, exclude_y=None, energy_format_string="%2.3f"):
    global_energy_format_string = energy_format_string
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
    y_lower_excl = float('-inf')
    y_upper_excl = float('inf')
    y_corr = 0.
    if exclude_y:
        y_lower_excl = np.min(exclude_y)
        y_upper_excl = np.max(exclude_y)
        y_corr = y_upper_excl - y_lower_excl
    columns = decay_scheme.num_nuclides
    total_width = columns + (columns + 1)*hor_padding
    total_height = max_e - min_e + 2*ver_padding - y_corr
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
            if level.energy_format_string:
                energy_format_string = level.energy_format_string
            else:
                energy_format_string = global_energy_format_string
            y1 = level.energy - y_corr if level.energy > y_upper_excl else level.energy
            plt.hlines(y1, x1, x2, ls=level.ls, lw=level.lw, color=level.color)
            if level.broad:
                y2 = level.upper_energy - y_corr if level.energy > y_upper_excl else level.upper_energy
                y0 = y1 - (y2 - y1)
                plt.fill([x1, x1, x2, x2], [y0, y2, y2, y0], color='silver', lw=0.)
            if level.many:
                y2 = level.upper_energy - y_corr if level.energy > y_upper_excl else level.upper_energy
                plt.hlines(y2, x1, x2, ls=level.ls, lw=level.lw, color=level.color)
                plt.fill([x1, x1, x2, x2], [y1, y2, y2, y1], color='silver', lw=0.)
            if not level.hide_energy_spin_parity:
                e_string = energy_format_string % level.energy if level.energy != 0. else "0.0"
                if not level.broad and not level.many:
                    if not level.energy_spin_parity_below:
                        E_text = plt.text(x1 + level.energy_x_adjust, y1 + above_text_offset + level.energy_y_adjust, e_string, ha='left', va='bottom')
                        plt.text(x2 + level.spin_parity_x_adjust, y1 + above_text_offset + level.spin_parity_y_adjust, "$%s^{%s}$" % (level.spin, level.parity), ha='right', va='bottom')
                        if level.energy == max_e:
                            adjust_top(E_text, nuclide_to_inch, MeV_to_inch, above_text_offset)
                    else:
                        E_text = plt.text(x1 + level.energy_x_adjust, y1 - below_text_offset + level.energy_y_adjust, e_string, ha='left', va='top')
                        plt.text(x2 + level.spin_parity_x_adjust, y1 - below_text_offset + level.spin_parity_y_adjust, "$%s^{%s}$" % (level.spin, level.parity), ha='right', va='top')
                        if level.energy == min_e:
                            adjust_bottom(E_text, nuclide_to_inch, MeV_to_inch, below_text_offset)
                elif level.broad:
                    upper_e_string = energy_format_string % level.energy
                    E_text = plt.text(x1 + level.upper_energy_x_adjust, y2 + above_text_offset + level.upper_energy_y_adjust, upper_e_string, ha='left', va='bottom')
                    plt.text(x2 + level.spin_parity_x_adjust, y2 + above_text_offset + level.spin_parity_y_adjust, "$%s^{%s}$" % (level.spin, level.parity), ha='right', va='bottom')
                    if level.upper_energy == max_e:
                        adjust_top(E_text, nuclide_to_inch, MeV_to_inch, above_text_offset)
                elif level.many:
                    upper_e_string = energy_format_string % level.upper_energy
                    E_text = plt.text(x1 + level.upper_energy_x_adjust, y2 + above_text_offset + level.upper_energy_y_adjust, upper_e_string, ha='left', va='bottom')
                    plt.text(x2 + level.upper_spin_parity_x_adjust, y2 + above_text_offset + level.upper_spin_parity_y_adjust, "$%s^{%s}$" % (level.upper_spin, level.upper_parity), ha='right', va='bottom')
                    if level.upper_energy == max_e:
                        adjust_top(E_text, nuclide_to_inch, MeV_to_inch, above_text_offset)
                    E_text = plt.text(x1 + level.energy_x_adjust, y1 - below_text_offset + level.energy_y_adjust, e_string, ha='left', va='top')
                    plt.text(x2 + level.spin_parity_x_adjust, y1 - below_text_offset + level.spin_parity_y_adjust, "$%s^{%s}$" % (level.spin, level.parity), ha='right', va='top')
                    if level.energy == min_e:
                        adjust_bottom(E_text, nuclide_to_inch, MeV_to_inch, below_text_offset)
            if level.draw_QEC_level_below:
                plt.hlines(y1 - 2*mec2, x1, x2, ls=(1, (3, 1.3)), lw=1.0, color=level.color)
                plt.text(x2 + bracket_offset + level.QEC_x_adjust, y1 - mec2 + level.QEC_y_adjust, "}", fontsize=16, va='center', ha='left')
                QEC_text = plt.text(x2 + QEC_text_offset + level.QEC_x_adjust, y1 - mec2 + level.QEC_y_adjust, "$2m_{\mathrm{e}}c^2$", va='center', ha='left')
                adjust_right(QEC_text, nuclide_to_inch, MeV_to_inch, bracket_offset+QEC_text_offset)
                QEC_text_width, h = get_text_field_dims(QEC_text)
                QEC = True
            if level.draw_reference_line:
                plt.hlines(y1, -hor_padding, total_width - hor_padding, ls=(1, (3, 1.3)), lw=0.5, color=level.color)
            if level.text_below:
                below_text = plt.text(x1 + 0.5 + level.text_below_x_adjust, y1 - below_text_offset + level.text_below_y_adjust, level.text_below, va='top', ha='center')
                if level.energy == min_e:
                    adjust_bottom(below_text, nuclide_to_inch, MeV_to_inch, below_text_offset)
            if level.text_above:
                if not level.broad:
                    above_text = plt.text(x1 + 0.5 + level.text_above_x_adjust, y1 + above_text_offset + level.text_above_y_adjust, level.text_above, va='bottom', ha='center')
                    if level.energy == max_e:
                        adjust_top(above_text, nuclide_to_inch, MeV_to_inch, above_text_offset)
                else:
                    above_text = plt.text(x1 + 0.5, y2 + above_text_offset + level.text_above_x_adjust, level.text_above + level.text_above_y_adjust, va='bottom', ha='center')
                    if level.upper_energy == max_e:
                        adjust_top(above_text, nuclide_to_inch, MeV_to_inch, above_text_offset)
        padding += hor_padding + QEC*(QEC_text_width + bracket_offset + QEC_text_offset)
    decays = decay_scheme.decays
    for decay in decays:
        # this part should be simple, but matplotlib's standard arrows are ugly because their heads are drawn relative to data coordinates; "fancyarrowpatches" do not have this problem, but the variety of head shapes is limitied... so we draw the arrows ourselves
        # may the user ImportanceOfBeingErnest be prosperous and succesful and have many beautiful children! https://stackoverflow.com/questions/53227057/size-distortion-when-rotating-custom-path-marker-in-matplotlib
        x1 = decay.parent_nuclide.index * (1 + hor_padding)
        y1 = decay.parent_level.energy - y_corr if decay.parent_level.energy > y_upper_excl else decay.parent_level.energy
        x2 = decay.daughter_nuclide.index*(1 + hor_padding)
        y2 = decay.daughter_level.energy - y_corr if decay.daughter_level.energy > y_upper_excl else decay.daughter_level.energy

        x1, y1, x2, y2 = calculate_arrow_offsets(x1, y1, x2, y2, nuclide_to_inch, MeV_to_inch)

        draw_arrow(x1, y1, x2, y2)
    decays_to_coordinates = decay_scheme.decays_to_coordinates
    for decay_to_coordinate in decays_to_coordinates:
        x1 = decay_to_coordinate.parent_nuclide.index * (1 + hor_padding)
        y1 = decay_to_coordinate.parent_level.energy - y_corr if decay_to_coordinate.parent_level.energy > y_upper_excl else decay_to_coordinate.parent_level.energy
        x2 = decay_to_coordinate.x
        y2 = decay_to_coordinate.y - y_corr if decay_to_coordinate.y > y_upper_excl else decay_to_coordinate.y

        # index offset
        if x1 < x2:
            x1 += 1

        draw_arrow(x1, y1, x2, y2)
    level_connections = decay_scheme.level_connections
    for level_connection in level_connections:
        nuclide1 = level_connection.nuclide1
        level1 = level_connection.level1
        nuclide2 = level_connection.nuclide2
        level2 = level_connection.level2
        x1 = nuclide1.index*(1 + hor_padding)
        x2 = nuclide2.index*(1 + hor_padding)
        if x1 > x2:
            x2 += 1
        else:
            x1 += 1
        y1 = level1.energy - y_corr if level1.energy > y_upper_excl else level1.energy
        y2 = level2.energy - y_corr if level2.energy > y_upper_excl else level2.energy
        plt.plot([x1, x2], [y1, y2], ls=(1, (3, 1.3)), lw=0.5, color=level1.color)
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
