class Character():

    def __init__(self, real_name, superhero_name):
        self.real_name = real_name
        self.superhero_name = superhero_name

    def set_power(self, power):
        self.power = power

    def get_power(self):
        print(self.power)