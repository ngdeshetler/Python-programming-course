##Problem Set 3
##Natalie

from string import *

##Problem 1

def countSubStringMatch(target,key):
	ref=-1 #starts ar -1, so +1 will be 0
	instances=0 #count of instances of key
	while ref+1 < len(target): #only looks in the range of target
                ref=find(target,key,ref+1)
                if ref != -1: #if there is a target
        		instances += 1
        	else:
                        break #breaks out of the while if no more keys can be found
	return instances 


def countSubStringMatchRecursive (target, key): 
	ref=find(target,key) 
	if ref != -1: #if there is a reference
                if ref+1<len(target): #if there is more of the list to check
                        return 1+countSubStringMatchRecursive (target[ref+1:], key) #return 1 plus check the rest of the list
                else: #if its the end of the target return 1
                        return 1
	else:
		return 0 #if there isnt a match in range, return 0

##Problem 2

def subStringMatchExact (target, key): 
	locations=[] #epmty list of locations
	ref=find(target,key) #finds the reference location
	if ref > -1: #if there is a reference
                if ref+1<len(target): #if the reference isnt at the end of the list (need this for referencing '')
                        locations=list(subStringMatchExact(target[ref+1:], key)) #recursively find the previous locations
                        locations=[item+ref+1 for item in locations] #since the reference is based on a shorter list, need to add the earlier reference to previous values
		locations.insert(0,ref) #recursion causes the list to build backward, so we add to the front
	return tuple(locations) #returns in format tuple

##Problem 3

def constrainedMatchPair(firstMatch,secondMatch,length):
    constrained=[] #I really hate working with tuples
    for n in range(0,len(firstMatch)):
        for k in range(0,len(secondMatch)):
            if firstMatch[n]+length+1==secondMatch[k]:
                constrained.append(firstMatch[n])#so much easier to add to!
    return tuple(constrained)
    
### the following procedure you will use in Problem 3

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
##        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
##        print 'match1',match1
##        print 'match2',match2
##        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

##Problem 4

def subStringMatchExactlyOneSub(target,key):
    one_off=[] #list of references that the key is onle one off
    exacts=list(subStringMatchExact (target, key))
    possibles=list(set(subStringMatchOneSub(key,target))) #set is a cheat to remove duplicates, and then list makes it indexable
    possibles.sort() #this is for my preference for the output to be ordered
    for n in range(0,len(possibles)):
        if not (possibles[n] in exacts):
            one_off.append(possibles[n])
    return tuple(one_off)
