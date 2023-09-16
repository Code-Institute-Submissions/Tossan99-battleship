# TOSSANS BATTLESHIP GAME


![Welcome page](readme-images/welcome.JPG)

Visit [Tossans battleship game](https://tossans-battleships-game-b3734a738de1.herokuapp.com/)

---

## CONTENTS 


---
## Intoduction
Tossans battleship game is a Python terminal game. It runs on a mock terminal deployed to Heroku. 

It is based on the classic board game “battleships”. A guessing game for two players that is played on ruled grids on which each player place their ships on. The locations of the ships are concealed for the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

## The User Experience

### Site Purpose
* To offer a simple and fun game to the users.

### User Goals
As a user i want:

* To have fun while being challenged.

* To learn and understand the game.

* The game to offer replay value with alot of customizable options.

* To easily choose available options and have a clear response to my actions.

## Project Goals 
As the developer I want:

* Users to meet their goals above.

* The game to be functional and without errors.

## Design

### Flow Chart

[Figma](https://www.figma.com/) was used to plan the flow of the program.

![Flow chart](readme-images/flowchart.JPG)

### Titles and Headings
* All titles and headings was created with [Fancy Text](https://www.fancytextpro.com/BigTextGenerator).

---

## Features

### Welcome Page 
![Welcome page](readme-images/welcome.JPG)

When the game is ran it immediately displays this welcome message and asks for input.

### Game Rules
![Game Rules](readme-images/rules.JPG)

In this section the game asks if you want to read the game rules. If you enter "Yes" the rules will be display for you. 

This input is checked with a function that validates in the input. If the user give input that isn't asked for an error message will be printed.

### Username
![Username](readme-images/username.JPG)

In this section the game asks for a username. There are no validation checks for this input so the user can be as creative as they want.


### Customizable Board
![Customizable Board](readme-images/setup1.JPG)

In this section the game asks for input to set up the board. The user can choose to have a board from 3x3 to 6x6 and 2 to 8 battleships. 

This input is checked with a function that validates in the input. If the user give input that isn't asked for an error message will be printed.

### Battlefield
![Battlefield](readme-images/board.JPG)

In this section the battlefield is displayed to the user. The board displays the users username, score, ships and misses/hits from the player and computer.

### Coordinates Input
![Coordinates Input](readme-images/guess.JPG)

In this section the game asks for the user to guess a coordinate to take a shot at the opponents board. This is done by entering a number for row and column. 

This input is checked with a function that validates in the input. If the user give input that isn't asked for an error message will be printed.

### Win and Lose
![Win](readme-images/win.JPG)
![Lose](readme-images/lose.JPG)

This section is displayed when all of someones ships have been hit.

### Replay
![Replay](readme-images/playagain.JPG)

This section asks the user if they want to play again. If the user answers "Yes" the game will run again and if the user answers "no" it will exit the game and display the "Thank you for playing" message. 

This input is checked with a function that validates in the input. If the user give input that isn't asked for an error message will be printed.

![Thank You](readme-images/thankyou.JPG)

### Favicon
The game have a simple favicon of a battleship
![Favicon](favicon.png)

### Features Left to Implement
* Different sizes for ships

At the moment all ships consists of 1x1 squares. I would like to fin a way to make ships 2x1, 3x1, 2x2 and so on...

* Highscore

I would like to link a google sheet to the game and store user data for a highscore page that can be viewed in the game

* Customizable option for both user and computer

In the games current state the user can only customize both boards at the same time. I would like to add the option to customize the boards individually.

---

## Bugs

---

## Technologies Used
* Languages: 
    * Python.
* Libraries:
    * random 
        - Used to select a random word.
    * os
        - Used for its `clear` tool, to clear the terminal window.
* Others:
    * Github
        - To store the repository for submission.
    * Heroku
        - To deploy a live version of the terminal.
    * Lucid 
        - To make a flowchart for preparation to project.
    * Fancy text pro
        - To make word art. 

## Deployment & Local Development

### Deployment

The site is deployed using GitHub Pages. Visit the deployed site [here](https://tossan99.github.io/flag-quiz2/). To deploy using GitHub pages:

1. login or Sign Up to GitHub.
2. open the project repository.
3. Click on "Settings" on the navigation bar under the repository title.
4. Click on "Pages" in the left hand navigation panel.
5. Under "Source", choose which branch to deploy. This should be Main for newer repositories (older repositories may still use Master).
6. Choose which folder to deploy from, usually "/root".
7. Click "Save", then wait for it to be deployed. It can take some time for the page to be fully deployed.
8. Your URL will be displayed above "Source".

---

## Testing

Go to this separate [testing page](#) to read about testing

### Validator testing

- Python3
  - All html pages have passed through the [Python3 validator]() 

### Unfixed Bugs

---

## Credits

### Code Used

### Content

### Media
