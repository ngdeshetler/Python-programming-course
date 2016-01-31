##Problem Set 3
##Problem 4
##Natalie

from string import *

def subStringMatchExactlyOneSub(target,key):
    one_off=[] #list of references that the key is onle one off
    exacts=list(subStringMatchExact (target, key))
    possibles=list(set(subStringMatchOneSub(key,target))) #set is a cheat to remove duplicates, and then list makes it indexable
    possibles.sort() #this is for my preference for the output to be ordered
    for n in range(0,len(possibles)):
        if not (possibles[n] in exacts):
            one_off.append(possibles[n])
    return tuple(one_off)
