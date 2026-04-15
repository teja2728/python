''''
3. Core Python: The "FareCalc" Travel Optimizer
Business Case: A ride-sharing startup, "CityCab," needs a backend script to calculate fares. The fare isn't flat; it changes based on the time of day (Peak Hours) and the type of vehicle requested.
Problem Statement
Write a script that calculates the final "Ride Estimate" based on distance, vehicle type, and a "Surge Pricing" multiplier.
Student Tasks:
1.	Dictionary Mapping: Store rates in a dictionary: {'Economy': 10, 'Premium': 18, 'SUV': 25} (rates per km).
2.	Surge Logic: Ask the user for the "Hour of Day" (0-23). If the hour is between 17 and 20 (5 PM - 8 PM), apply a 1.5x Surge Multiplier to the total.
3.	Function Definition: Create a function calculate_fare(km, type, hour) that returns the final price.
4.	Error Handling: If the user enters a vehicle type not in your dictionary, use a try-except block or an if-in check to provide a "Service Not Available" message.
Deliverable: A .py script that takes user input and prints a formatted "Price Receipt."
'''

def calculate_fare(km, vtype, hour):
    ctype={'Economy': 10, 'Premium': 18, 'SUV': 25}
    if vtype not in ctype:
        return -1
    charge = km*ctype[vtype]
    if (hour>=17 and hour<=20):
        print("Applying Surge Price(1.5x)")
        charge= charge * 1.5
    return charge
try:
    print()
    dis=float(input("Enter Distance"))
    vehicle= input("Enter Vehicle Type(Economy / Premium / SUV)")
    hour = int(input("Enter Hours (0-23)"))
    final_price= calculate_fare(dis,vehicle,hour)
    if(final_price==-1):
        print("Service Not Available")
    else:
        print("\nReceipt")
        print("Distance :",dis)
        print("Vehicle :", vehicle)
        print("Hour :",hour)
        print("Amount :",round(final_price,2))
except ValueError:
    print("Service Not Available")