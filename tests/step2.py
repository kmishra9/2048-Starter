test = {
  'name': 'Random',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> for j in range(N):
          ...   for i in range(N):
          ...      starter.place_random(board);
          >>> assert utils.board_full(board), "N by N Board needs to be full after N*N calls to place_random";
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
      >>> board = utils.make_board(4)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> empty, two, four, eight = 0, 0, 0, 0;
          ... for row in board:
          ...     for piece in row:
          ...          if piece == '*':    empty += 1;
          ...          elif piece == '2':  two += 1;
          ...          elif piece == '4':  four += 1;
          ...          elif piece == '8':  eight += 1;
          ...          else:
          ...               continue;
          >>> assert empty == 0, "If board is full, there shouldn't be empty spaces";
          >>> assert two > four > eight, "Test failed. Ratio is improbable";
          >>> assert 75 >= two >= 45, "There don't seem to be enough 2's. Test failed.";         
          >>> assert 50 >= four >= 25, "There don't seem to be enough 4's. Test failed.";         
          >>> assert 10 >= eight >= 1, "There don't seem to be enough 8's. Test failed ... BUT retry 1 time";     
          >>> assert two + four + eight == 100, "There should only be 2s, 4s, and 8s placed by random";
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import starter_2048 as starter
      >>> import utils
      >>> N = 10
      >>> board = utils.make_board(N)
      >>> while not utils.board_full(board):
      ...   starter.place_random(board);
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
