from random import randint
import random


def validate_board_size(data):
    """
    Validates the users input for board size
    """
    try:
        if not data.isdigit():
            raise ValueError(
                f"You can only enter whole numbers. You have entered: {data}")
        if int(data) < 4:
            raise ValueError(
                f"Smalest battlefield is 4x4. You have entered: {data}")
        if int(data) > 8:
            raise ValueError(
                f"Largest battlefield is 8x8. You have entered: {data}")
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
            raise ValueError(
                f"You can only enter whole numbers. You have entered: {data}")
        if int(data) < 2:
            raise ValueError(
                f"Least amount of battleships is 2. You have entered: {data}")
        if int(data) > 8:
            raise ValueError(
                f"Most amount of battleships is 8. You have entered: {data}")
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
        self.board = [["." for y in range(self.board_size)]
                      for x in range(self.board_size)]
        self.ships = []
        self.guesses = []
        self.score = 0

    def add_ships(self):
        while len(self.ships) < self.num_ships:
            y = randint(0, self.board_size - 1)
            x = randint(0, self.board_size - 1)
            if self.type == "player":
                if [y, x] not in self.ships:
                    self.board[x][y] = "@"
                    self.ships.append([y, x])
            else:
                if [y, x] not in self.ships:
                    self.ships.append([y, x])
        print(self.ships)

    def create_board(self):
        print(f"{self.name}'s board. Score: {self.score}")
        print("-"*30)
        print("¤ 0 1 2 3 4 5 6 7")
        i = 0
        for j in self.board:
            print(i, *j)
            i += 1
        print("-"*30)

    def validate_guess(self, data):
        """
        Validates the users input for guess
        """
        try:
            if not data.isdigit():
                raise ValueError(
                    f"You can only guess a whole number. You have entered: {data}")
            if int(data) > self.board_size - 1:
                raise ValueError(
                    f"Largest number you can guess is {self.board_size - 1}. You guessed: {data}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again \n")
            return False
        return True

    def check_guesses(self, data):
        try:
            if data in self.guesses:
                raise ValueError(
                    f"You have already guessed: {data}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again \n")
            return False
        return True

    def calculate_hit(self, data):
        if data in self.ships:
            self.board[data[0]][data[1]] = "X"
            self.guesses.append(data)
            print("true")
            return 1
        else:
            print("missed!")
            self.board[data[0]][data[1]] = "-"
        print("guess appended")
        self.guesses.append(data)

    def player_guess(self):
        while True:
            while True:
                y = input("Guess a row: ")
                if self.validate_guess(y):
                    break
            while True:
                x = input("Guess a column: ")
                if self.validate_guess(x):
                    break
            guess = [int(y), int(x)]
            if self.check_guesses(guess):
                break
        self.calculate_hit(guess)

    def computer_guess(self):
        y = randint(0, self.board_size - 1)
        x = randint(0, self.board_size - 1)
        guess = [y, x]
        self.calculate_hit(guess)
    
    def give_score(self):
        print(f"{self.name} hit!")
        self.score += 1

    def check_score(self):
        if self.score >= self.num_ships:
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
        board_size = input(
            "Enter a number between 4-8 to choose your battlefield size: ")
        if validate_board_size(board_size):
            print()
            break

    while True:
        print("Number of battleships ranges from 2-8")
        num_ships = input(
            "Choose how many ships you want each player to have: ")
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

    while True:
        if computer.player_guess() == 1:
            print("returned")
            user.give_score()
        if user.computer_guess():
            computer.give_score()
        user.create_board()
        computer.create_board()
        if user.check_score() or computer.check_score():
            break
    print("Game over")


main()


"""
noted bugs
"""

#Points is given to computer instead of the player
#Also says computer hit when player hit
#Hits didnt register in the guesses list