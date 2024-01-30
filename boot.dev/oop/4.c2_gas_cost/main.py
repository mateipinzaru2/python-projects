"""
GAS COST
A local car dealership has been advertising the average gas cost for a trip, and how much cargo their cars can stow. They have noticed that this has increased their sales dramatically.

They have been doing these calculations by hand, but have asked if you will write them a program that will automate it.

CHALLENGE
Complete the Vehicle, Car, and Truck classes.

VEHICLE CLASS
CONSTRUCTOR
Accepts two parameters (in order) and sets them as instance variables:

max_speed
efficiency

GET_TRIP_COST()
Calculates the cost of gas for a trip:

(distance / efficiency) * fuel_price

GET_CARGO_VOLUME()
This method should be left empty. Use the pass keyword. Child classes will override this method.

TRUCK CLASS
CONSTRUCTOR
Calls the parent constructor, then sets the extra truck-only instance variables as member variables.

GET_TRIP_COST()
Uses the parent method to calculate the cost of gas for a trip, plus the extra cost of carrying a load.

The formula for calculating the cost of gas for a trip is:

base_cost + (load_weight * 0.01)

GET_CARGO_VOLUME()
Returns the cargo capacity of the truck in meters cubed. Get the volume of the truck's bed by multiplying the bed's area and depth. Every truck's bed is 2 meters deep.

CAR CLASS
CONSTRUCTOR
Calls the parent constructor, then sets the extra car-only instance variable as a member variable.

GET_TRIP_COST()
Do not override this method.

GET_CARGO_VOLUME()
Just returns the cargo capacity of the car. This is already set by the constructor.
"""


class Vehicle:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, fuel_price):
        return (distance / self.efficiency) * fuel_price

    def get_cargo_volume(self):
        pass


class Truck(Vehicle):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, fuel_price):
        return super().get_trip_cost(distance, fuel_price) + (self.load_weight * 0.01)

    def get_cargo_volume(self):
        return self.bed_area * 2


class Car(Vehicle):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume
