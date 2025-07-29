player = input("Enter your choice (rock, paper, scissors): ").lower()
import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
print("Computer chose:", computer)
if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
# Ask if the player wants to play again
play_again = input("Do you want to play again? (yes/no): ").lower()
while play_again == "yes":
    player = input("Enter your choice (rock, paper, scissors): ").lower()
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
print("Thanks for playing!")    


# Flame game
string1 = input("Enter your name: ")
string2 = input("Enter your crush's name: ")
def flame_game(name1, name2):
    combined = name1 + name2
    count = 0
    for char in combined:
        if char.lower() in "aeiou":
            count += 1
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    index = (count - 1) % len(flames)
    return flames[index]
result = flame_game(string1, string2)
print(f"The result of the FLAMES game for {string1} and {string2} is: {result}")
# Rock Paper Scissors game

