from random import randint
import random

def validate_board_size(data):
    """
    Validates the users input for board size
    """
    try:
        if not data.isdigit():
            raise ValueError(f"You can only enter whole numbers. You have entered: {data}")
        if int(data) < 4:
            raise ValueError(f"Smalest battlefield is 4x4. You have entered: {data}")
        if int(data) > 8:
            raise ValueError(f"Largest battlefield is 8x8. You have entered: {data}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again \n")
        return False
    return True

def validate_num_of_ships(data):
    """
    Validates the users input for number of ships
    """
    try:
        if not data.isdigit():
            raise ValueError(f"You can only enter whole numbers. You have entered: {data}")
        if int(data) < 2:
            raise ValueError(f"Least amount of battleships is 2. You have entered: {data}")
        if int(data) > 8:
            raise ValueError(f"Most amount of battleships is 8. You have entered: {data}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again \n")
        return False
    return True



def main():
    """
    Calls all functions
    """

    print("Welcome to Battleships")
    username = input("Enter your username: ")
    print()

    while True:
        print("Battlefield size ranges from 4x4-8x8")
        board_size = input("Enter a number between 4-8 to choose your battlefield size: ")
        if validate_board_size(board_size):
            print()
            break
    
    while True:
        print("Number of battleships ranges from 2-8")
        num_of_ships = input("Choose how many ships you want each player to have: ")
        if validate_num_of_ships(num_of_ships):
            print()
            break


main()
