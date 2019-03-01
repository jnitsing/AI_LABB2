import Crossword
import copy

def BacktrackingSearch(CSP):
    return RecursiveBacktrackingSearch(CSP.Assignment, Crossword.CSP)

def RecursiveBacktrackingSearch(Assignment, CSP):
    if goalTest(CSP):
        return Assignment
    var = selectUnassignedVar(CSP)
    #for i in DomainValues(var):
    for i in var.WordList:
        if TestingConstraints(var, CSP, i):
            Assignment[var.Name] = i
            var.Word = i
            RemoveWords(CSP, i, var)
            CPY = copy.deepcopy(CSP)
            result = RecursiveBacktrackingSearch(Assignment, CPY)
            if result is not False:
                return result
            Assignment.popitem()
            var.Word = "000"
            AddWords(CSP, i, var)
    return False

def goalTest(CSP):
    for i in CSP.Puzzle:
        if i.Word is "000":
            return False
    return True

def selectUnassignedVar(CSP):
    x = 41
    for i in CSP.Puzzle:
        if 0 < i.NrWords < x and i.Word is "000":
            x = i.NrWords
            var = i
    return var

def DomainValues(var):
    List = []
    for i in var.WordList:
        List.append(i)
    return List

def TestingConstraints(var, CSPcpy, word):
    if not domainEmptyTest(CSPcpy):
        return False

    if var.Line < 3:
        CrossingList = [CSPcpy.Puzzle[3], CSPcpy.Puzzle[4], CSPcpy.Puzzle[5]]
    else:
        CrossingList = [CSPcpy.Puzzle[0], CSPcpy.Puzzle[1], CSPcpy.Puzzle[2]]

    WordPosition = 0
    for node in CrossingList:
        if word[WordPosition] is not node.Word[var.Index]:
            if node.Word is not "000":
                return False
        WordPosition = WordPosition + 1
    return True

def domainEmptyTest(CSPcpy):
    for i in CSPcpy.Puzzle:
        if i.NrWords is 0 and i.Word == "000":
                return False
    return True

def RemoveWords(CSPcpy, word, var):
    if var.Line < 3:
        CrossingList = [CSPcpy.Puzzle[3], CSPcpy.Puzzle[4], CSPcpy.Puzzle[5]]
    else:
        CrossingList = [CSPcpy.Puzzle[0], CSPcpy.Puzzle[1], CSPcpy.Puzzle[2]]

    for position in CSPcpy.Puzzle:
        if word in position.WordList:
            position.WordList.remove(word)
            position.NrWords = position.NrWords - 1

    i = 0
    for position in CrossingList:
        cpyList = copy.copy(position.WordList)
        for ORD in cpyList:
            if ORD[var.Index] is not word[i]:
                position.WordList.remove(ORD)
                position.NrWords = position.NrWords - 1

        i = i + 1
    return

def AddWords(CSPcpy, word, var):
    if var.Line < 3:
        Cross = [CSPcpy.D1, CSPcpy.D2, CSPcpy.D3]
    else:
        Cross = [CSPcpy.A1, CSPcpy.A2, CSPcpy.A3]

    for position in CSPcpy.Puzzle:
        if word not in position.WordList:
            position.WordList.append(word)
            position.NrWords = position.NrWords + 1

    i = 0
    for position in Cross:
        OriginalWordlist = copy.copy(CSPcpy.Original)
        for j in OriginalWordlist:
            if j[var.Index] is not word[i]:
                if j not in position.WordList:
                    position.WordList.append(j)
                    position.NrWords = position.NrWords + 1
        i = i + 1
    return
