##Problem Set 3
##Problem 3
##Natalie

from string import *

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
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
