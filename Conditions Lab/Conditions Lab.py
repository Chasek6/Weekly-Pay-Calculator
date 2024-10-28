#Chase Stratton 
#LAB Conditions 
# 5 POINTS 
# Simple code for 3 exam grades to calculate the average!

# First user input for grades here!
grade1 = float(input("Enter the first Exam Grade here:"))
# Second inout for grades here !
grade2 = float(input("Enter the second Exam Grade here:"))
# Third input user input ofr grades here!
grade3 = float(input("Enter the third Exam Grade here:"))


# Below the code will calculate the average of all exam inputs from user
average =(grade1 + grade2 + grade3) / 3

# Displaying the results using print function 

print ("Average grade:", average)

# If and Else statements 
# Along with print to along user to know if their hired or not.
if average>= 70:
    print("Student Passes!")
else:  
    print("Student Failed!")