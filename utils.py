#2048 Utils

file_name = "starter_2048"
try:
    starter = __import__(file_name, fromlist=["something"])
except ImportError:
    starter = __import__("_2048." + file_name, fromlist=["something"])

#Importing non-standard libraries
try:
    import getch
except ImportError:
    getch = None
try:
    import termcolor
except ImportError:
    termcolor = None
try:
    from tkinter import *
    #Assigned to None because import was successful but $DISPLAY may not be set
    gui, GUI_runnable, = None, None
except ImportError:
    gui, GUI_runnable, = False, False
    
#Importing standard libraries
import random
import os
import time


############################################################################################################
################################## DO NOT CHANGE ANYTHING ABOVE THIS LINE ##################################    - Section 2 -
############################################################################################################


def get_key_press():
    """Utility function that gets which key was pressed and translates it into its character ascii value - takes no arguments"""
    return ord(getch.getch());


def clear():
    """Utility function that clears the terminal GUI's screen - takes no arguments"""
    try:
        try:
            #For Macs and Linux
            os.system('clear');
        except:
            #For Windows            REPORTED BUG: Sometimes does not work on 64 bit Windows
            os.system('cls');
    except:
        #If nothing else works, a hacky, non optimal solution
        for i in range(50): print("")
    

def pause(seconds):
    """
    Utility function that pauses for the given amount of time
    Arg seconds: a float or integer - number of seconds to pause for
    """
    time.sleep(seconds);


def make_board(N):
    """
    Utility function that returns a new N x N empty board (empty spaces represented by '*')
    Arg N: integer - board dimensions - must be greater than or equal to 1
    """
    assert N >= 1, "Invalid board dimension";
    assert type(N) == int, "N must be an integer";
    return [["*" for x in range(N)] for x in range(N)];


def print_board(board):
    """
    Utility function that prints out the state of the board
    Arg board: board - the board you want to print
    """
    
    colors = {
        '*': None,
        '2': 'red',
        '4': 'green',
        '8': 'yellow',
        '16': 'blue',
        '32': 'magenta',
        '64': 'cyan',
        '128': 'grey',
        '256': 'white',
        '512': 'green',
        '1024': 'red',
        '2048': 'blue',
        '4096': 'magenta'
    };
    header = "Use the arrows keys to play 2048! Press q to quit";
    print(header);
    N = len(board);
    vertical_edge = "";
    for i in range(N+2):
        vertical_edge += "-\t";
    print(vertical_edge);
    for y in range(N):
        row = "";
        for x in board[y]:
            
            #Handling installation fail (no colors printed)
            if termcolor is not None:
                row += termcolor.colored(x, colors[x]);
            else:
                row += x
            
            row += "\t";
        print("|\t" + row + "|");
        if y is not N-1: print("")
    print(vertical_edge);
    
    
    if GUI_runnable:
        gui.update_grid(board)
        gui.update()


def board_full(board):
    """
    Utility function that returns True if the given board is full and False otherwise
    Arg board: board - the board you want to check
    """
    
    for row in board:
        for piece in row:
            if piece == '*':  return False;

    return True;


def move_possible(x, y, board):
    """
    Utility function that, given a position, will return True if a move is possible at that (x,y) position and False otherwise
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg board: board - the board you wish to check if a move is possible on
    """
    
    piece_at_xy = starter.get_piece(x, y, board);
    if piece_at_xy == None:
        return False;
    elif piece_at_xy == '*':    #An empty space means a move is always possible
        return True;

    return (
           piece_at_xy == starter.get_piece(x+1, y, board) or
           piece_at_xy == starter.get_piece(x-1, y, board) or
           piece_at_xy == starter.get_piece(x, y+1, board) or
           piece_at_xy == starter.get_piece(x, y-1, board)
           );


def move(x, y, direction, board):
    """
    Utility function that moves the piece at the position (x,y) on the given board the given direction
    Returns whether an action was actually executed or not
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg direction: string - "left", "right", "up", "down"
    Arg board: board - the board you wish to make a move on
    """
    
    piece_at_xy = starter.get_piece(x, y, board);           #Getting necessary pieces
    
    assert piece_at_xy != '*', "Error in swipe logic";      #Logical debug case
    valid_direction = (direction == "left"  or
                       direction == "right" or
                       direction == "up"    or
                       direction == "down");
    assert valid_direction, "Invalid direction passed in";  #Logical debug case
    
    #The new x and y for the current piece (adjacent's current position) are stored alongside adjacent (fewer ifs + redundant code)
    if   direction == "left":   adjacent = (starter.get_piece(x-1, y, board), x-1, y);
    elif direction == "right":  adjacent = (starter.get_piece(x+1, y, board), x+1, y);
    elif direction == "up":     adjacent = (starter.get_piece(x, y-1, board), x, y-1);
    elif direction == "down":   adjacent = (starter.get_piece(x, y+1, board), x, y+1);

    if adjacent[0] == None:                                             #Edge of the board case (no action taken)
        return False;

    elif piece_at_xy != adjacent[0] and adjacent[0] != '*':             #Can't combine two numbers case (no action taken)
        return False;

    elif adjacent[0] == '*':                                            #Empty spot adjacent case (recursive movement in direction)
        starter.place_piece('*', x, y, board);
        starter.place_piece(piece_at_xy, adjacent[1], adjacent[2], board);
        move(adjacent[1], adjacent[2], direction, board);
        return True;

    elif piece_at_xy == adjacent[0]:                                    #Adjacent same numbers case (combine them)
        starter.place_piece('*', x, y, board);
        starter.place_piece(str(int(adjacent[0]) * 2), adjacent[1], adjacent[2], board);
        move(adjacent[1], adjacent[2], direction, board);
        return True;

    else:
        #Logical debug case
        assert False, "No way you should be in here. Error in move logic";

    return False;


