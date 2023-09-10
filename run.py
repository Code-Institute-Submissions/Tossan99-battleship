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

def validate_num_ships(data):
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


class Battlefield:
    """
    Class that stores data to create and manipulate the game
    """
    def __init__(self, name, board_size, num_ships, type):
        self.name = name
        self.board_size = int(board_size)
        self.num_ships = int(num_ships)
        self.type = type
        self.board = [["." for x in range(self.board_size)] for y in range(self.board_size)]
        self.ships = []
        self.guesses = []

    def add_ships(self):
        while len(self.ships) < self.num_ships:
            x = randint(0, self.board_size - 1)
            y = randint(0, self.board_size - 1)
            if self.type == "player":
                if [x, y] not in self.ships:
                    self.board[x][y] = "@"
                    self.ships.append([x, y])
            else:
                if [x, y] not in self.ships:
                    self.ships.append([x, y])
        print(self.ships)

    def create_board(self):
        print(f"{self.name}'s board")
        print("¤ 0 1 2 3 4 5 6 7")
        i = 0
        for x in self.board:
            print(i, *x)
            i += 1
        print("-"*30)
    
    def validate_guess(self, data):
        """
        Validates the users input for guess
        """
        try:
            if not data.isdigit():
                raise ValueError(f"You can only guess a whole number. You have entered: {data}")
            if int(data) > self.board_size - 1:
                raise ValueError(f"Largest number you can guess is {self.board_size - 1}. You have guessed: {data}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again \n")
            return False
        return True
    
    def player_guess(self):
        while True:
            print("guess")
            x = input("Guess a row: ")
            if self.validate_guess(x):
                print()
                break
        while True:
            print("guess")
            y = input("Guess a column: ")
            if self.validate_guess(y):
                print()
                break
        guess = [int(x), int(y)]
        if guess in self.ships:
            print("hit")
        else:
            print("miss")
        self.guesses.append(guess)



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
        num_ships = input("Choose how many ships you want each player to have: ")
        if validate_num_ships(num_ships):
            print()
            break
    
    global user
    user = Battlefield(username, board_size, num_ships, "player")
    user.add_ships()
    user.create_board()

    global computer
    computer = Battlefield("Computer", board_size, num_ships, "comp")
    computer.add_ships()
    computer.create_board()
    
    user.player_guess()

main()
