# functions go here
def yes_no(question):
    """checks that users enter yes / y or no / n to a question """

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return  "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")


# Main routine here

# loop
while True:
    want_instructions = yes_no("do you want to read the instructions? ")
    print(f"you chose {want_instructions}\n")
