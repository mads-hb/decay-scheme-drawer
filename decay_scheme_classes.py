import bisect

class decay_scheme:
    def __init__(self):
        self.nuclides = []
        self.current_nuclide = 0
        self.num_nuclides = 0
        self.decays = []
        self.decays_to_coordinates = []
        self.freetexts = []
    
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
                 draw_QEC_level_below=False, 
                 hide_energy_spin_parity=False, energy_spin_parity_below=False, 
                 broad=False, upper_energy=0., upper_spin='', upper_parity=''):
        self.energy = energy
        self.spin = spin
        self.parity = parity
        self.ls = ls
        self.lw = lw
        self.color = color
        self.text_above = text_above
        self.text_below = text_below
        self.draw_QEC_level_below = draw_QEC_level_below
        self.hide_energy_spin_parity = hide_energy_spin_parity
        self.energy_spin_parity_below = energy_spin_parity_below
        self.broad = broad
        self.upper_energy = upper_energy
        self.upper_spin = upper_spin
        self.upper_parity = upper_parity
    
    def __lt__(self, other):
        return self.energy < other.energy
    
    def __repr__(self):
        return "E=%2.3f, J=%s, π=%s" % (self.energy, self.spin, self.parity)

# wip
class decay:
    def __init__(self, parent_nuclide, parent_level, daughter_nuclide, daughter_level, 
                 ls='-', lw=1., color='k', arrowstyle='-|>'):
        self.parent_nuclide = parent_nuclide
        self.parent_level = parent_level
        self.daughter_nuclide = daughter_nuclide
        self.daughter_level = daughter_level
        self.lw = lw
        self.ls = ls
        self.color = color
        self.arrowstyle = arrowstyle

# wip
class decay_to_coordinate:
    def __init__(self, parent_nuclide, parent_level, x, y, 
                 ls='-', lw=1., color='k', arrowstyle='-|>'):
        self.parent_nuclide = parent_nuclide
        self.parent_level = parent_level
        self.x = x
        self.y = y
        self.ls = ls
        self.lw = lw
        self.color = color
        self.arrowstyle = arrowstyle

class freetext:
    def __init__(self, text, x, y, va='center', ha='center'):
        self.text = text
        self.x = x
        self.y = y
        self.va = va
        self.ha = ha