#End of utils
############################################################################################################
################################## DO NOT CHANGE ANYTHING BELOW THIS LINE ##################################
############################################################################################################






#You can minimize this class -- it handles the GUI and understanding it, examining it, or using it is not required to complete the project
class gui_2048(Frame):
    """
    The class gui_2048 is a tkinter GUI application that will run along with the main console
    2048 application. The class is initialized along in the main() function and is updated using
    update_grid in the while loop in the main() function.
    """

    def __init__(self,master = None):
        Frame.__init__(self,master)

        #Background and font colors for each number upto 8192.
        self.background_color = {'2':'#EBE1D7','4':'#ECE0CA','8':'#F4B176','16':'#F7975C','32':'#FA7961','64':'#F2613C','128':'#EBE899','256':'#F0D069','512':'#EBE544','1024':'#EAC80D','2048':'#F4FC08','4096':'#A4FC0D','8192':'#FC0D64'}
        self.foreground_color = {'2':'#857865','4':'#857865','8':'#FDF5E9','16':'#FDF5E9','32':'#FDF5E9','64':'#FDF5E9','128':'#FDF5E9','256':'#FDF5E9','512':'#FDF5E9','1024':'#FDF5E9','2048':'#FDF5E9','4096':'#FDF5E9','8192':'#FDF5E9'}

        #support window resizing
        self.grid(sticky = N+S+E+W)

        #Adding weights to each column in the row so they are resized correctly
        #6/9/2016 top = self.winfo_toplevel()
        #6/9/2016 top.rowconfigure(0,weight = 1)
        #6/9/2016 top.columnconfigure(0,weight = 1)
        #6/9/2016 self.rowconfigure(0,weight = 1)
        #6/9/2016 self.columnconfigure(0,weight = 1)

        #Adding the size of the board to create. This may be changed anytime to get a different sized board
        self.board_size = 4

        #matrix_numbers is a list of frames (N x N frames) where N is board_size
        self.matrix_numbers = list()

        #initializing the GUI without any numbers (Starting point)
        self.create_grid(self.board_size)


    def create_grid(self,board_size):

        #creating one frame for the whole window
        f = Frame(self,width = 500,height = 500, bg = '#BBADA0',borderwidth = 5)

        #support window resizing each frame
        f.grid(sticky = N+S+E+W)

        #Adding weights to support resizing each frame
        #6/9/2016 for m in range(int(board_size)):
        #6/9/2016     f.rowconfigure(m,weight = 1)
        #6/9/2016     f.columnconfigure(m,weight = 1)

        #Adding frames inside the main frame f for each grid point along with its background and font color
        for i in range(int(board_size)):
            label_row = []
            for j in range(int(board_size)):
                frames = Frame(f, bg = '#EEE4DA',height = 150, width = 150,relief = SUNKEN)
                frames.grid(row=i, column=j,padx = 5, pady = 5,sticky = N+S+E+W)
                each_label = Label(f, text = "",background = "#EEE4DA",font = ("Arial",55),justify = CENTER)
                each_label.grid(row=i, column=j,padx = 5, pady = 5, sticky = N+S+E+W)
                label_row.append(each_label)
            self.matrix_numbers.append(label_row)

    #update function that updates the number matrix after every loop in the main function
    def update_grid(self,board):
        assert len(board) == self.board_size
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == '*':
                    self.matrix_numbers[x][y].configure(text = '',bg = '#EEE4DA')
                else:
                    self.matrix_numbers[x][y].configure(text = str(board[x][y]),bg = self.background_color[board[x][y]
                    ],fg = self.foreground_color[board[x][y]])

#You can minimize these classes -- they handle getting user input for a key and understanding it, examining it, or using it is not required to complete this project
class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()
            
    def getch(self):    return self()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

#Check if the environment is GUI-runnable (no import error, GUI is able to initialize) OR if only CLI is supported
if GUI_runnable == None:
    
    try:
        root = Tk()
        gui = gui_2048(root)
        GUI_runnable = True 
    except:
        GUI_runnable = False
    
if getch == None:
    getch = _Getch()


#End of utils.py
