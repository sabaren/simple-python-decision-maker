# Decision Maker by Nicholaus Sabare
# This program will ask the user for a set of decisions and return a random decision back

import random

# Define the main function for the decision maker
def decision_maker():
    # Initialize an empty list to store the decisions
    decisions = []
    # Initialize a variable to track the user's choice
    choices = 0
    # Initialize a variable to track whether the program should exit
    do = 0
    
    # Print a welcome message
    print("Welcome to the decision maker: \n")
    
    # Loop until the user chooses to exit
    while do != -1:
        # Print the menu options
        print("1. Add Decision")
        print("2. View Decisions")
        print("3. Make Decision")
        print("4. Delete Decision")
        print("5. Exit \n")
        
        # Get the user's choice
        choices = input("Choose an option: \n")
        
        # Handle the user's choice
        if choices == "1":
            # Get the decision from the user and add it to the list
            decision = input("Add a decision: ")
            print(f"{decision} has been added. \n")
            decisions.append(decision)
        elif choices == "2":
            # Check if there are any decisions to view
            if len(decisions) > 0:
                # Print the decisions
                print("\nDecisions: ")
                for i, decision in enumerate(decisions, start=1):
                    print(f"{i}. {decision}")
                print()
            else:
                # Print a message if there are no decisions
                print("No decisions have been added.\n")
        elif choices == "3":
            # Check if there are any decisions to make
            if len(decisions) == 0:
                # Print a message if there are no decisions
                print("Please add decisions")
                print()
            else:
                # Make a random decision
                print(random.choice(decisions))
                print()
        elif choices == "4":
            # Check if there are any decisions to delete
            if len(decisions) == 0:
                # Print a message if there are no decisions
                print("Please add decisions")
                print()
            else:
                # Print the decisions and ask the user which one to delete
                print("\n Decisions: ")
                for i, decision in enumerate(decisions, start=1):
                    print(f"{i}. {decision}")
                print()
                delete = 0
                delete = int(input("Which decision do you want to delete?(starting from 1): "))
                # Check if the user's choice is valid
                if delete > 0 and delete <= len(decisions):
                    # Delete the decision
                    print(f"{decisions[delete - 1]} has been deleted")
                    del decisions[delete - 1]
                    print()
                else:
                    # Print an error message if the user's choice is invalid
                    print("Invalid choice")
                    print()
        elif choices == "5":
            # Print a farewell message and exit the program
            print("Thank you for using the decision maker. Farewell.")
            do = -1
            print()
        else:
            # Print an error message if the user's choice is not recognized
            print("Please choose an option from the menu:")
            print()
    
    # Print a message to confirm that the program has exited
    print("Program exitted")

# Call the main function
decision_maker()