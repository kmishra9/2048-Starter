"""
Project: "2048 in Python!"

Developed by: Kunal Mishra and Paradigm Shift
Autograder support, video introductions added by: Jesse Luo and Michael Tu

Developed for: Beginning students in Computer Science

To run: python3 starter_2048.py

Student Learning Outcomes:
    Various levels of comfort with:
        large projects and abstraction
        understanding, modeling, and maintaining existing code
        variables
        functional programming
        loops and conditionals
        multidimensional arrays/lists
        randomness and distributions
        CLI programming and terminal GUIs

Skill Level:
    assumed knowledge of language and concepts, but without mastery or even comfortability with them
    ~8-15 hours of lecture/lab/homework for a beginner at CS0 level coming into this project
    ~Calibrated at somewhat below the difficulty level of UC Berkeley's 61A project, Hog (less code synthesis but more interpretation required, given the students' backgrounds) 

Abstraction Reference Guide:

    main                - responsible for starting the game and directing control to each function, the tests, or quitting
        board           - a variable within main that contains the current board and is passed to most functions as an argument

    System Functions:
        get_key_press   - returns the user's key_press input as an ascii value
        clear           - clears the screen (should be called before each print_board call)
        pause           - a function used by the GUI to allow for a slight delay that is more visually appealing in placing the new piece


    Board Functions:
        make_board      - creates a new, empty square board of N x N dimension
        print_board     - prints out the state of the argument board
        board_full      - returns True if the board is full and False otherwise


    Logic:
        swipe_right     - simulates a right swipe on the argument board
        swipe_left      - simulates a left swipe on the argument board
        swipe_up        - simulates a upward swipe on the argument board
        swipe_down      - simulates a downward swipe on the argument board
        swap            - occurs when the spacebar is pressed and randomly switches two different numbers on the board
        swap_possible   - a helper function that returns True if a swap is possible and False otherwise


    Useful Helper Functions:
        get_piece       - gets the piece from the given board at the given (x,y) coordinates or returns None if the position is invalid
        place_piece     - places the given piece on the given board at the given (x,y) coordinates and returns True or returns False if the position is invalid
        place_random    - user implemented function which places a random 2 OR 4 OR 8 in an empty part of the board
        have_lost       - responsible for determining if the game has been lost yet (no moves remain)
        move_possible   - responsible for determining if a move is possible from a single position
        move            - responsible for moving a piece, at the given (x,y) coordinates in the given direction on the given board

"""

#End of first section
############################################################################################################
################################## DO NOT CHANGE ANYTHING ABOVE THIS LINE ##################################    - Section 2 -
############################################################################################################


#Start of Step 0 ###########################################################################################

def main():

    #Creating my new 4x4 board
    board = ">>>>>>>>>>YOUR CODE HERE 1<<<<<<<<<<"

    #Getting the game started with a single piece on the board
    place_random(board)
    print_board(board)

    #Runs the game loop until the user quits or the game is lost
    while True:

        #Gets the key pressed and stores it in the key variable
        key = ">>>>>>>>>>YOUR CODE HERE 2<<<<<<<<<<"

        #Quit case ('q')
        if ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            print("Game Finished!");
            quit()

        #Up arrow
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            "YOUR CODE HERE (1 line) <<<<<"

        #Down arrow
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            "YOUR CODE HERE (1 line) <<<<<"

        #Right arrow
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            "YOUR CODE HERE (1 line) <<<<<"

        #Left arrow
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            "YOUR CODE HERE (1 line) <<<<<"

        #Space bar
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            swap(board);

        #Check to see if I've lost at the end of the game or not
        if ">>>>>>>>>>YOUR CODE HERE 4<<<<<<<<<<":
            
            print("You lost! Would you like to play again? (y/n)");
            if (input() == 'y'):
                main();
            else:
                quit()

#End of Step 0 #############################################################################################



#Start of Step 1 ###########################################################################################

