test = {
  'name': 'Swap',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert not starter.swap(board), "An empty board should not perform swap"
          >>> calls
          ['print']
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
      >>> def test_print(message):
      ...     calls.append('print') # do not actually print
      >>> starter.print = test_print
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> starter.place_piece('2', 0, 0, board)
          True
          >>> assert not starter.swap_possible(board), "A board with 1 piece cannot perform swap"
          >>> calls
          ['print']
          >>> starter.place_piece('2', 1, 1, board)
          True
          >>> assert not starter.swap_possible(board), "A board with 2 identical pieces cannot perform swap"
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
      >>> def test_print(message):
      ...     calls.append('print') # do not actually print
      >>> starter.print = test_print
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> board = utils.make_board(4);
          >>> starter.place_piece('2', 0, 0, board)
          True
          >>> starter.place_piece('4', 1, 0, board)
          True
          >>> assert starter.swap(board), "A board with 2 unique pieces should perform swap"
          >>> assert starter.get_piece(0,0,board)=='4', "The pieces are not correctly swapped. check your swap functions again."
          >>> assert starter.get_piece(1,0,board)=='2', "The pieces are not correctly swapped. check your swap functions again."
          >>> assert starter.get_piece(0,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap functions again."
          >>> assert starter.get_piece(1,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap functions again."
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
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> board = utils.make_board(4);
          >>> starter.place_piece('2', 0, 0, board)
          True
          >>> starter.place_piece('4', 1, 1, board)
          True
          >>> assert starter.swap(board), "A board with 2 unique pieces should perform swap"
          >>> assert starter.get_piece(0,0,board)=='4', "The pieces are not correctly swapped. \nYou shoudn't swap randomly, not staticly. \ncheck your swap functions again."
          >>> assert starter.get_piece(1,1,board)=='2', "The pieces are not correctly swapped. \nYou shoudn't swap randomly, not staticly. \ncheck your swap functions again."
          >>> assert starter.get_piece(0,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap functions again."
          >>> assert starter.get_piece(1,0,board)=='*', "There shoudn't be pieces added to empty places. check your swap functions again."
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import starter_2048 as starter
      >>> import utils
      >>> board = utils.make_board(10)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> board = utils.make_board(4);
          >>> entered = False
          >>> starter.place_piece('2', 0, 0, board)
          True
          >>> starter.place_piece('4', 0, 1, board)
          True
          >>> starter.place_piece('8', 1, 0, board)
          True
          >>> assert starter.swap(board), "A board with 3 unique pieces should perform swap"
          >>> if starter.get_piece(0,0,board) =='2':
          ...    entered = True
          ...    assert starter.get_piece(0,1,board)=='8', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
          ...    assert starter.get_piece(1,0,board)=='4', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
          ...    assert starter.get_piece(1,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap function again.";
          >>> if starter.get_piece(0,0,board) =='4':
          ...    entered = True
          ...    assert starter.get_piece(0,1,board)=='2', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
          ...    assert starter.get_piece(1,0,board)=='8', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
          ...    assert starter.get_piece(1,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap function again.";
          >>> if starter.get_piece(0,0,board) =='8':
          ...    entered = True
          ...    assert starter.get_piece(0,1,board)=='4', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
          ...    assert starter.get_piece(1,0,board)=='2', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
          ...    assert starter.get_piece(1,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap function again.";
          >>> if not entered:
          ...    assert False,"Improper swaps occurred. Check your swap function again";
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import starter_2048 as starter
      >>> import utils
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
