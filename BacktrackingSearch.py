import Crossword
import copy

def BacktrackingSearch(CSP):
    return RecursiveBacktrackingSearch(CSP.Assigment, CSP)


def RecursiveBacktrackingSearch(Assignment, CSP):
   if goalTest(CSP, CSP.Assignment):
       return CSP.Assignment


def goalTest(CSP, Assigment):
    for i in CSP.Puzzle:
        if i.Word is "000":
            return False
    return Assigment

def selectUnassignedVar(CSP):
    var = copy.deepcopy(CSP.A1)
    for i in CSP.Puzzle:
        if i.Word is "000":
            if i.noOfWords < var.noOfWords:
                var = copy.deepcopy(i)
    return var

def TestingConstraints(var, CSPcpy, word):
    if var.Line < 3:
        Crossing = [CSPcpy.Puzzle[3], CSPcpy.Puzzle[4], CSPcpy.Puzzle[5]]
    else:
        Crossing = [CSPcpy.Puzzle[0], CSPcpy.Puzzle[1], CSPcpy.Puzzle[2]]

    WordPosition = 0
    for node in Crossing:
        if word[WordPosition] is not node.Word[var.Index]:
            if node.Word[var.Index] is not "0":
                print("DO NOT FIT")
                return False
        WordPosition = WordPosition + 1

    i = 0
    for position in Crossing:
        cpyList = copy.deepcopy(position.WordList)
        for ORD in cpyList:
            if ORD[var.Index] is not word[i]:
                position.WordList.remove(ORD)
                #print(ORD, "removed")
                position.NrWords = position.NrWords - 1
        i = i + 1

    if domainEmptyTest(CSPcpy):
        return True

    return False

def domainEmptyTest(CSPcpy):
    for i in CSPcpy.Puzzle:
        if i.NrWords is 0:
            return False
    return True
