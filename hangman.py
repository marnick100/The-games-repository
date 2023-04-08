import random

words = ["python", "programming", "computer", "science", "algorithm", "database", "javascript"]

word = random.choice(words)
word_length = len(word)
letters = set(word)
alphabet = set("abcdefghijklmnopqrstuvwxyz")
used_letters = set()

lives = 6

while len(letters) > 0 and lives > 0:
    print("You have", lives, "lives left and you have used these letters:", " ".join(used_letters))
    
    word_list = [letter if letter in used_letters else "-" for letter in word]
    print("Current word: ", " ".join(word_list))
    
    user_letter = input("Guess a letter: ").lower()
    
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in letters:
            letters.remove(user_letter)
        else:
            lives = lives - 1
            print("Letter is not in word.")
    
    elif user_letter in used_letters:
        print("You have already used that letter. Guess another letter.")
    
    else:
        print("Invalid character. Please try again.")
    
if lives == 0:
    print("Sorry, you died. The word was", word)
else:
    print("Congratulations! You guessed the word", word, "in", len(used_letters), "tries.")
