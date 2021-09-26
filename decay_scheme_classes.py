import bisect

class decay_scheme:
    def __init__(self):
        self.nuclides = []
        self.current_nuclide = 0
        self.num_nuclides = 0
        self.decays = []
        self.decays_to_coordinates = []
        self.level_connections = []
        self.freetexts = []
        self.freearrows = []
    
    def add_nuclide(self, nuclide):
        bisect.insort(self.nuclides, nuclide)
        self.num_nuclides += 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_nuclide == self.num_nuclides:
            self.current_nuclide = 0
            raise StopIteration
        self.current_nuclide += 1
        return self.nuclides[self.current_nuclide - 1]
    
    def __repr__(self):
        result = "------ Decay scheme ------\n"
        for nuclide in self.nuclides:
            result += nuclide.__repr__() + "\n"
        return result
    
    def add_decay(self, decay):
        self.decays.append(decay)
    
    def add_decay_to_coordinate(self, decay_to_coordinate):
        self.decays_to_coordinates.append(decay_to_coordinate)

    def add_level_connection(self, level_connection):
        self.level_connections.append(level_connection)

    def add_freetext(self, freetext):
        self.freetexts.append(freetext)


class nuclide:
    def __init__(self, index, name):
        if index < 0:
            raise SystemExit("code does not support nuclides with index < 0, aborting")
        self.index = index
        self.name  = name
        self.levels = []
        self.current_level = 0
        self.num_levels = 0
    
    def add_level(self, level):
        bisect.insort(self.levels, level)
        self.num_levels += 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_level == self.num_levels:
            self.current_level = 0
            raise StopIteration
        self.current_level += 1
        return self.levels[self.current_level - 1]
    
    def __lt__(self, other):
        return self.index < other.index
    
    def __repr__(self):
        result = self.name + " (id=%i): " % self.index
        for level in self.levels:
            result += level.__repr__() + ";   "
        result = result[0:-4] if self.levels else result[0:-2]
        return result


class level:
    def __init__(self, energy, spin, parity, 
                 ls='-', lw=1., color='k', text_above='', text_below='', 
                 energy_format_string="",
                 draw_QEC_level_below=False,
                 draw_reference_line=False,
                 hide_energy_spin_parity=False, energy_spin_parity_below=False, 
                 broad=False, many=False, upper_energy=0., upper_spin='', upper_parity='',
                 energy_x_adjust=0., energy_y_adjust=0.,
                 spin_parity_x_adjust=0., spin_parity_y_adjust=0.,
                 text_above_x_adjust=0., text_above_y_adjust=0.,
                 text_below_x_adjust=0., text_below_y_adjust=0.,
                 QEC_x_adjust=0., QEC_y_adjust=0.,
                 upper_energy_x_adjust=0., upper_energy_y_adjust=0.,
                 upper_spin_parity_x_adjust=0., upper_spin_parity_y_adjust=0.):
        self.energy = energy
        self.spin = spin
        self.parity = parity
        self.ls = ls
        self.lw = lw
        self.color = color
        self.text_above = text_above
        self.text_below = text_below
        self.energy_format_string = energy_format_string
        self.draw_QEC_level_below = draw_QEC_level_below
        self.draw_reference_line = draw_reference_line
        self.hide_energy_spin_parity = hide_energy_spin_parity
        self.energy_spin_parity_below = energy_spin_parity_below
        self.broad = broad
        self.many = many
        self.upper_energy = upper_energy
        self.upper_spin = upper_spin
        self.upper_parity = upper_parity
        self.energy_x_adjust = energy_x_adjust
        self.energy_y_adjust = energy_y_adjust
        self.spin_parity_x_adjust = spin_parity_x_adjust
        self.spin_parity_y_adjust = spin_parity_y_adjust
        self.text_above_x_adjust = text_above_x_adjust
        self.text_above_y_adjust = text_above_y_adjust
        self.text_below_x_adjust = text_below_x_adjust
        self.text_below_y_adjust = text_below_y_adjust
        self.QEC_x_adjust = QEC_x_adjust
        self.QEC_y_adjust = QEC_y_adjust
        self.upper_energy_x_adjust = upper_energy_x_adjust
        self.upper_energy_y_adjust = upper_energy_y_adjust
        self.upper_spin_parity_x_adjust = upper_spin_parity_x_adjust
        self.upper_spin_parity_y_adjust = upper_spin_parity_y_adjust
    
    def __lt__(self, other):
        return self.energy < other.energy
    
    def __repr__(self):
        return "E=%2.3f, J=%s, π=%s" % (self.energy, self.spin, self.parity)


class decay:
    def __init__(self, parent_nuclide, parent_level, daughter_nuclide, daughter_level):
        self.parent_nuclide = parent_nuclide
        self.parent_level = parent_level
        self.daughter_nuclide = daughter_nuclide
        self.daughter_level = daughter_level


class decay_to_coordinate:
    def __init__(self, parent_nuclide, parent_level, x, y):
        self.parent_nuclide = parent_nuclide
        self.parent_level = parent_level
        self.x = x
        self.y = y


class level_connection:
    def __init__(self, nuclide1, level1, nuclide2, level2):
        self.nuclide1 = nuclide1
        self.level1 = level1
        self.nuclide2 = nuclide2
        self.level2 = level2


class freetext:
    def __init__(self, text, x, y, va='center', ha='center'):
        self.text = text
        self.x = x
        self.y = y
        self.va = va
        self.ha = ha

