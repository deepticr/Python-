import random
player1=input("Select rock, paper or scissor: ")
print('Player1 choosed:' + str(player1))
player2=random.choice(["rock","paper","scissor"])
print("player 2 selected:",player2)
if player1=="rock"and player2=="paper":
    print("player2 won the game and player1 lost the game")
elif player1=="paper"and player2=="scissor":
    print("player2 won the game and player1 lost the game")
elif player1=="scissor"and player2=="rock":
    print("player2 won the game and player1 lost the game")
elif player1==player2:
    print("tie")
else :
    print("player1 won the game and player2 lost the game ")




