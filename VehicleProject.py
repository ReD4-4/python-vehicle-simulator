
# This program simulates a vehicle dealership where the user can choose to purchase a Truck, Car, or Motorcycle. The program then displays the features of the chosen vehicle, such as ignition, radio, and condition.

class Vehicle:
    def miles(self, miles): 
        print(f"This vehicle has {miles} miles on it")

    def ignition(self, condition):
        if condition >= 25:
            print("Vroom\nIgnition is on")
        else:
            print("vehicle is in poor condition and cannot start")

    def radio(self):
        print("Radio tuned and playing music")

    def condition(self, wear):
        if wear >= 25:
            print("Vehicle is in good condition")
        else:
            print("Vehicle is in poor condition")

class vehicleDealership:
    def getVehicleChoice(self):
        print("Welcome to the Vehicle Dealership! Would you like to buy a Truck, Car, or Motorcycle?")
        if input("Type 'yes' to continue: ") == "yes":
            vehicleChoice = input("Great! Which vehicle do you want to buy? (Truck, Car, Motorcycle): ")
            if vehicleChoice.lower() == "truck":
                print("You have purchased a Truck")
            elif vehicleChoice.lower() == "car":
                print("You have purchased a Car")
            elif vehicleChoice.lower() == "motorcycle":
                print("You have purchased a Motorcycle")
            return vehicleChoice
        else:
            print("Thank you for visiting the Vehicle Dealership. Have a great day!")
    def getvehicleOwned(self):
        return True





dealership = vehicleDealership()
vehicleChoice = dealership.getVehicleChoice()
vehicleOwned = dealership.getvehicleOwned()

    

if vehicleChoice == "truck":
    Truck = Vehicle()
    Truck.ignition(100)
    Truck.radio()
    Truck.condition(100)
    Truck.miles(0)

elif vehicleChoice == "car":
    Car = Vehicle()
    Car.ignition(100)
    Car.radio()
    Car.condition(100)
    Car.miles(0)

elif vehicleChoice == "motorcycle":
    Motorcycle = Vehicle()
    Motorcycle.ignition(100)
    Motorcycle.radio()
    Motorcycle.condition(100)
    Motorcycle.miles(0)


while vehicleOwned == True: 
    menuoption= input("Type the number you want to see more options for! \n\n1.Check Vehicle Levels \n\n2.Choose a Destination \n\n3.Make a Stop \n\n4.Interrupt Journey(restart)")
    if menuoption == "1":
        print("Checking vehicle levels...")
     
    elif menuoption == "2":
        print("Choosing a destination...")
        
    elif menuoption == "3":
        print("Making a stop...")
    elif menuoption == "4":
        print("Interrupting journey and restarting...")

  






