class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# 1. Code Duplication
#class GingerChai(Chai):
#    def __init__(self, type_, strength, spice_level):
#        self.type = type_
#        self.strength = strength
#        self.spice_level = spice_level

# 2. Explicit call way
#class GingerChai(Chai):
#   def __init__(self, type_, strength, spice_level):
#       Chai.__init__(self, type_, strength)
#       self.spice_level = spice_level

# 3. using super() keyword
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level