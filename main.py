# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

# Define a repair() method that will update the condition of the podracer to "repaired".
        
    def repair(self):
        if self.condition == 'trashed':
            self.condition = 'repaired'
        else:
            print('Repair not needed.')


# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
            
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class SebulbasPod(Podracer):
    def flame_jet(self, other):
        other.condition = 'trashed'



podracer1 = Podracer(max_speed=500, condition='perfect', price=10000)

anakins_pod = AnakinsPod(max_speed=600, condition='perfect', price=20000)
print(anakins_pod.max_speed)
anakins_pod.boost()
print(anakins_pod.max_speed)


sebulbas_pod = SebulbasPod(max_speed=700, condition='perfect', price=25000)
sebulbas_pod.flame_jet(podracer1)
print(podracer1.condition)


podracer1.repair()
print(podracer1.condition)

# Once an Object Oriented solution has been implemented, answer the following questions:
# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# How in particular did Object Oriented Programming assist in the solving of this problem?