test = {
  'name': 'SwapPossible',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert not starter.swap_possible(board), "An empty board cannot perform swap"
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
          >>> starter.place_piece('0', 0, 0, board)
          True
          >>> assert not starter.swap_possible(board), "A board with 1 piece cannot perform swap"
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
          >>> starter.place_piece('0', 1, 1, board)
          True
          >>> assert not starter.swap_possible(board), "A board with 2 identical pieces cannot perform swap"
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
          >>> starter.place_piece('0', 1, 1, board)
          True
          >>> starter.place_piece('1', 0, 1, board)
          True
          >>> assert starter.swap_possible(board), "A board with 2 unique pieces should be able to perform swap";
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import starter_2048 as starter
      >>> import utils
      >>> board = utils.make_board(4)
      >>> calls = []
      >>> def test_print(message):
      ...     calls.append('print') # do not actually print
      >>> starter.print = test_print
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
