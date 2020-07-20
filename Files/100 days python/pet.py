class Pet:
    allowed=['cat','rat','fish','dog']
    def __init__(self,name,species):
        if species not in Pet.allowed:
            raise ValueError(f"you cannot have {species} pet!")
        def set_species(self,species):
            if species not in Pet.allowed:
                raise ValueError(f"you cant have a {species} pet !")
            self.species=species
        self.name=name
        self.species =species
cat =Pet("blue","cat")
dog=Pet("wyatt","dog")
