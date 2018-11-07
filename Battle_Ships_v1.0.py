"""
BattleShip Game using python
v1.0
"""

from random import randint
  
#Main Game Starts Here
def start_game():
    #the main board
  board = []

  for x in range(5):
    board.append(["O"] * 5)
  #function that prints board to the console
  def print_board(board):
    for row in board:
      print " ".join(row)

  print_board(board)

  def random_row(board):
    return randint(0, len(board) - 1)

  def random_col(board):
    return randint(0, len(board[0]) - 1)
  for turn in range(4):
    print "Turn "+ str(turn+1)
    #vars holding coordinates for the ship
    ship_row = random_row(board)
    ship_col = random_col(board)
    try:
    	guess_row = int(raw_input("Guess Row: "))
    except ValueError:
      print "You should enter a whole number"
      start_game()
    try:
      guess_col = int(raw_input("Guess Col: "))
    except ValueError:
      print "You should enter a whole number"
      start_game()
  ################################
    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sunk my battleship!"
      break
    else:
      if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print "Oops, that's not even in the ocean."
      elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
      # Print (turn + 1) here!
      print_board(board)
      if turn==3:
        print 'Game Over'
      	replay=raw_input("play again?(Y/N)")
        if replay=="Y":
          start_game()
        elif replay=="N":
          print "exiting";
        
start_game()      
 #The End
