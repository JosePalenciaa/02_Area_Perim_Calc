# function goes here
def num_check(question):

    # checks that user has enter a number more than zero
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero2."

        try:

            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)


# Extra added
print()
print("~~ Area Perimeter Calculator ~~")
print()

# Main routine goes here

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")
    print()
    # Calculate area (Width * Height)
    area = width * height

    # Calculate perimeter (Width + Height) x 2
    perimeter = 2 * (width + height)

    # Outputs area and perimeter
    print("Perimeter: {:.2f} units.". format(perimeter))
    print("Area: {:.2f} units.". format(area))
    print()
    keep_going = input("Press <enter> to keep going or any key to quit.")
    
print()
print("Thanks for using the Area / Perimeter calculator.")