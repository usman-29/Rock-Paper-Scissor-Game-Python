# Rock Paper Scissor game
import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print(f"Computer: {computer}")
        return 'tie'
    elif is_win(user, computer):
        print(f"Computer: {computer}")
        return "You won!"
    else:
        return "You lost!"




def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True



print(play())
