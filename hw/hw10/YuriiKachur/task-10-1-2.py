class Human:
    species = "Homosapiens"  # Class variable for species

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome {self.name}!"

    @classmethod
    def species_info(cls):
        return f"The species is {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."
