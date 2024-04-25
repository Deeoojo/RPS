from getpass import getpass as input
print("A Demi game of Rock, Paper and Scissors")
print("This would be between two players. Think you're better than your opponent?")
print("Show em!!!😀")
print()
while True:
  print("R = Rock. P = Paper S = Scissors Q = Quit")
  player1 = input("Player 1, Rock, Paper, Scissors?> ")
  player2 = input("Player 2, Rock, Paper, Scissors?> ")
  if player1 == "Q" or player1 == "q":
    print("Thank you for playing")
    break
  if player2 == "Q" or player2 == "q":
    print("Thank you for playing")
    break
  if player1 == player2:
    print("it's a tie, are you reading minds now?")
  if player1 == "R" or player1 == "r":
    if player2 == "S" or player2 == "s":
      print("Rock beats Scissors all day, Player1 wins")
    elif player2 == "P" or player2 == "p":
      print("Paper wins Rock, Player 2 wins")
  if player1 == "P" or player1 == "p":
    if player2 == "R" or player2 == "r":
      print("Paper wins Rock, Player 1 wins")
  if player1 == "S" or player1 == "s":
    if player2 == "p" or player2 == "p":
      print("Scissors cut the paper into shreddsss, Player1 wins")
  if player1 == "P" or player1 == "p":
    if player2 == "S" or player2 == "s":
      print("Scissors cut the paper into shreddsss, Player2 wins")
  if player1 == "S" or player1 == "s":
    if player2 == "R" or player2 == "r":
      print("Rock beats Scissors all day, Player2 wins")
  
