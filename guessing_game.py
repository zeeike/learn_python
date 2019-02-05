secret_word = "giraffe"
guess = ""

while guess != secret_word:
    print(guess + "Was your old guess")
    secret_word = input("Please enter your guess: ")
    print(guess + "was your guess")

print("You win the guessing game")