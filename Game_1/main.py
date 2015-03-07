# Game 1: Rock-paper-scissors-lizard-Spock - RPSLS
# name: "rock", "paper", "scissors", "lizard", or "Spock" in priority
# 0 rock
# 1 Spock
# 2 paper
# 3 lizard
# 4 scissors

from random import randint

def translate(x):
    moves = ["rock", "paper", "scissors", "lizard", "Spock"]
    if isinstance(x, basestring):
        i = 0
        while(i <len(moves)) and (moves[i] != x):
            i = i+1
    elif isinstance(x, int):
        i = x
    return moves[i]

def wins(a,b):  # If first variable compared wins, true is returned. Otherwise false returned
    return (a > b)

def rpsls(name):
    computer = randint(0,4)
    user = translate(raw_input('What do you present (rock, Spock, paper, lizard, or scissors: '))

    print "Computer chose", translate(computer), "and user chose", user
    if wins(computer,user):
        print "Computer wins!"
    else:
        print "User wins!"

def main():
    rpsls("rock")

if __name__ == '__main__':
    main()