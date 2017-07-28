test = {
  'name': 'SetupAndMain',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def test_getch():
          ...     try:
          ...         import getch
          ...     except ImportError:
          ...         try:
          ...             subprocess.check_call(["sudo", "easy_install3", "getch"])
          ...         except subprocess.CalledProcessError:
          ...             os.system("python3 -m pip install getch")
          >>> def test_termcolor():
          ...     try:
          ...         import termcolor
          ...     except ImportError:
          ...         try:
          ...             subprocess.check_call(["sudo", "easy_install3", "termcolor"])
          ...         except subprocess.CalledProcessError:
          ...             os.system("python3 -m pip install termcolor")
          >>> test_getch()
          >>> test_termcolor()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> starter.main()
          >>> assert calls[0] == 'make_board', 'Make sure the first thing you do is create a new 4x4 board.'
          >>> assert calls[1] == 'get_key_press', 'Make sure you are getting the current key pressed.'
          >>> assert calls[2] == 'swipe_up', 'Make sure you have the correct associated key press value for the up arrow, and that you call the correct swipe function.'
          >>> assert calls[4] == 'swipe_down', 'Make sure you have the correct associated key press value for the down arrow, and that you call the correct swipe function.'
          >>> assert calls[6] == 'swipe_right', 'Make sure you have the correct associated key press value for the right arrow, and that you call the correct swipe function.'
          >>> assert calls[8] == 'swipe_left', 'Make sure you have the correct associated key press value for the left arrow, and that you call the correct swipe function.'
          >>> assert calls[10] == 'swap', 'Make sure you have the correct associated key press value for the space bar.'
          >>> assert calls[13] == 'quit', 'Make sure you have the correct associated key press value for the letter q.'
          >>> calls
          ['make_board', 'get_key_press', 'swipe_up', 'get_key_press', 'swipe_down', 'get_key_press', 'swipe_right', 'get_key_press', 'swipe_left', 'get_key_press', 'swap', 'get_key_press', 'print', 'quit']
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import os as os
      >>> import subprocess as subprocess
      >>> import starter_2048 as starter
      >>> import sys as sys
      >>> import utils
      >>> index = -1
      >>> calls = []
      >>> def get_key_press():
      ...     global index
      ...     if index == 5:
      ...        sys.exit()
      ...     calls.append('get_key_press')
      ...     inputs = [65, 66, 67, 68, 32, 113]
      ...     index += 1
      ...     return inputs[index]
      >>> def board_full(board):
      ...     calls.append('board_full')
      >>> starter.get_key_press = get_key_press
      >>> starter.board_full = board_full
      >>> def swipe_up(board):
      ...     calls.append('swipe_up')
      >>> def swipe_down(board):
      ...     calls.append('swipe_down')
      >>> def swipe_right(board):
      ...     calls.append('swipe_right')
      >>> def swipe_left(board):
      ...     calls.append('swipe_left')
      >>> def make_board(N):
      ...     calls.append('make_board')
      >>> def swap(board):
      ...     calls.append('swap')
      >>> def print(msg):
      ...     calls.append('print')
      >>> def quit():
      ...     calls.append('quit')
      >>> def end_move(board):
      ...     return 1
      >>> def place_random(board):
      ...     return 1
      >>> def print_board(board):
      ...     return 1
      >>> starter.swipe_up = swipe_up
      >>> starter.swipe_down = swipe_down
      >>> starter.swipe_right = swipe_right
      >>> starter.swipe_left = swipe_left
      >>> starter.make_board = make_board
      >>> starter.swap = swap
      >>> starter.print = print
      >>> starter.quit = quit
      >>> starter.end_move = end_move
      >>> starter.place_random = place_random
      >>> starter.print_board = print_board
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
