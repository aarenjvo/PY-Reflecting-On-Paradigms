# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        arr.append(item)
    return sorted(arr)

print(flatten_and_sort([2, 3, 1, 9, 5, 23, 16, 8]))


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
    def flame_jet(self):
        self.condition = 'trashed'



podracer1 = Podracer(max_speed=500, condition='perfect', price=10000)

anakins_pod = AnakinsPod(max_speed=2, condition='perfect', price=20000)
print(anakins_pod.max_speed)
# use boost() to multiply anakins_pod max_speed by 2
anakins_pod.boost()
print(anakins_pod.max_speed)


sebulbas_pod = SebulbasPod(max_speed=700, condition='perfect', price=25000)
# set sebulbas pod to trashed with flame_jet()
sebulbas_pod.flame_jet()
print(sebulbas_pod.condition)
# repair sebulbas_pod with repair()
sebulbas_pod.repair()
print(sebulbas_pod.condition)