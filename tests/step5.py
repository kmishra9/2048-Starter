test = {
  'name': 'Swipe',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': '3ec7e0142088997708592f1e52d5434a',
          'choices': [
            'Keeps track of whether swiping left actually did anything or not.',
            'Gets the piece at a given x and y position on the board.',
            'Places a piece at a given x and y position on the board.',
            'Checks if, at the end of the turn, the game has been lost.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the function swipe_left do?'
        },
        {
          'answer': '7e1584bfcfbfc411f626a37c0b3930e2',
          'choices': [
            'If a piece was moved or not.',
            'If this function was called or not.',
            'If a piece was placed on the board.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': True,
          'question': "'What does the variable action_taken represent?'"
        },
        {
          'answer': '5f75454988a92adff154ff457d884a3d',
          'choices': [
            'The number of squares along one side of the board.',
            'If the game has ended or not.',
            'Nothing, since we never assign it to anything.',
            'Number of total squares on the board.'
          ],
          'hidden': False,
          'locked': True,
          'question': "'What does the variable N represent?'"
        },
        {
          'answer': 'fd055b3b74081851cfbe47fdf4f9df89',
          'choices': [
            'Iteration through each column and row of the board.',
            'Iteration only through each column of the board.',
            'Iteration only through each row of the board.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the "for y in range(N) and for x in range(N) represent"?'
        },
        {
          'answer': '8fe0a22a1002c3905013752b65958c84',
          'choices': [
            'They are an adjacent pair of pieces.',
            'They are 2 squares on the board.',
            'They are 2 random pieces on the board.',
            'There is no relationship between them.'
          ],
          'hidden': False,
          'locked': True,
          'question': "'What are piece_at_xy and left_adjacent?'"
        },
        {
          'answer': '52b1ebf73f00d2648a3fee0da47efc1c',
          'choices': [
            'I cannot move an empty piece, so just move on.',
            'I can move an empty piece, so I move it.',
            'I place a new piece at the location of piece_at_xy.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': True,
          'question': "What happens if the piece_at_xy is an '*'?"
        },
        {
          'answer': '9f6310136158a873a916893e981e16d0',
          'choices': [
            'I continue since I cannot do anything if the left_adjacent piece is off the edge of the board.',
            'I can swap a piece with None, so I swap piece_at_xy and left_adjacent.',
            'I place a new piece at the location of left_adjacent.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What happens if left_adjacent is None?'
        },
        {
          'answer': 'b7fa3ed4b32c28bbd40ffe8e26ed3edf',
          'choices': [
            'It is moved to the left and action_taken is set to True.',
            'It is moved to the left and action_taken is set to False.',
            'It is not moved to the left and action taken is set to True.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What happens if I can move a piece left?'
        },
        {
          'answer': '760b760b7fccc6710f5e1a16a436df7e',
          'choices': [
            'We end our move.',
            'We keep going.',
            'action_taken is never True.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What happens if action_taken is True"?'
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}
