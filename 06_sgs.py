### Shot Gun Surgery ###
# https://refactoring.guru/smells/shotgun-surgery

class Minion:
    energy: int
    def attack(self):
        if self.energy < 20:
            self.animate('no-energy')
            self.skip_turn()
            return

    def block(self):
        if self.energy < 10:
            self.animate('no-energy')
            self.skip_turn()
            return

    def move(self):
        if self.energy < 35:
            self.animate('no-energy')
            self.skip_turn()
            return

    
    def animate(self, str):
        pass

    def skip_turn(self):
        pass


# Think about what would happen if we wanted to change the energy checks from less than (<) to less than equal (<=)
# We would have to modify the code in three places which is a sign of shot gun surgery
    
# Suggested
class Minion:
    energy: int

    def check_energy(self, energy_threshold):
        if self.energy < energy_threshold:
            self.animate('no-energy')
            self.skip_turn()
            return

    def attack(self):
        self.check_energy(20)

    def block(self):
        self.check_energy(10)

    def move(self):
        self.check_energy(35)

    
    def animate(self, str):
        pass

    def skip_turn(self):
        pass






















# class Monster:
#     def attack(self):
#         if self.energy < 30:
#             self.animate('no-energy')
#             self.skip_turn()
#             return

#     def roar(self):
#         if self.energy < 10:
#             self.animate('no-energy')
#             self.skip_turn()
#             return

#     def run(self):
#         if self.energy < 20:
#             self.animate('no-energy')
#             self.skip_turn()

    
#     def animate(self, str):
#         pass

#     def skip_turn(self):
#         pass