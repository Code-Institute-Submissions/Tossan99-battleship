from random import randint
import random
import messages


def validate_input(data, min, max):
    """
    Validates users input for setting up the battlefield
    """
    try:
        if not data.isdigit():
            raise ValueError(
                f"You can only enter one whole number."
                f"\n You have entered: {data}")
        if int(data) < min:
            raise ValueError(
                f"Smallest number you can enter is {min}."
                f"\n You have entered: {data}")
        if int(data) > max:
            raise ValueError(
                f"Biggest number you can enter is {max}."
                f"\n You have entered: {data}")
    except ValueError as e:
        print(f"\n Invalid input: {e}. Please try again.")
        return False
    return True


def validate_answer(data):
    """
    Validates users input answering 'yes' or 'no'
    """
    try:
        if data != "yes" and data != "no":
            raise ValueError(
                f"You can only answer 'yes' or 'no'."
                f"\n You have answered: {data}")
    except ValueError as e:
        print(f"\n Invalid input: {e}. Please try again.")
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
        """
        Adds visible ships to the players board
        Adds locations of the ships, in form of coordinates, to a list
        """
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

    def render_board(self):
        """
        Renders the board each turn
        """
        print(f"\n {self.name}'s board \\\\ Score: {self.score}")
        column_num = [column for column in range(len(self.board))]
        print(" ¤", *column_num)
        row_num = 0
        for row in self.board:
            print("", row_num, *row)
            row_num += 1

    def validate_guess(self, data):
        """
        Validates the users input when guessing rows and columns
        """
        try:
            if not data.isdigit():
                raise ValueError(
                    f"You can only enter one whole number."
                    f"\n You have entered: {data}")
            if int(data) > self.board_size - 1:
                raise ValueError(
                    f"Biggest number you can enter is {self.board_size - 1}."
                    f"\n You entered: {data}")
        except ValueError as e:
            print(f"\n Invalid input: {e}. Please try again.")
            return False
        return True

    def check_guesses(self, data):
        """
        Checks if the guess already have been guessed
        """
        try:
            if data in self.guesses:
                raise ValueError(
                    f"You have already guessed: {data}")
        except ValueError as e:
            print(f"\n Invalid input: {e}. Please try again.")
            return False
        return True

    def calculate_hit(self, data):
        """
        Calculates if the guess is correct or not
        Appends the guess to the llist of guesses
        """
        if data in self.ships:
            self.board[data[0]][data[1]] = "X"
            self.guesses.append(data)
            return True
        else:
            self.board[data[0]][data[1]] = "/"
            self.guesses.append(data)
            return False

    def player_guess(self):
        """
        Takes input from the user and calls functions to
        validate input, check guesses and calculates hits and misses
        """
        while True:
            while True:
                print(self.ships)
                y = input("\n Guess a row: ")
                if self.validate_guess(y):
                    break
            while True:
                x = input(" Guess a column: ")
                if self.validate_guess(x):
                    break
            guess = [int(y), int(x)]
            print(f" You have guessed coordinates: {y}, {x}")
            if self.check_guesses(guess):
                break
        if self.calculate_hit(guess):
            return True
        else:
            return False

    def computer_guess(self):
        """
        Generates a random coordinate and calls
        a function to calculate hits and misses
        """
        while True:
            y = randint(0, self.board_size - 1)
            x = randint(0, self.board_size - 1)
            guess = [y, x]
            if guess not in self.guesses:
                break
        print(f"\n Computer have guessed coordinates: {y}, {x}")
        if self.calculate_hit(guess):
            return True
        else:
            return False

    def hit(self):
        """
        Prints out if someone hit and gives score
        """
        print(f"\n {self.name} hit!")
        self.score += 1

    def miss(self):
        """
        Prints out if someone missed
        """
        print(f"\n {self.name} missed!")

    def check_score(self):
        """
        Checks if someone have sunk all the ships
        """
        if self.score >= self.num_ships:
            print(f"\n {self.name} wins the game!")
            return True


def main():
    """
    Holds while loops and calls functions to run the game
    """
    print(messages.welcome)

    while True:
        print("\n Do you want to read the game rules?")
        read_gamerules = input("\n Yes or No?: ").lower()
        if validate_answer(read_gamerules):
            break
    if read_gamerules == "yes":
        print(messages.rules)

    username = input("\n Enter your username: ")

    while True:
        print("\n Choose the size of the battlefield")
        board_size = input(" Enter a number between 3-6: ")
        if validate_input(board_size, 3, 6):
            break

    while True:
        print("\n Choose how manny battleships you want")
        num_ships = input(" Enter a number between 2-8: ")
        if validate_input(num_ships, 2, 8):
            break

    computer = Battlefield("Computer", board_size, num_ships, "comp")
    user = Battlefield(username, board_size, num_ships, "player")

    user.add_ships()
    computer.add_ships()
    user.render_board()
    computer.render_board()

    while True:
        if computer.player_guess():
            user.hit()
        else:
            user.miss()

        if user.computer_guess():
            computer.hit()
        else:
            computer.miss()

        user.render_board()
        computer.render_board()

        if user.check_score():
            print(messages.win)
            break
        elif computer.check_score():
            print(messages.lose)
            break

    while True:
        print("\n Do you want to play again?")
        play_again = input(" Yes or No?: ").lower()
        if validate_answer(play_again):
            break

    if play_again == "yes":
        main()
    if play_again == "no":
        print(messages.thank_you)


main()
