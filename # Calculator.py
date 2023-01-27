# Multi-use Calculator

print("""
 _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

while True:

    type = input("""Welcome to a multi method calculator
You can choose one of the following calculators - When chosen, the additional options related to the type of calculator will populate.
A - Percentage Calculator
B - Volume Calculator
C - Random Number Generator
Please type a letter:""")

# If Volume cal - provide the additional otpions within an if statement - Once the code is finished, place within the read me, what you would like it to be able to do

# Chosen calculator, how it works and the calculation from user input

# If the user chose A - A percentage calculator, they will be provided a definition and a calculation for their input
    if type == 'A' or type == 'a':
        print("You chose a Percentage Calculator")
        print("""How it works.
25% of 500 = 125
Steps:
25% of 500 = 0.25 × 500 = 125""")
        print("Lets start your calculation!")
        percentage = float(input(f"Please type the percentage (example, type 0.25 for 25%): %"))
        number = float(input(f"You would like %{percentage} of what number? :"))

        # The calculation - Find a method to change the input 25 into 0.25 - for now request it as an decimal input
        calculation = percentage * number 
        print(f"Your answer: %{percentage} of {number} is {calculation}")


# If the user chose B
    elif type == 'B' or type == 'b':
        print("You chose a Volume Calculator")

# List of options the user can choose related to volume, once the user choose a type, the list of conversions will display.
        print() # Empty Space
        volume_choice = input("""Here are your options! Once you choose, a list of additional conversions or how it works will populate
A - Sphere Volume Calculator
B - Cone Volume Calculator
C - Cube Volume Calculator
D - Cylinder Volume Calculator
E - Rectangular Tank Volume Calculator
F - Capsule Volume Calculator
G - Spherical Cap Volume Calculator
H - Conical Frustum Volume Calculator
I - Ellipsoid Volume Calculator
J - Square Pyramid Volume Calculator
K - Tube Volume Calculator
Please tpye your answer here: """)

        # Option A
        if volume_choice == 'a' or volume_choice == 'A':
            print("You Chose A Sphere Volume Calculator")
            print() # Empty space
            print(""" How it works - Example Radius(r) 1 meters 
Volume = 	4/3 πr3
       = 	4/3	×π×13
       = 	4.1887902047864 meters3
""")

        # Option B
        elif volume_choice == 'b' or volume_choice == 'B':
            print("""You chose a Cone Volume Calculator
       ^    
      /|\   
     / | \  
    /  |  \
        
KCK '-.|.-'      
""")
            print("""How it works - Base Radius(r) 1, Height(h) 1 both in meters!
Volume = 1/3 πr2h
       = 1/3 ×π×12×1
       = 1.0471975511966 meters3""")
            print() # Empty space

        # Option C
        elif volume_choice == 'c' or volume_choice == 'C':
            print("You chose a Cube Volume Calculator")
            print("""How it works - Edge Length (a) 1 Meters
Volume = 1(3power) = 1 meters3""")

        # Option D
        elif volume_choice == 'd' or volume_choice == 'D':
            print("You chose Cylinder Volume Calculator")
            print() # Empty space
            print(""" How it works - Example Base Radius (r) = 1 in meters, Height (h) = 2 in meters results in:
volume = 	πr2h
       = 	π×12×2
       = 	2π
       = 	6.2831853071796 meters3
You can also convert using miles, yards, feet, inches and more!
Unfortunately we do not have a calculater available""")

        # Option E
        elif volume_choice == 'e' or volume_choice == 'E':
            print("You chose Rectangular Tank Volume Calculator")
            print() # Empty space
            print("How it works : lenght(l) * width(w) * height(h)")
            rectangular_tank_volume_length = float(input("Please enter a length :"))
            rectangular_tank_volume_width = float(input("Please enter a length :"))
            rectangular_tank_volume_height = float(input("Please enter a length :"))
            rtv_result = rectangular_tank_volume_length * rectangular_tank_volume_width * rectangular_tank_volume_height
            print(f"""The volume of a rectagular tank with a length of {rectangular_tank_volume_length}, a width of {rectangular_tank_volume_width} and a height {rectangular_tank_volume_height}
the result : {rtv_result}""")

        # Option F
        elif volume_choice == 'f' or volume_choice == 'F':
            print("You chose a Capsule Volume Calculator")
            print("""How it works
Volume = 4/3 πr3 + πr2h
       = 4/3 ×π×13 + π×12×1
       = 7.3303828583762 meters3""")
            print() # Empty space

        # Option G
        elif volume_choice == 'g' or volume_choice == 'G':
            print("You chose a Spherical Cap Volume Calculator")
            print("""How it works - The calculator only needs two values. The following result is based on r1 and r2. It is a hemisphere since R=r
It is a hemisphere since R=r.
Example : Base Radius(r) 1, Ball Radius(R) 1, Height(h) in meters
Height = 1 meters
Volume = 1/3 πh2(3R - h)
       = 1/3 ×π×12(3×1 - 1)
       = 	2.0943951023932 meters3 """)

        # Option H
        elif volume_choice == 'h' or volume_choice == 'H':
            print("You chose a Conical Frustum Volume Calculator")
            print("How it works")

        # Option I
        elif volume_choice == 'i' or volume_choice == 'I':
            print("You chose a Ellipsoid Volume Calculator")
            print("How it works")

        # Option J
        elif volume_choice == 'j' or volume_choice == 'J':
            print("You chose a Square Pyramid Volume Calculator")
            print("How it works")

        # Option K
        elif volume_choice == 'k' or volume_choice == 'K':
            print("You chose a Tube Volume Calculator")
            print("How it works")
            

# If the user chose C - A Random Number Generator, they will be provided a definition, additional options and solutions
    elif type == 'C' or type == 'c':
        print("You chose a Random Number Generator")
        random_choice = input("Please choose one of the following!") 

        if random_choice == 'a':
            type = input("""Welcome to a multi method calculator
You can choose one of the following calculators - When chosen, the additional options related to the type of calculator will populate.
A - Percentage Calculator
B - Volume Calculator
C - Random Number Generator
Please type a letter:""")

    else:
        print("Please tpye the letter, a, b or c")

