# Problem Set 5: Ghost
# Name: Natalie
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def is_valid(entry,fragment):
	"""
	Recursively checks if an entry is valid. If is valid adds entry to fragment and returns
	fragment. If not valid prompts for a new entry until a valid one is entered.
	
	entry: string
	fragment: string
	return: string
	"""
	if len(entry) == 1 and entry in string.ascii_letters:
		fragment=fragment+entry
	else:
		print "'" + str(entry) + "' is not a valid entry. "
		entry=raw_input('Please enter a letter: ')
		fragment=is_valid(entry,fragment)
	return fragment


def is_pos_word(fragment):
	"""
	Evaluates if a word can be started with fragment. 
	
	fragment: string
	return: boolean  
	"""
	is_pos=False
	for word in wordlist:
		if word[0:len(fragment)] == fragment:
			is_pos=True
			break
	return is_pos
	

def switch_player(player):
	"""
	Switches the player # between 1 and 2.
	
	player: int 1 or 2
	return: int 1 or 2
	"""
	if player == 1:
		return 2
	else:
		return 1

	
def is_word(fragment):
	"""
	Evaluates if fragment is a word larger than 3 characters long. 
	
	fragment: string
	return: boolean
	"""
	return len(fragment) > 3 and fragment in wordlist


def ghost():
	fragment=''
	print "===============\nWelcome to Ghost!\n===============\n"
	player=1 #start with player 1
	first=True #indicated first round, where the display is a little bit different
	game_on=True #True till game ends
	while game_on:
		print "Current word fragment: '" + fragment.upper() +"'"
		if not is_word(fragment) and is_pos_word(fragment): #checks the fragment at the start of each round to see if it ends the game
			if first: #different display for round 1
				print "Player 1 goes first."
				first = False
			else:
				player=switch_player(player) #switches players if the game is still on after checking previous players fragment
				print "\nPlayer " + str(player) + "'s turn." 
			entry=raw_input('Player ' + str(player) + ' says letter: ')
			fragment=is_valid(entry.lower(),fragment) #checks entry, and updates fragment
			print '\n'
		elif is_word(fragment): #checks if word first, since pos_word will be true if it is a word
			print "Player " + str(player) + " loses because '" + fragment.upper() + "' is a word!"
			print "Player " + str(switch_player(player)) + " wins!"
			game_on=False #ends game
		elif not is_pos_word(fragment): #dont really need the elif, could just be else, but I wanted to reference to know what happened
			print "Player " + str(player) + " loses because no word begins with '" + fragment.upper() + "'!"
			print "Player " + str(switch_player(player)) + " wins!"
			game_on=False #ends game
	print "\n===============\nGame Over!\n===============\n"
			
ghost()		
			
		

	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	