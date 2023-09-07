from random import randint
import random

def validate_board_size(data):
    """
    Validates the players input for board size
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
            break


main()
