HEIGHT = 6
WIDTH = 7

def init():
  #Sets up the empty board
  pass 

def print_board(board):
  #Print out a correct board 
  pass

def get_move(board, player): 
  ''' Takes the board and the player as parameters. Asks the player to input a column and checks if the entry is valid'''
  pass 

def make_move(board, player, col): 
  '''Takes the board, the player, and the players entry and makes the move based on the board configuration and the entry.'''
  pass

def check_win(board):
  '''This function takes the board as a parameter and checks if someones has won the game. If so, if returns the player that has won. Otherwise, it returns an empty string.'''
  pass 

def main(): 
  '''Sets up the game and runs the game loop until the game is over.'''
  board = init()
  player = "R"
  winner = ""

  while winner == "":
    print_board(board)
    col = get_move(board, player) 
    make_move(board, player, col)
    winner = check_win(board)
    if player == "R":
      player = "B"
    else: 
      player = "R"

  print_board(board)
  if winner == "Tie":
    print("Tie Game.")
  else: 
    print("Player {} wins!".format(winner))

if __name__ == "__main__":
  main()

  