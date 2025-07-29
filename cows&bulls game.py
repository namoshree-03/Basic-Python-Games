#cowsbulls game
import random   
def generate_number():
    """Generate a random 4-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def cows_and_bulls():
    num = generate_number()
    attempts = 0
    while True:
        guess = input("Enter your 4-digit guess: ")
        if guess == num:
            print("Congratulations! You've guessed the number.")
            break
        else:
            attempts += 1
            cows = sum(1 for a, b in zip(guess, num) if a == b)
            bulls = len(set(guess) & set(num)) - cows
            print(f"Cows: {cows}, Bulls: {bulls}")
    print(f"It took you {attempts} attempts to guess the number.")
if __name__ == "__main__":
    print("Welcome to the Cows and Bulls game!")
    cows_and_bulls()
a = input("Do you want to play again? (yes/no)")
if a.lower() == 'yes':
    cows_and_bulls()
else:
    print("Goodbye! Thanks for playing.")



# This is a simple implementation of the Cows and Bulls game.
# The player has to guess a 4-digit number with unique digits.
# The game provides feedback on the number of cows (correct digits in the correct place)
# and bulls (correct digits in the wrong place) after each guess.
# The game continues until the player guesses the number correctly.
# The player can enter guesses until they find the correct number.
# The number of attempts is counted and displayed at the end.
# The game uses a random number generator to create the target number.
# The digits in the generated number are unique, ensuring a fair game.
# The game is played in the console, and the player interacts with it through text input.
# The game can be extended with features like input validation, difficulty levels, or a scoring system.
# The current implementation is straightforward and easy to understand.
# The game can be played multiple times by running the script again.
# The player can improve their guessing strategy based on the feedback received.
# The game is suitable for players of all ages and can be a fun way to practice logical thinking and deduction skills.
# The game can be modified to include more digits or different rules for added complexity.
# The implementation is efficient and runs in linear time relative to the number of guesses.                
# The game can be easily adapted for different programming languages or platforms.
# The code is structured to be clear and maintainable, making it easy to add new features or modify existing ones.