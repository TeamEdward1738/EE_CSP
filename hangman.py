# EE, hangman
import random

# create a list of 10 words on a seperate txt file

# create another file holds win/loss counts

#use split(",") on the content of the words txt document to create your list of words

#pull win and lose totals from the other txt file and save them as 2 seperate variables

# build the hangman game

#save the correct word as a variable random.choice(name of the list)

#number of wrong guesses

#What letters have been guessed

 #function too diplay the hangman
"""______
   |    |
   |    O
   |   /|\\
   |   /  \\
   |__________
"""
#function to show the letters and space(The correct word, letters that have been guessed)
# loop over the correct word
    # varible for display word(start as an empty string)
    #check if letter has been guessed
        #then add the letter to the display word
    #if they haven't guessed the letter
        # add an underscore to te display word
# returns the finished display word (outside of the loop)


# Main game loop (while True)
    #call function to show hangman
    # print function call to show display word
    # create variable and ask user to guess a letter
    # add the letter to list of guessed letters
    # check if not letter in word:
        # increase incorrect guesses
    #check if display word is the same as the word
        # Tell user tey won!
        # increas win total
        #ask them if they want to play again
            #reset random word, rest wrong guess
    #check to see if they lost (if they have 6 wrong guesses)
        #tell them they lost
        #tell them what the word was
        #Increase the lost count
        #ask if they want to play again
                    #reset random word, rest wrong guess count
                    