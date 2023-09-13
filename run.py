from random import randint
import random


def validate_input(data, minn, maxx):
    """
    Validates the users inpsrd sizeetting up the Battlefield
    """
    try:
        if not data.isdigit():
            raise ValueError(
                f"You can only enter whole numbers. You have entered: {data}")
        if int(data) < minn:
            raise ValueError(
                f"Lowest number you can choose is {minn}. You have entered: {data}")
        if int(data) > maxx:
            raise ValueError(
                f"Highest number you can choose is {maxx}. You have entered: {data}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again \n")
        return False
    return True


def validate_play_again(data):
    """
    Validates the users input for play again
    """
    try:
        if data != "yes" and data != "no":
            raise ValueError(
                f"You can only answer 'yes' or 'no'. You have answered: {data}")
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
            return True
        else:
            print("missed!")
            self.board[data[0]][data[1]] = "-"
            self.guesses.append(data)
            print("false")
            return False

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
        if self.calculate_hit(guess):
            return True

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
        if validate_input(board_size, 4, 8):
            break
        print()

    while True:
        print("Number of battleships ranges from 2-8")
        num_ships = input(
            "Choose how many ships you want each player to have: ")
        if validate_input(num_ships, 2, 8):
            break
        print()
    
    global computer
    computer = Battlefield("Computer", board_size, num_ships, "comp")
    global user
    user = Battlefield(username, board_size, num_ships, "player")
    
    user.add_ships()
    user.create_board()
    computer.add_ships()
    computer.create_board()

    while True:
        if computer.player_guess():
            user.give_score()
        if user.computer_guess():
            computer.give_score()
        user.create_board()
        computer.create_board()
        if user.check_score():
            print("You Won!\n")
            break
        elif computer.check_score():
            print("You Lost!\n")
            break
    
    while True:
        print("Do you want to play again?")
        play_again = input("yes or no?: ").lower()
        if validate_play_again(play_again):
            break
        print()

    if play_again == "yes":
        main()
    if play_again == "no":
        print("Thank you for playing Battleships!\n")


main()


"""
noted bugs
"""


#Någon skillnad på if och elif
#Points is given to computer instead of the player
"""
def give_score(self):
        print(f"{self.name} hit!")
        self.score += 1
"""
#Also says computer hit when player hit
#Hits didnt register in the guesses list Needed to append for both since i did return
#column numbers went up to 7 for all board sizes
#you can guess several 0's