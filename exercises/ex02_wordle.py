"""The creation of wordle for my Computer Science Class"""

__author__: str = "730667424"


def contains_char(word: str, char: str) -> bool:
    """This function will check to see if a character is in a word"""
    assert len(char) == 1, f"len('{char}') is not 1"
    for i in range(
        len(word)
    ):  # gonna use a for loop here to iterate over each letter in the string
        if word[i] == char:  # if that letter is the character, return true
            return True
    return False  # otherwise its false


def emojified(guess: str, secret: str) -> str:
    """This function will emojify the result of your guess based on Wordle's logic"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    response = ""  # Going to start with an empty string, and i iterate, the emoji will be added
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            response += (
                "\U0001F7E9"  # if the letters are the same in the same spot, then green
            )
        elif contains_char(secret, guess[i]):
            response += "\U0001F7E8"  # if not in the same spot, but contains char is True, the yellow
        else:
            response += (
                "\U00002B1C"  # can just say else here, because anything else is white
            )
    return response


def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word:")
    while (
        len(guess) != expected_length
    ):  # Doing a while loop so it keeps asking for an input (Originally was trying to do an if statement for a long time)
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess  # returning guess will either return the correct thing if done, but while it is not the right length, will ask for input again, because we redefine guess in the while loop


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 6
    for i in range(1, 7):  # You get 6 turns, so six iterations
        print(f"=== Turn {i}/{turns} ===")
        guess = input_guess(
            len(secret)
        )  # your guess is gonna be the length of the secret word
        response = emojified(
            guess, secret
        )  # the response is the emojis according to your guess
        print(response)

        if guess == secret:
            print(f"You won in {i}/{turns} turns!")
            return  # So that the game ends if youre correct and stops iterating

    print(f"X/{turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
