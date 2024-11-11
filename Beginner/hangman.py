import random

words = [ 'shadow', 'river', 'bliss', 'galaxy', 'puzzle', 'flame', 'wisdom', 'echo', 'valor', 'crystal', 'whisper', 'oasis', 'jungle', 'thunder', 'horizon', 'riddle', 'spark', 'fable', 'mystic', 'ember']
chosen_word = random.choice(words)
word_display = [ '_' for _ in chosen_word]
attempts = 10

print ("Hangman    Game")

while attempts>0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter:").lower()

    if len(guess) != 1 or not guess or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"No letter '{guess}' in the word.")
        attempts -=1
        print(f"ATTEMPTS REMAINING: {attempts}")

if '_' not in word_display:
    print("You guessed the word! The word was: " +chosen_word)
else:
    print ("You failed! The word was: "+chosen_word)
