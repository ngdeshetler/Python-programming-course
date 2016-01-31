##Problem Set 3
##Problem 2
##Natalie

from string import *

def subStringMatchExact (target, key): 
	locations=[] #epmty list of locations
	ref=find(target,key) #finds the reference location
	if ref > -1: #if there is a reference
                if ref+1<len(target): #if the reference isnt at the end of the list (need this for referencing '')
                        locations=list(subStringMatchExact(target[ref+1:], key)) #recursively find the previous locations
                        locations=[item+ref+1 for item in locations] #since the reference is based on a shorter list, need to add the earlier reference to previous values
		locations.insert(0,ref) #recursion causes the list to build backward, so we add to the front
	return tuple(locations) #returns in format tuple

