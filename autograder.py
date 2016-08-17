starter = __import__("starter_2048", fromlist=['x'])
utils = __import__("utils", fromlist=['x'])
import time
import os

def tests_2048():

    print("Testing...");

    msg = "\nWhich option would you like to test?\n";
    msg += "0\t\tQuit\n";
    msg += "1\t\tget_piece and place_piece\n";
    msg += "2\t\tplace_random\n";
    msg += "3\t\thave_lost\n";
    msg += "4\t\tend_move\n"
    msg += "5\t\tswap_possible\n"
    msg += "6\t\tswap\n"

    #Runs suite of tests
    while True:

        print(msg);

        #Gets the key pressed
        key = utils.get_key_press()

        N = 4
        board = utils.make_board(N)

        ###########################################
        #Quit case ('0')
        if key == 48 or key==113:
            quit();


        ###########################################
        #Test case: get_piece and lace_piece ('1')
        elif key == 49:
            try:
                #Tests that they are returning None properly during an invalid (x,y) call
                result = (None == starter.get_piece(-1, -1, board)          ==
                                  starter.get_piece(N, N, board)
                         );
                assert result, "Not returning None properly during an invalid get or misunderstanding of spec w/ invalid inputs";

                result = (False == starter.place_piece('*', -1, -1, board)  ==
                                   starter.place_piece('*', N, N, board)
                         );
                assert result, "Not returning False properly during an invalid place or misunderstanding of spec w/ invalid inputs";


                #Tests that getting what was placed is possible
                to_place = '0';
                for y in range(N):
                    for x in range(N):
                        starter.place_piece(to_place, x, y, board);
                        assert to_place == starter.get_piece(x, y, board), ("Placed a piece at ", x, ", ", y, " but did not get same piece back");
                        to_place = chr(ord(to_place) + 1);

                assert utils.board_full(board), "N by N Board needs to be full after N*N calls to place_piece at different (x,y) coordinates";

                #Checks against data abstraction violations
                temp_board = utils.make_board(10);
                assert starter.place_piece('7', 7, 7, temp_board) != False, "Abstraction violation. Hard-coded bounds in place_piece. Use the board's dimensions";
                assert starter.get_piece(7, 7, temp_board) != None, "Abstraction violation. Hard-coded bounds in get_piece. Use the board's dimensions";


                print("Test passed.");
                board = utils.make_board(N);      #Clears the board



            except IndexError:
                print("Test failed! Check bounds logic in place_piece and get_piece again. Quitting now...");
                quit();


        ##############################
        #Test case: place_random ('2')
        elif key == 50:
            for i in range(N):
                for j in range(N):  starter.place_random(board);
                utils.print_board(board);
                print("There should be ", (i+1)*(j+1), " spots filled. Pausing for 2 seconds...");
                utils.pause(2);
            assert utils.board_full(board), "N by N Board needs to be full after N*N calls to place_random";

            board = utils.make_board(10);
            while not utils.board_full(board):
                starter.place_random(board);

            #Ensuring there are no asterisks, more 2's than 4's, and more 4's than 8's on the board
            empty, two, four, eight = 0, 0, 0, 0;
            for row in board:
                for piece in row:
                    if piece == '*':    empty += 1;
                    elif piece == '2':  two += 1;
                    elif piece == '4':  four += 1;
                    elif piece == '8':  eight += 1;
                    else:
                        print("Incorrect piece found: ", piece);
                        print("Examine to_place and place piece more carefully... Quitting now");

            assert empty == 0, "If board is full, there shouldn't be empty spaces";
            assert two > four > eight, "Test failed. Ratio is improbable";
            assert 75 >= two >= 45, "There don't seem to be enough 2's. Test failed.";
            assert 50 >= four >= 25, "There don't seem to be enough 4's. Test failed.";
            assert 10 >= eight >= 1, "There don't seem to be enough 8's. Test failed ... BUT retry 1 time";
            assert two + four + eight == 100, "There should only be 2s, 4s, and 8s placed by random";

            print("");
            print("Ensure the ratio is roughly 60/37/3: ");
            print("Twos: ", two);
            print("Fours:", four);
            print("Eights:", eight);
            print("");

            print("Test complete.");
            board = utils.make_board(N);      #Clears the board


        ###########################
        #Test case: have_lost ('3')
        elif key == 51:
            assert not starter.have_lost(board), "An empty board should not lose";
            starter.place_piece('0', 0, 0, board);
            assert not starter.have_lost(board), "A board with 1 piece should not lose";


            board = utils.make_board(2);
            starter.place_piece('0', 0, 0, board);
            starter.place_piece('0', 1, 0, board);
            starter.place_piece('0', 0, 1, board);
            starter.place_piece('0', 1, 1, board);
            assert not starter.have_lost(board), "A full board but with possible moves should not lose";

            board = utils.make_board(2);
            starter.place_piece('1', 0, 0, board);
            starter.place_piece('0', 1, 0, board);
            starter.place_piece('0', 0, 1, board);
            starter.place_piece('1', 1, 1, board);
            assert starter.have_lost(board), "A full board with no possible moves should lose";

            print("Test passed.");
            board = utils.make_board(N);      #Clears the board

        ###########################
        #Test case: end_move ('4')
        elif key == 52:
            utils.clear();
            print("If this msg does not get cleared, test failed. Ensure you always clear the screen before printing a board");
            utils.pause(3.5);
            starter.end_move(board);

            print("There should only be one board on the screen with 1 total piece at a random position");
            utils.pause(3.5);

            starter.end_move(board);
            print("There should only be one board on the screen with 2 total pieces at random positions");
            print("If two boards are on the screen, ensure you always clear the screen before printing a board");
            utils.pause(4);


            now = time.time();
            starter.end_move(board);
            after = time.time();

            assert after - now > .2, ("Not pausing correctly in end_move -- review instructions carefully -- execution took " + str(after - now) + " seconds");
            utils.clear();
            print("Execution of single function should take between .2 and .6 seconds at most.\nYour execution took ", str(after-now));
            print("");

            print("Test complete");
            board = utils.make_board(N);      #Clears the board

        ###########################
        #Test case: swap_possible ('5')
        elif key == 53:
            assert not starter.swap_possible(board), "An empty board cannot perform swap";

            starter.place_piece('0', 0, 0, board);
            assert not starter.swap_possible(board), "A board with 1 piece cannot perform swap";

            starter.place_piece('0', 1, 1, board);
            assert not starter.swap_possible(board), "A board with 2 identical pieces cannot perform swap";

            starter.place_piece('1', 0, 1, board);
            assert starter.swap_possible(board), "A board with 2 unique pieces should be able to perform swap";

            print("Test passed.");
            board = utils.make_board(N);      #Clears the board

        ###########################
        #Test case: swap ('6')
        elif key == 54:
            assert not starter.swap(board), "An empty board should not perform swap";

            starter.place_piece('2', 0, 0, board);
            assert not starter.swap(board), "A board with 1 piece should not perform swap";

            starter.place_piece('2', 1, 1, board);
            assert not starter.swap(board), "A board with 2 identical pieces should not perform swap";

            # check the basic swap situation
            board = utils.make_board(4);
            starter.place_piece('2', 0, 0, board);
            starter.place_piece('4', 1, 0, board);
            assert starter.swap(board), "A board with 2 unique pieces should perform swap";
            assert starter.get_piece(0,0,board)=='4', "The pieces are not correctly swapped. check your swap functions again.";
            assert starter.get_piece(1,0,board)=='2', "The pieces are not correctly swapped. check your swap functions again.";
            assert starter.get_piece(0,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap functions again.";
            assert starter.get_piece(1,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap functions again.";

            # check against static swap situations
            board = utils.make_board(4);
            starter.place_piece('2', 0, 0, board);
            starter.place_piece('4', 1, 1, board);
            assert starter.swap(board), "A board with 2 unique pieces should perform swap";
            assert starter.get_piece(0,0,board)=='4', "The pieces are not correctly swapped. \nYou shoudn't swap randomly, not staticly. \ncheck your swap functions again.";
            assert starter.get_piece(1,1,board)=='2', "The pieces are not correctly swapped. \nYou shoudn't swap randomly, not staticly. \ncheck your swap functions again.";
            assert starter.get_piece(0,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap functions again.";
            assert starter.get_piece(1,0,board)=='*', "There shoudn't be pieces added to empty places. check your swap functions again.";


            #check against swapping of multiple pieces
            board = utils.make_board(4);
            starter.place_piece('2', 0, 0, board);
            starter.place_piece('4', 0, 1, board);
            starter.place_piece('8', 1, 0, board);
            assert starter.swap(board), "A board with 3 unique pieces should perform swap";
            if starter.get_piece(0,0,board)=='2':
                assert starter.get_piece(0,1,board)=='8', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
                assert starter.get_piece(1,0,board)=='4', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
                assert starter.get_piece(1,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap function again.";
            elif starter.get_piece(0,0,board)=='4':
                assert starter.get_piece(0,1,board)=='2', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
                assert starter.get_piece(1,0,board)=='8', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
                assert starter.get_piece(1,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap function again.";
            elif starter.get_piece(0,0,board)=='8':
                assert starter.get_piece(0,1,board)=='4', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
                assert starter.get_piece(1,0,board)=='2', "The pieces are not correctly swapped. \nMultiple swaps probably occurred. \ncheck your swap function again.";
                assert starter.get_piece(1,1,board)=='*', "There shoudn't be pieces added to empty places. check your swap function again.";
            else:
                assert False,"Improper swaps occurred. Check your swap function again";


            print("Test passed.");
            board = utils.make_board(N);      #Clears the board

        ###########################
        else:
            utils.clear();
            print("invalid command.\n");


# Start testing suite for the correct test
def main():
    while(True):
        tests_2048()

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()