# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name: Natalie
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """
    inputFile = open(filename)
    subjects={}
    for line in inputFile:
        line=line.strip() #to remove the /n at the end of the line?
        parts=line.split(',') #to break line into parts
        subjects[parts[0]]=(int(parts[1]),int(parts[2]))
    return subjects

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    selected={} #classes that will ultimately be seleced and returned
    avail_subs=subjects.copy() #a copy of subjects that can be altered
    current_work=0 #initiate work load at 0
    while len(avail_subs.keys()) > 0: #while there are still subjects in the availiable subjects
        max_holder=min(avail_subs) #just a place to initialize the max_holder at
        for subject in avail_subs:
            if comparator(avail_subs[subject],avail_subs[max_holder]): #if the new subject is better than current subject
                max_holder=subject #set current subject to new subject
        del avail_subs[max_holder] #once selected we dont want to look at it again
        if current_work + subjects[max_holder][1] <= maxWork: #if class can be added without going over maxWork
            current_work += subjects[max_holder][1] #add to selected
            selected[max_holder]=subjects[max_holder]
            if current_work == maxWork: #stop looking at subjects once max is reached
                break
    return selected
    
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    max_to_try=[1,2,4,6,8]
    for timeMax in max_to_try:
        start_time=time.time()
        bruteForceAdvisor(subjects, timeMax)
        end_time=time.time()
        print 'For a max work of %d it took the brute force method %.2f seconds to find a solution' \
        % (timeMax, end_time-start_time)

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
#For a max work of 1 it took the brute force method 0.01 seconds to find a solution
#For a max work of 2 it took the brute force method 0.02 seconds to find a solution
#For a max work of 3 it took the brute force method 0.08 seconds to find a solution
#For a max work of 4 it took the brute force method 0.27 seconds to find a solution
#For a max work of 5 it took the brute force method 0.99 seconds to find a solution
#For a max work of 6 it took the brute force method 2.84 seconds to find a solution
#For a max work of 7 it took the brute force method 11.69 seconds to find a solution
#For a max work of 8 it took the brute force method 27.78 seconds to find a solution
#For a max work of 9 it took the brute force method 75.92 seconds to find a solution
#For a max work of 10 it took the brute force method 220.24 seconds to find a solution


#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    sub_indexable=subjects.keys() #makes a list of the subjects that can use int indexes
    m={} #a dictionary to hold all the calculated values in the recursion
    val, index_subjects=find_max_value(subjects,sub_indexable,len(sub_indexable)-1,maxWork,m)
    selected={} #dictionary to hold the classes selected
    for index in index_subjects: #uses the indexs from the list made above to fill out selected
        selected[sub_indexable[index]]=subjects[sub_indexable[index]]
    print 'Max Value for classes with a max work load of %d is %d' % (maxWork, val)
    return selected
    
    
def find_max_value(subjects,sub_indexable,index,remainder,m): #the actually recursive function used in dp
    try: return m[(index,remainder)] #first check to see if that index and that remainder have already been calculated
    except KeyError: #else
        if index == 0: #base case, ened of the index list
            if subjects[sub_indexable[index]][1] <= remainder: #if the work load of this last case is less than the remaining work load
                m[(index, remainder)]=subjects[sub_indexable[index]][0], [index] 
                return subjects[sub_indexable[index]][0], [index] #return its value and initiate a list with its index as the first item
            else:
                m[(index, remainder)]= 0, []
                return 0, [] #else return zero for its value and a blank list to add other indexes too
        without_i_val, without_i_list= find_max_value(subjects,sub_indexable,index-1,remainder,m) #find the left side of the tre
        if subjects[sub_indexable[index]][1] > remainder: #if the weight is greater than the remainder, stop and return w/o
            m[(index, remainder)]= without_i_val, without_i_list
            return without_i_val, without_i_list
        else: #else find the right side of the tree, removing its work load from the remainder
            with_i_val, with_i_listP=find_max_value(subjects,sub_indexable,index-1,remainder-subjects[sub_indexable[index]][1],m)
            with_i_list=with_i_listP[:] #totally doesnt work if you dont do this
            with_i_list.append(index) #adds index to ones that make up the val
            with_i_val += subjects[sub_indexable[index]][0] #adds indexs value
        if without_i_val > with_i_val: #if w/o is better then w/
            m[(index, remainder)]=without_i_val, without_i_list
            return without_i_val, without_i_list #return w/o
        else: #else return w/
            m[(index, remainder)]=with_i_val, with_i_list
            return with_i_val, with_i_list
        
#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    max_to_try=[1,2,3,4,5,6,7,8,9,10]
    for timeMax in max_to_try:
        start_time=time.time()
        dpAdvisor(subjects, timeMax)
        end_time=time.time()
        print 'For a max work of %d it took the dynamic programing method %.2f seconds to find a solution' \
        % (timeMax, end_time-start_time)

# Problem 5 Observations
# ======================
#
# Max Value for classes with a max work load of 1 is 10
#For a max work of 1 it took the dynamic programing method 0.01 seconds to find a solution
#Max Value for classes with a max work load of 2 is 20
#For a max work of 2 it took the dynamic programing method 0.01 seconds to find a solution
#Max Value for classes with a max work load of 3 is 27
#For a max work of 3 it took the dynamic programing method 0.01 seconds to find a solution
#Max Value for classes with a max work load of 4 is 34
#For a max work of 4 it took the dynamic programing method 0.02 seconds to find a solution
#Max Value for classes with a max work load of 5 is 41
#For a max work of 5 it took the dynamic programing method 0.02 seconds to find a solution
#Max Value for classes with a max work load of 6 is 48
#For a max work of 6 it took the dynamic programing method 0.02 seconds to find a solution
#Max Value for classes with a max work load of 7 is 54
#For a max work of 7 it took the dynamic programing method 0.03 seconds to find a solution
#Max Value for classes with a max work load of 8 is 60
#For a max work of 8 it took the dynamic programing method 0.03 seconds to find a solution
#Max Value for classes with a max work load of 9 is 64
#For a max work of 9 it took the dynamic programing method 0.04 seconds to find a solution
#Max Value for classes with a max work load of 10 is 70
#For a max work of 10 it took the dynamic programing method 0.04 seconds to find a solution





##Test of the various part of the assignment below:

#problem 1: Make Subjects Dictionary
subjects=loadSubjects(SUBJECT_FILENAME)

#problem 2: Greedy Advisor
#maxWork=7
#to_test=[cmpValue,cmpWork,cmpRatio]
#for cmpTest in to_test:
#    comparator=cmpTest
#    print comparator
#    picked=greedyAdvisor(subjects, maxWork, comparator)
#    printSubjects(picked)

#problem 4:Brute Force:
#maxWork=7
#pickedb=bruteForceAdvisor(subjects, maxWork)
#printSubjects(pickedb)
bruteForceTime()

#problem 5: dynamic programing
#maxWork=7
#picked=dpAdvisor(subjects, maxWork)
#printSubjects(picked)
#dpTime()

