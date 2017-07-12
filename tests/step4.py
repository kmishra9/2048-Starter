test = {
  'name': 'End_move',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> starter.end_move(board)
          >>> assert utils.made_move(board), "A piece should be placed at random."
          >>> assert utils.num_pieces(board) == 1, "Only one piece should be placed each time."
          >>> assert calls[0] == 'clear', "Make sure you always clear the screen before printing the board."
          >>> assert calls[1] == 'print_board', "Make sure you print the board after clearing the screen."
          >>> assert calls[2] == 'pause0.2', "Make sure you pause for .2 seconds before placing a piece!"
          >>> assert calls[3] == 'clear', "After placing a piece, make sure you clear the board again."
          >>> assert calls[4] == 'print_board', "After placing a piece and clearing the screen, make sure you print the board again."
          >>> calls
          ['clear', 'print_board', 'pause0.2', 'clear', 'print_board']
          >>> starter.end_move(board);
          >>> assert utils.made_move(board), "A piece should be placed at random."
          >>> assert utils.num_pieces(board) == 2, "Only one piece should be placed each time."
          >>> starter.end_move(board);
          >>> assert utils.made_move(board), "A piece should be placed at random."
          >>> assert utils.num_pieces(board) == 3, "Only one piece should be placed each time."
          >>> len(calls)
          15
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import starter_2048 as starter
      >>> import utils
      >>> N = 4
      >>> board = utils.make_board(N)
      >>> calls = []
      >>> def test_clear():
      ...     calls.append('clear') # do not actually clear
      >>> def test_print_board(board):
      ...     calls.append('print_board') # do not actually print
      >>> def test_pause(quantity):
      ...     calls.append('pause{}'.format(quantity)) # do not actually pause
      >>> starter.clear = test_clear
      >>> starter.print_board = test_print_board
      >>> starter.pause = test_pause
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
