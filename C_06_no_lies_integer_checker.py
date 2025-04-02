# Functions go here
def int_check(question):
    """Checks users enter an integer"""

    error = "oops - please enter an integer"

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# main routine here

# loop for testing
while True:
    print()

    # ask user for their name
    name = input("Name: ") # replace with call to 'not blank' function

    # ask for their age and check if its between 12 and 120
    age = int_check("Age: ")

    # output error/success message
    if age <12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")