def get_piece(x, y, board):
    """
    Utility function that gets the piece at a given (x,y) coordinate on the given board
    Returns the piece if the request was valid and None if the request was not valid
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg board: board - the board you wish to get the piece from
    """
    
    #Ensure that x and y are both integers (use assert)
    ">>>>>>>>>>YOUR CODE HERE 5<<<<<<<<<<"

    #What does this do?
    N = len(board)

    #Checking that the (x,y) coordinates given are valid for the N x N board
    ">>>>>>>>>>YOUR CODE HERE 6<<<<<<<<<<"

    #Getting the piece on the board
    return board[y][x]


def place_piece(piece, x, y, board):
    """
    Utility function that places the piece at a given (x,y) coordinate on the given board if possible
    Will overwrite the current value at (x,y), no matter what that piece is
    Returns True if the piece is placed successfully and False otherwise
    Arg piece: string - represents a piece on the board ('*' is an empty piece, '2' '8' etc. represent filled spots)
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg board: board - the board you wish to place the piece on
    """
    
    #Ensure that x and y are both integers (use assert)
    ">>>>>>>>>>YOUR CODE HERE 7<<<<<<<<<<"

    #What are the dimensions of the board?
    ">>>>>>>>>>YOUR CODE HERE 8<<<<<<<<<<"

    #Checking that the (x,y) coordinates given are valid for the board
    ">>>>>>>>>>YOUR CODE HERE 9<<<<<<<<<<"

    #Placing the piece on the board
    board[y][x] = piece
    return True

#End of Step 1 #############################################################################################


#Start of Step 2 ###########################################################################################

def place_random(board):
    """
    Helper function which is necessary for the game to continue playing
    Returns True if a piece is placed and False if the board is full
    Places a 2 (60%) or 4 (37%) or 8 (3%) randomly on the board in an empty space
    Arg board: board - the board you wish to place the piece on
    """
    
    #Delete this return statement AND comment before beginning Step 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    return;

    #Check if the board is full and return False if it is
    ">>>>>>>>>>YOUR CODE HERE 10<<<<<<<<<<"

    #random.random() generates a random decimal between [0, 1) ... Multiplying by 100 generates a number between [0, 100)
    generated = random.random() * 100;

    #Assign to_place according to my generated random number

    if generated < -1:                              #YOUR CODE HERE (replace -1) <<<<<
        to_place = "2"

    elif generated < -1 and generated >= -1:        #YOUR CODE HERE (replace -1) <<<<<
        to_place = "4"

    else:
        #What should to_place be if it's not a 2 or 4?
        to_place = ">>>>>>>>>>YOUR CODE HERE 11<<<<<<<<<<"


    #Variable keeps track of whether a randomly generated empty spot has been found yet
    found = False
    N = len(board)

    while not found:
        #Generate a random (x,y) coordinate that we can try to put our new value in at
        #How did we "generate" a random number earlier? (hint: x and y should be between [0, N) )
        random_y = ">>>>>>>>>>YOUR CODE HERE 12<<<<<<<<<<"
        random_x = ">>>>>>>>>>YOUR CODE HERE 13<<<<<<<<<<"

        #Think about why this is necessary ( hint: changes 3.4 (float) -> 3 (int) )
        random_y = int(random_y)
        random_x = int(random_x)

        #If the randomly generated coordinates are empty, we have found a spot to place our random piece
        found = get_piece(random_x, random_y, board) == '*'

    #Place the piece at the randomly generated (x,y) coordinate
    ">>>>>>>>>>YOUR CODE HERE 14<<<<<<<<<<"

    return True

#End of Step 2 #############################################################################################


#Start of Step 3 ###########################################################################################

def have_lost(board):
    """
    Helper function which checks at the end of each turn if the game has been lost
    Returns True if the board is full and no possible turns exist and False otherwise
    Arg board: board - the board you wish to check for a losing state
    """

    #Delete this return statement AND comment before beginning Step 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    return False


    N = len(board)

    #Check every (x,y) position on the board to see if a move is possible
    for y in range(N):
        for x in range(N):
            ">>>>>>>>>>YOUR CODE HERE 15<<<<<<<<<< (1 or 2 lines)"

    return True

#End of Step 3 #############################################################################################


#Start of Step 4 ###########################################################################################

