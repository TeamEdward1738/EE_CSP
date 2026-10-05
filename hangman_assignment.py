#EE, hangman

import random 
with open("words.txt", "r") as file:
    content= file.read()
    content.split
    print(content)
with open("wins_and_losses.txt", "r") as file:
    Content= file.read()
    print(Content)
correct_word= random.choice(content)
wrong_guesses= 0
