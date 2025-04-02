# functions go here
def int_check(question, low, high):
    """checks if users enter an integer between two values"""

    error = f"oops - please enter an integer between {low} and {high}."

    while True:

        try:
            # change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# main routine goes here

# loop
while True:

    print()

    # ask user for an integer
    my_num = int_check("choose a number: ", 1, 10)
    print(f"you chose {my_num}")