def end_move(board):
    """
    Prints the board after a swipe, pauses for .2 seconds, places a new random piece and prints the new state of the board
    Arg board: board - the board you're finishing a move on
    """
    
    #Print the board
    ">>>>>>>>>>YOUR CODE HERE 16<<<<<<<<<< (2 lines)"

    #Pause for .2 seconds
    ">>>>>>>>>>YOUR CODE HERE 17<<<<<<<<<<"

    #Place a random piece on the board at a random (x,y) position
    ">>>>>>>>>>YOUR CODE HERE 18<<<<<<<<<<"

    #Print the board again
    ">>>>>>>>>>YOUR CODE HERE 19<<<<<<<<<< (2 lines)"

#End of Step 4 #############################################################################################



#Start of Step 5 ###########################################################################################

def swipe_left(board):
    """
    YOUR COMMENT HERE (WHAT DOES THIS FUNCTION DO?)
    Arg board: board - (WHAT IS A BOARD ARGUMENT?)
    """
    
    #YOUR COMMENT HERE
    action_taken = False

    #YOUR COMMENT HERE
    N = len(board)

    #YOUR COMMENT HERE
    for y in range(N):
        for x in range(N):
            #YOUR COMMENT HERE
            piece_at_xy = get_piece(x, y, board)
            left_adjacent = get_piece(x-1, y, board)

            #YOUR COMMENT HERE
            if piece_at_xy == '*':
                continue

            #YOUR COMMENT HERE
            if left_adjacent == None:
                continue

            #YOUR COMMENT HERE
            action_taken = move(x, y, "left", board) or action_taken


    #YOUR COMMENT HERE
    if action_taken:
        end_move(board)

def swipe_right(board):
    action_taken = False

    N = len(board)

    for y in range(N):
        for x in range(N):
            #Don't worry about why this is done (is not needed for up or left)
            x = N-1-x

            piece_at_xy = get_piece(x, y, board)
            right_adjacent = get_piece(x+1, y, board)

            if piece_at_xy == '*':
                continue

            if right_adjacent == None:
                continue

            action_taken = move(x, y, "right", board) or action_taken


    if action_taken:
        end_move(board)

def swipe_up(board):
    action_taken = False

    N = len(board)

    for y in range(N):
        for x in range(N):
            piece_at_xy = get_piece(x, y, board)
            up_adjacent = get_piece(x, y-1, board)

            if piece_at_xy == '*':
                continue

            if up_adjacent == None:
                continue

            action_taken = move(x, y, "up", board) or action_taken


    if action_taken:
        end_move(board)

def swipe_down(board):
    action_taken = False

    N = len(board)

    for y in range(N):
        #Don't worry about why this is done (is not needed for up or left)
        y = N-1-y

        for x in range(N):

            piece_at_xy = get_piece(x, y, board)
            down_adjacent = get_piece(x, y+1, board)

            if piece_at_xy == '*':
                continue

            if down_adjacent == None:
                continue

            action_taken = move(x, y, "down", board) or action_taken


    if action_taken:
        end_move(board)

#End of Step 5 #############################################################################################



#End of second section
############################################################################################################
######################## Optional Challenge -- ATTEMPT AFTER FINISHING PROJECT #############################    - Section 3 -
############################################################################################################

def swap(board):
    """
    Optional Challenge: an addition to our game that adds some randomness and chance!
    Randomly swaps 2 different numbers on the board and returns True if a swap is performed and False otherwise
    Purpose: allows you to evade losing for a little while longer (if the swap is useful)
    
    Note: have_lost does not take into account possible swaps that can "save the day". This is expected behavior.
    """
    
    print("Not implemented yet!")
    return False


def swap_possible(board):
    """
    Optional Challenge: helper function for swap
    Returns True if a swap is possible on the given board and False otherwise
    """
    
    print("Not implemented yet!")
    return False






#End of third section
############################################################################################################
################################## DO NOT CHANGE ANYTHING BELOW THIS LINE ##################################   - Section 4 -
############################################################################################################

try:
    from utils import *
except ImportError:
    from _2048.utils import *

if __name__ == "__main__":
    #Only want to see the game board at the top
    clear();
    
    #Starting the game
    main()



#End of fourth section
#End of starter_2048.py