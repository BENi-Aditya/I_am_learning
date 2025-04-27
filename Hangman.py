import random


hangman = """ _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/         """
                   
life1 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''

life2 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''

life3 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''

life4 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''

life5 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''

life6 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''

life7 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''



print("Starting Hangman, Gotta save the lil guy !!!")

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

random_word = random. choice(words)
#print(random_word)
random_word_into_list = random_word.split()

length = len(random_word)
#print(length)

dash = ('_ ')
dashes = (dash*length)
print(dashes)


def guess(word, current_display):
    user_guess = input('Guess a letter: \n').lower()
    new_display = ''
    display_list = list(current_display.replace(" ", ""))        
    for i in range(len(word)):
        
        if word[i] == user_guess:
            display_list[i] = user_guess    
            
            new_display = ' '.join(display_list)
            return new_display


random_word = random.choice(words)
dashes = '_ ' * len(random_word)
dashes = dashes.strip()  

while True:
    print(dashes)
    dashes = guess(random_word, dashes)
    