# Problem Set 6: 6.00 Word Game II
# Name: Natalie
#

import random
import string
import time

#
# Below are environment variable
#

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

# --------------------
# Code they gave us:

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

def display_hand (hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def get_time_limit(points_dict, k):
    """
     Return the time limit for the computer player as a function of the
    multiplier k.
     points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
        end_time = time.time()
    return (end_time - start_time) * k 

# --------------------
# Functions made for the game in ps5:
# 

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    updated_hand=hand.copy() #so we dont mess with the original hand
    for i in word: 
        updated_hand[i]= updated_hand[i] - 1 #removes 1 from frequency 
    return updated_hand


# -----------------------------
# Updated versions of functions made in ps5:
# All have been updated to use points_dict instead of word_list

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    bonus=0 #assume no bonus
    score=points_dict[word] #gets score from premade points dictionary
    if len(word) == n: #if word is the length of n add bonus
        bonus=50
    return score+bonus

def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    freq=get_frequency_dict(word) #gets the frequencies of the letters in word
    for i in freq: #looks at each letter in word
        if freq[i] > hand.get(i,0): #if the frequency of the letter in word is greater 
        #than the frequency in the hand its not possible in the hand, so we return false
            return False
    return word in points_dict #if not false above check to see if its a word

def play_hand(hand, points_dict):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    running_score=0
    dead_hand=False
    current_hand=hand.copy() #so we dont mess with the original hand
    while not dead_hand:
        print '\nCurrent Hand:\n'
        display_hand(current_hand)
        print '\n'
        word=raw_input('Enter a word made up of letters in the current hand. \nIf you can not make any more words enter a period (.) to finish.\n\nYour word: ')
        if word == '.':
            dead_hand=True #ends play
        elif is_valid_word(word, current_hand, points_dict):
            running_score += get_word_score(word, sum(hand.values())) #adds word score to running score
            print '\n\t"' + word + '"' + ' earned ' + str(get_word_score(word, sum(hand.values()))) + ' points.'
            current_hand=update_hand(current_hand, word) #update hand
            if sum(current_hand.values()) > 0: #if still letters left in hand
                print '\tYour current score is: ' + str(running_score) + ' points.\n=============='
            else: #empty hand
                dead_hand=True #ends play
        else: #if not valid or not '.'
            print '\n\t"' + word + '" is not a valid word, please try again.'
    print '\n==============\nHand Over\n==============\n\nYour final score is: ' + str(running_score) + ' points.'

def play_game(points_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
  
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), points_dict)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), points_dict)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

# --------------------
# Problem #1: How long?
# Code for playing a game that times the player:

def play_hand_timed(hand, points_dict):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      points_dict: dictionary of possible words and their point values
    """
    # TO DO ...
    running_score=0
    dead_hand=False
    current_hand=hand.copy() #so we dont mess with the original hand
    while not dead_hand:
        print '\nCurrent Hand:\n'
        display_hand(current_hand)
        print '\n'
        start_time=time.time()
        word=raw_input('Enter a word made up of letters in the current hand. \nIf you can not make any more words enter a period (.) to finish.\n\nYour word: ')
        if word == '.':
            dead_hand=True #ends play
        elif is_valid_word(word, current_hand, points_dict):
            end_time=time.time()
            duration=.01 #min time elapsed 
            if end_time-start_time > duration: duration=end_time-start_time #only update duration is larger than min
            running_score += (get_word_score(word, sum(hand.values()))/duration) #adds word score/time it took to answer to running score
            print '\n\tIt took %.2f seconds to provide an answer.' % duration #displays time it took to answer
            print '\t"' + word + '"' + ' earned ' + str("%.2f" % (get_word_score(word, sum(hand.values()))/duration)) + ' points.'
            current_hand=update_hand(current_hand, word) #update hand
            if sum(current_hand.values()) > 0: #if still letters left in hand
                print '\tYour current score is: %.2f points.\n==============' % running_score
            else: #empty hand
                dead_hand=True #ends play
        else: #if not valid or not '.'
            print '\n\t"' + word + '" is not a valid word, please try again.'
    print '\n==============\nHand Over\n==============\n\nYour final score is: %.2f points.' % running_score

def play_game_timed(points_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
  
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand_timed(hand.copy(), points_dict)
            print
        elif cmd == 'r':
            play_hand_timed(hand.copy(), points_dict)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."
            
# --------------------
# Problem #2: Time Limit
# Code for playing a game that has a time limit for players:

def play_hand_timer(hand, points_dict):
    running_score=0
    dead_hand=False
    current_hand=hand.copy() #so we dont mess with the original hand
    time_limit=float(raw_input('Enter time limit, in seconds, for players: ')) #asks for time limit
    elapsed=0.0 #initialize time elapsed
    while not dead_hand:
        print '\nCurrent Hand:\n'
        display_hand(current_hand)
        print '\n'
        start_time=time.time()
        word=raw_input('Enter a word made up of letters in the current hand. \nIf you can not make any more words enter a period (.) to finish.\n\nYour word: ')
        if word == '.':
            dead_hand=True #ends play
        elif is_valid_word(word, current_hand, points_dict):
            end_time=time.time()
            duration=.01 #min time elapsed 
            if end_time-start_time > duration: duration=end_time-start_time #only update duration is larger than min time
            elapsed += duration
            print '\n\tIt took %.2f seconds to provide an answer.' % duration
            if elapsed < time_limit: #if there is still time on the timer then count score
                print '\tYou have %.2f seconds remaining' % (time_limit-elapsed)
                running_score += (get_word_score(word, sum(hand.values()))/duration) #adds word score to running score
                print '\t"' + word + '"' + ' earned ' + str("%.2f" % (get_word_score(word, sum(hand.values()))/duration)) + ' points.'
                current_hand=update_hand(current_hand, word) #update hand
            else: #else no time left to play, so dont add word
                print 'Total time exceeds ' + str(time_limit) + ' seconds.'
                dead_hand=True
            if sum(current_hand.values()) > 0: #if still letters left in hand
                print '\tYour current score is: %.2f points.\n==============' % running_score
            else: #empty hand
                dead_hand=True #ends play
        else: #if not valid or not '.'
            print '\n\t"' + word + '" is not a valid word, please try again.'
    print '\n==============\nHand Over\n==============\n\nYour final score is: %.2f points.' % running_score

def play_game_timer(points_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
  
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand_timer(hand.copy(), points_dict)
            print
        elif cmd == 'r':
            play_hand_timer(hand.copy(), points_dict)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."
            
# --------------------
# Problem #3: Computer Player
# Code for a computer player:

def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value. 
    """
    points_dict={}
    for word in word_list:
        for letter in word:
            points_dict[word]=points_dict.get(word,0)+SCRABBLE_LETTER_VALUES[letter]
    return points_dict

def pick_best_word(hand, points_dict):
    """
    Return the highest scoring word from points_dict that can be made with the
    given hand.
    Return '.' if no words can be made with the given hand.
    """ 
    word='.'#default return '.'
    for pos_word in points_dict:
        if is_valid_word(pos_word, hand, points_dict):
            if points_dict.get(pos_word,0)> points_dict.get(word,0):
                word=pos_word
    return word

def play_hand_timer_computer(hand, points_dict):
    running_score=0
    dead_hand=False
    current_hand=hand.copy() #so we dont mess with the original hand
    elapsed=0.0
    while not dead_hand:
        print '\nCurrent Hand:\n'
        display_hand(current_hand)
        print '\n'
        start_time=time.time()
        word=pick_best_word(current_hand,points_dict)
        print 'The computer played: ' + word
        if word == '.':
            dead_hand=True #ends play
        elif is_valid_word(word, current_hand, points_dict):
            end_time=time.time()
            duration=.01 #min time elapsed 
            if end_time-start_time > duration: duration=end_time-start_time #only update duration is larger than min
            elapsed += duration
            print '\n\tIt took %.2f seconds to provide an answer.' % duration
            if elapsed < time_limit:
                print '\tYou have %.2f seconds remaining' % (time_limit-elapsed)
                running_score += (get_word_score(word, sum(hand.values()))) #adds word score to running score
                print '\t"' + word + '"' + ' earned ' + str("%.2f" % (get_word_score(word, sum(hand.values())))) + ' points.'
                current_hand=update_hand(current_hand, word) #update hand
            else:
                print 'Total time exceeds ' + str(time_limit) + ' seconds.'
                dead_hand=True
            if sum(current_hand.values()) > 0: #if still letters left in hand
                print '\tYour current score is: %.2f points.\n==============' % running_score
            else: #empty hand
                dead_hand=True #ends play
        else: #if not valid or not '.'
            print '\n\t"' + word + '" is not a valid word, please try again.'
    print '\n==============\nHand Over\n==============\n\nYour final score is: %.2f points.' % running_score

def play_game_timer_computer(points_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
  
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand_timer_computer(hand.copy(), points_dict)
            print
        elif cmd == 'r':
            play_hand_timer_computer(hand.copy(), points_dict)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."
            

# --------------------
# Problem #4: Even Faster Computer Player
# Code for a faster computer player:

def get_word_rearrangements(word_list):
    """
    Returns a dictionary whos keys are all the ordered strings that make up the possible words
    and whos values are all the possible words that can be made from those ordered strings
    """
    rearrange_dict={}
    for word in word_list:
        update=rearrange_dict.get(''.join(sorted(word)),[]) #get a list of all the current word that can be made from the rearranged letters
        update.append(word) #need to append here so that your rearranged_dict will contain all words that can be made from those ordered letters
        rearrange_dict[''.join(sorted(word))]=update #my code didnt work when this was done in one step, so i broke it into three
    return rearrange_dict

def build_substrings(string):
    """ Returns all subsets that can be formed with letters in string. """
    # I didnt make this code, I stole if from online
    result = []
    if len(string) == 1:
        result.append(string)
    else:
        for substring in build_substrings(string[:-1]):
            result.append(substring)
            substring = substring + string[-1]
            result.append(substring)
        result.append(string[-1])
    return result

def get_submultiset(hand):
    """
    Returns all the unique, ordered multi-sets of letters than can be made from hand
    """
    full_set='' #holds the full set of letters in hand
    for letter in sorted(hand.keys()): #goes though all the letters in alphabetical order
        for j in range(hand[letter]):
            full_set +=letter #makes an ordered string with all the letters in hand
    return set(build_substrings(full_set)) #returns a set so there are no repeats of substrings

def pick_best_word_faster(hand, points_dict):
    """
    Return the highest scoring word from points_dict that can be made with the
    given hand.
    Return '.' if no words can be made with the given hand.
    """ 
    word='.' #default return '.'
    subsets=get_submultiset(hand) #all the sub(multi)sets that can be made from hand
    for sub_set in subsets: #for each of the subsets
        if sub_set in rearrange_dict: #if they can make a valid word
            for pos_word in rearrange_dict[sub_set]: #for each of the valid words that can be made from the subset
                if points_dict.get(pos_word)> points_dict.get(word,0): #if that valid words point score is greater than the current best words score
                    word=pos_word #update best word to that word
    return word

def play_hand_timer_computer_fast(hand, points_dict):
    running_score=0
    dead_hand=False
    current_hand=hand.copy() #so we dont mess with the original hand
    elapsed=0.0
    while not dead_hand:
        print '\nCurrent Hand:\n'
        display_hand(current_hand)
        print '\n'
        start_time=time.time()
        word=pick_best_word_faster(current_hand,points_dict)
        print 'The computer played: ' + word #so we can see what the computer played
        if word == '.':
            dead_hand=True #ends play
        elif is_valid_word(word, current_hand, points_dict):
            end_time=time.time()
            duration=.01 #min time elapsed 
            if end_time-start_time > duration: duration=end_time-start_time #only update duration is larger than min
            elapsed += duration
            print '\n\tIt took %.2f seconds to provide an answer.' % duration
            if elapsed < time_limit:
                print '\tYou have %.2f seconds remaining' % (time_limit-elapsed)
                running_score += (get_word_score(word, sum(hand.values()))) #adds word score to running score
                print '\t"' + word + '"' + ' earned ' + str("%.2f" % (get_word_score(word, sum(hand.values())))) + ' points.'
                current_hand=update_hand(current_hand, word) #update hand
            else:
                print 'Total time exceeds ' + str(time_limit) + ' seconds.'
                dead_hand=True
            if sum(current_hand.values()) > 0: #if still letters left in hand
                print '\tYour current score is: %.2f points.\n==============' % running_score
            else: #empty hand
                dead_hand=True #ends play
        else: #if not valid or not '.'
            print '\n\t"' + word + '" is not a valid word, please try again.'
    print '\n==============\nHand Over\n==============\n\nYour final score is: %.2f points.' % running_score           

def play_game_timer_computer_fast(points_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
  
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand_timer_computer_fast(hand.copy(), points_dict)
            print
        elif cmd == 'r':
            play_hand_timer_computer_fast(hand.copy(), points_dict)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."
            
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    points_dict=get_words_to_points((word_list))
    rearrange_dict=get_word_rearrangements(word_list)
    k=2
    time_limit=get_time_limit(points_dict, k)
    play_game_timer_computer_fast(points_dict) #change this so that you can test any of the versions of the game
