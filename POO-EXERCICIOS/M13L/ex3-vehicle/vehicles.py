from interface import Vehicles

class Car(Vehicles):
    def __init__(self):
        self.cars = []
        
    def register(self):
        num_cars = int(input("How many cars would you like to add?: "))
        for i in range(num_cars):
            cars_make = input(f"What make is the car {i+1}°:").capitalize()
            cars_type = input("Is the car automatic or manual?").capitalize()
            cars_insurance = input("Have auto insurance(Y/N)?").lower()
            
            has_insurance = True if cars_insurance == 'y' else False

            car_data = {
                "Cars Make": cars_make,
                "Type": cars_type,
                "Insurance": has_insurance
                }
            self.cars.append(car_data)
        print("\nCars registered successfully!")
            
    def consult_vehicle(self):
        if not self.cars:
            print("No cars registered yet.")
            return

        print("\nRegistered Cars:")
        for i, car in enumerate(self.cars, start=1):
            print(f"Car {i}:")
            print(f"Make: {car['Cars Make']}")
            print(f"Type: {car['Type']}")
            print(f"Insurance: {car['Insurance']}")
            
            
class Motorcycle(Vehicles):
    def __init__(self):
        self.motorcycles = []
        
    def register(self):
        num_motorcycle = int(input("How many motorcycles would you like to add?: "))
        for i in range(num_motorcycle):
            motorcycle_make = input(f"What make is the motorcycle {i+1}°:").capitalize()
            motorcycle_type = input("Is the motorcycle automatic or manual?").capitalize()
            motorcycle_insurance = input("Have auto insurance(Y/N)?").lower()
            has_insurance = True if motorcycle_insurance == 'y' else False
            
            motorcycle_data = {
                "Motorcycle Make": motorcycle_make,
                "Type": motorcycle_type,
                "Insurance": has_insurance
                }
            self.motorcycles.append(motorcycle_data)
        print("\nMotorcycles registered successfully!")

    def consult_vehicle(self):
        if not self.motorcycles:
            print("No motorcycles registered yet.")
            return

        print("\nRegistered Motorcycle:")
        for i, motorcycle in enumerate(self.motorcycles, start=1):
            print(f"Motorcycle {i}:")
            print(f"  Make: {motorcycle['Motorcycle Make']}")
            print(f"  Type: {motorcycle['Type']}")
            print(f"  Insurance: {motorcycle['Insurance']}")
        
        
class Truck(Vehicles):
    def __init__(self):
        self.trucks = []
    def register(self):
        num_truck = int(input("How many trucks would you like to add?: "))
        for i in range(num_truck):
            trucks_make = input(f"What make is the truck {i+1}°:").capitalize()
            trucks_type = input("Is the truck automatic or manual?").capitalize()
            trucks_insurance = input("Have auto insurance(Y/N)?").lower()
            has_insurance = True if trucks_insurance == 'y' else False

            truck_data = {
                "Trucks Make": trucks_make,
                "Type": trucks_type,
                "Insurance": has_insurance
                }
            self.trucks.append(truck_data)

    def consult_vehicle(self):
        if not self.trucks:
            print("No trucks registered yet.")
            return

        print("\nRegistered Trucks:")
        for i, truck in enumerate(self.trucks, start=1):
            print(f"Truck {i}:")
            print(f"  Make: {truck['Trucks Make']}")
            print(f"  Type: {truck['Type']}")
            print(f"  Insurance: {truck['Insurance']}")