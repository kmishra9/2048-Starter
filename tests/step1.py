test = {
  'name': 'Pieces',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert starter.get_piece(-1, -1, board) == None, "Not returning None properly during an invalid get or misunderstanding of spec w/ invalid inputs";
          >>> starter.get_piece(N, N, board) == None, "Not returning False properly during an invalid place or misunderstanding of spec w/ invalid inputs";
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
          >>> assert not starter.place_piece('*', -1, -1, board),"Not returning False properly during an invalid place or misunderstanding of spec w/ invalid inputs";
          >>> assert not starter.place_piece('*', N, N, board), "Not returning False properly during an invalid place or misunderstanding of spec w/ invalid inputs";
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
          >>> to_place = '0'
          >>> for y in range(N):
          ...    for x in range(N):
          ...        starter.place_piece(to_place, x, y, board);
          ...        if to_place != starter.get_piece(x, y, board):
          ...          raise AssertionError("Placed a piece at {} {} but did not get same piece back".format(x, y))
          ...        to_place = chr(ord(to_place) + 1)
          >>> # The board needs to be full after placing these pieces
          >>> assert utils.board_full(board), "N by N Board needs to be full after N*N calls to place_piece at different (x,y) coordinates";
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
          >>> # Checks against data abstraction violations
          >>> assert starter.place_piece('7', 7, 7, board), "Abstraction violation. Hard-coded bounds in place_piece. Use the board's dimensions";
          >>> assert not starter.get_piece(7, 7, board) == None, "Abstraction violation. Hard-coded bounds in get_piece. Use the board's dimensions";
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
    }
  ]
}
