from random import randint
import random


def validate_input(data, minn, maxx):
    """
    Validates the users input for setting up the battlefield
    """
    try:
        if not data.isdigit():
            raise ValueError(
                f"You can only enter one whole number. You have entered: {data}")
        if int(data) < minn:
            raise ValueError(
                f"Smallest number you can choose is {minn}. You have entered: {data}")
        if int(data) > maxx:
            raise ValueError(
                f"Biggest number you can choose is {maxx}. You have entered: {data}")
    except ValueError as e:
        print(f"\n Invalid input: {e}. Please try again \n")
        return False
    return True


def validate_answer(data):
    """
    Validates the users input for play again
    """
    try:
        if data != "yes" and data != "no":
            raise ValueError(
                f"You can only answer 'yes' or 'no'. You have answered: {data}")
    except ValueError as e:
        print(f"\n Invalid input: {e}. Please try again \n")
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
        self.board = [["." for y in range(self.board_size)]for x in range(self.board_size)]
        self.ships = []
        self.guesses = []
        self.score = 0

    def add_ships(self):
        """
        Add ships in the form of coordinates to a list
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

    def create_board(self):
        """
        Creates the battlefield and uppdates it each turn
        """
        print(f" {self.name}'s board \\\\ Score: {self.score}")
        column_num = [column for column in range(len(self.board))]
        print(" ¤", *column_num)
        row_num = 0
        for row in self.board:
            print("", row_num, *row)
            row_num += 1
        print()

    def validate_guess(self, data):
        """
        Validates the users input when guessing rows and columns
        """
        try:
            if not data.isdigit():
                raise ValueError(
                    f"You can only guess one whole number. You have entered: {data}")
            if int(data) > self.board_size - 1:
                raise ValueError(
                    f"Biggest number you can guess is {self.board_size - 1}. You guessed: {data}")
        except ValueError as e:
            print(f"\n Invalid input: {e}. Please try again\n")
            return False
        return True

    def check_guesses(self, data):
        """
        Checks if the users guess already have been guessed
        """
        try:
            if data in self.guesses:
                raise ValueError(
                    f"You have already guessed: {data}")
        except ValueError as e:
            print(f" Invalid input: {e}. Please try again\n")
            return False
        return True

    def calculate_hit(self, data):
        """
        Calculate if the guess is correct or not
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
        validate input, check guess and calculate hit or miss
        """
        while True:
            while True:
                print(self.ships)
                y = input(" Guess a row: ")
                if self.validate_guess(y):
                    break
            while True:
                x = input(" Guess a column: ")
                if self.validate_guess(x):
                    break
            guess = [int(y), int(x)]
            print(f" You have guessed coordinates: {y}, {x}\n")
            if self.check_guesses(guess):
                break
        if self.calculate_hit(guess):
            return True
        else:
            return False

    def computer_guess(self):
        """
        Generate a random coordinates and calls
        function to calculate hit or miss
        """
        while True:
            y = randint(0, self.board_size - 1)
            x = randint(0, self.board_size - 1)
            guess = [y, x]
            if guess not in self.guesses:
                break
        if self.calculate_hit(guess):
            return True
        else:
            return False

    def hit(self):
        """
        Prints out if someone hit and gives score
        """
        print(f" {self.name} hit!\n")
        self.score += 1

    def miss(self):
        """
        Prints out if someone missed
        """
        print(f" {self.name} missed!\n")

    def check_score(self):
        """
        Checks if someone sunk all ships
        """
        if self.score >= self.num_ships:
            print(f" {self.name} wins the game!\n")
            return True


def main():
    """
    Calls all functions to run the game loop
    """
    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")
    print("               _      ________   _________  __  _______  __________  ")
    print("              | | /| / / __/ /  / ___/ __ \/  |/  / __/ /_  __/ __ \ ")
    print("              | |/ |/ / _// /__/ /__/ /_/ / /|_/ / _/    / / / /_/ / ")
    print("              |__/|__/___/____/\___/\____/_/  /_/___/   /_/  \____/  ")
    print("                      __________  ___________   _  ______ ")
    print("                     /_  __/ __ \/ __/ __/ _ | / |/ / __/ ")
    print("                      / / / /_/ /\ \_\ \/ __ |/    /\ \   ")
    print("                     /_/  \____/___/___/_/ |_/_/|_/___/   ")
    print("    ___  ___ ______________   __________ _________    ________   __  _______  __")
    print("   / _ )/ _ /_  __/_  __/ /  / __/ __/ // /  _/ _ \  / ___/ _ | /  |/  / __/ / /")
    print("  / _  / __ |/ /   / / / /__/ _/_\ \/ _  // // ___/ / (_ / __ |/ /|_/ / _/  /_/ ")
    print(" /____/_/ |_/_/   /_/ /____/___/___/_//_/___/_/     \___/_/ |_/_/  /_/___/ (_)  ")
    print()
    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")
    while True:
        print(" \nDo you want to read the game rules?")
        read_gamerules = input(" Yes or No?: ").lower()
        if validate_answer(x):
            print()
            break
    if read_gamerules == "yes":
        print(" GAME RULES")
        print(" The object of Battleship is to try and sink all of the")
        print(" other player's ships before they sink all of yours.")
        print(" Try to hit them by entering coordinates on the board.")
        print(" When all your opponents ships have been hit, you win.")
        print(" @ = Your ships  X = Ships that been hit  / = Missed shots")
        print(" ")

    username = input(" Enter your username: ")
    print()

    while True:
        print(" Choose the size of the battlefield you want to play on")
        board_size = input(" Enter a number between 3-6: ")
        if validate_input(board_size, 3, 6):
            print()
            break

    while True:
        print(" Choose how manny battleships you want each player to have")
        num_ships = input(" Enter a number between 2-8: ")
        if validate_input(num_ships, 2, 8):
            print()
            break

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
            user.hit()
        else:
            user.miss()

        if user.computer_guess():
            computer.hit()
        else:
            computer.miss()

        user.create_board()
        computer.create_board()

        if user.check_score():
            print("--------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------")
            print("               __  ______  __  __  _      _______  __  __ ")
            print("               \ \/ / __ \/ / / / | | /| / /  _/ |/ / / / ")
            print("                \  / /_/ / /_/ /  | |/ |/ // //    / /_/  ")
            print("                /_/\____/\____/   |__/|__/___/_/|_/ (_)   ")
            print()
            print("--------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------")
            break
        elif computer.check_score():
            print("--------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------")
            print("               __  ______  __  __  __   ____  ________  __ ")
            print("               \ \/ / __ \/ / / / / /  / __ \/ __/ __/ / / ")
            print("                \  / /_/ / /_/ / / /__/ /_/ /\ \/ _/  /_/  ")
            print("                /_/\____/\____/ /____/\____/___/___/ (_)   ")
            print()
            print("--------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------")
            break
    
    while True:
        print(" \nDo you want to play again?")
        play_again = input(" Yes or No?: ").lower()
        if validate_answer(play_again):
            print()
            break

    if play_again == "yes":
        main()
    if play_again == "no":
        print("--------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------")
        print("                ________ _____   _  ____ __  __  ______  __  __ ")
        print("               /_  __/ // / _ | / |/ / //_/  \ \/ / __ \/ / / / ")
        print("                / / / _  / __ |/    / ,<      \  / /_/ / /_/ /  ")
        print("               /_/ /_//_/_/ |_/_/|_/_/|_|     /_/\____/\____/   ")
        print("            ________  ___    ___  __   _____  _______  _______  __ ")
        print("           / __/ __ \/ _ \  / _ \/ /  / _ \ \/ /  _/ |/ / ___/ / / ")
        print("          / _// /_/ / , _/ / ___/ /__/ __ |\  // //    / (_ / /_/  ")
        print("         /_/  \____/_/|_| /_/  /____/_/ |_|/_/___/_/|_/\___/ (_)   ")
        print()
        print("--------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------")

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
#computer could guess same guess