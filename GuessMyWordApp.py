#Guess My Word App
import random

print("Welcome to the Guess My Word App")

#init dictionary
game_dict = {
    "classes":["mathematics", "philosophy", "science", "biology", "geography", "english"],
    "fruits":["apple", "banana", "orange", "watermelon", "ananas", "kiwi"],
    
    }

game_keys = []

#add to the list game_dict
for key in game_dict.keys():
    game_keys.append(key)

#Use loop
plaing = True
while plaing:
    game_category = game_keys[random.randint(0, len(game_keys)-1)]
    game_word = game_dict[game_category][random.randint(0, len(game_dict[game_category])-1)]

    blank_word = []
    for letter in game_word:
        blank_word.append('-')

    print("\nGuess a " + str(len(blank_word)) + " letter word from the following category: " + game_category)

    guess = ''
    guess_count = 0
    loop = True

    while game_word != guess:
        
        
        
 
            print(str(len(game_word)))
            guess_count += 1
            print("\nThe word is: " + (''.join(blank_word)))
            guess = input("What is this word: ").strip().lower()
            if guess == game_word:
                print("\n!!! You won !!! for " + str(guess_count) + " tries.")
                break
            else:
                print("\nThat is not correct. Let us reveal a letter to help you!")
                flag = True
                while flag:
                    letter_index = random.randint(0, (len(game_word)-1))

                    if  blank_word[letter_index] == '-':
                        blank_word[letter_index] = game_word[letter_index]
                        flag = False
                
                        
             
                
      
    game_end = input("\nWould you like to play again(y/n): ").strip().lower()
    if game_end == 'y':
        continue
    elif game_end == 'n':
        playing = False
        print("\nGoodbay")
        break
    else:
        print("\nInvalid option")
        playing = False
        break
    
    
    

