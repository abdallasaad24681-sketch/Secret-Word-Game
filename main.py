secret_word = "OpenAI"
guess = ""
guess_count = 0
max_attempts = 10
hint_attempt = 5

while guess_count < max_attempts:

    guess = input("Enter your guess: ").strip()
    guess_count += 1

    if guess.lower() == secret_word.lower():
        print("Congratulations! You've guessed the secret word.")
        break

    else:
        print("Incorrect guess. Try again.")

    print("Attempts left:", max_attempts - guess_count)

    if guess_count == hint_attempt:
        print("Hint: The first letter is:", secret_word[0])

else:
    print("You reached the limit of tries.")
    print("The secret word was:", secret_word)