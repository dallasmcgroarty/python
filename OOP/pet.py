class Pet:
    # class attributes shared by all instances of a class
    # and the class itself
    allowed = set(['cat', 'dog', 'fish', 'rat'])
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self.name = name
        self.species = species
    
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self.species = species
    
cat = Pet('Blue', 'cat')
dog = Pet('Wyatt', 'dog')

cat.set_species('rat')

Pet.allowed.add('pig')
print(Pet.allowed)