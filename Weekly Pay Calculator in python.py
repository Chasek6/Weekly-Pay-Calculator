#Chase Stratton
#Assignment conditions Python
#10 points
# Sep 22nd 2024



#Weekly Pay Calculator: Money Matters

# This will be the input section (Essentials from the user goes here!)
# will prompt two questions for the user to input here 
hourly_wage = float(input("Hey there! What is your hourly wage? $ "))

hours_worked = float(input("Aright, now tell me how many hours did you work this week:"))

# Here we will set up the constants 
# Regular hours worked and the overtime hours difference 
REGULAR_HOURS = 40
OVERTIME_MULTIPLIER = 1.5

# Here will be code to calculate pay by the hour (step nby step)

if hours_worked > REGULAR_HOURS:

    # Here will be an Overtime Alert 
    
    overtime_hours = hours_worked - REGULAR_HOURS
    regular_pay = REGULAR_HOURS * hourly_wage
    overtime_pay = overtime_hours * hourly_wage * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay

    # Print overtime message
    print(f"You worked {overtime_hours:.2f} hours of overtime this week!")

else:   
    # No overtime hours worked this week! Normal Calculations 

    total_pay = hours_worked * hourly_wage
    print("NO overtime hours worked this week. Try again next week!")   


# No overtime hours worked this week! Normal Calculations 
total_pay = hours_worked * hourly_wage
print ("NO overtime hours worked this week Try again next week!")



# Closing Code ( Showing the Money made)
print (f" Your total pay for the week is :${total_pay:.2f}.")