import Crossword
import copy

def BacktrackingSearch(CSP):
    return RecursiveBacktrackingSearch(CSP.Assignment, Crossword.CSP)

def RecursiveBacktrackingSearch(Assignment, CSP):
    if goalTest(CSP, Assignment):
        print("RETURNING:", Assignment)
        return Assignment
    var = selectUnassignedVar(CSP)

    #Lista = copy.deepcopy(var.WordList)
    for i in var.WordList:
        if TestingConstraints(var, CSP, i):
            Assignment[var] = i
            CSPcpy = copy.deepcopy(CSP)
            print(var.Line, var.Index, i)
            print(Assignment)
            RemoveWords(CSPcpy, i, var)
            print("A1 WORDLIST:", CSPcpy.A1.WordList)
            print("A2 WORDLIST:", CSPcpy.A2.WordList)
            print("A3 WORDLIST:", CSPcpy.A3.WordList)
            print("D1 WORDLIST:", CSPcpy.D1.WordList)
            print("D2 WORDLIST:", CSPcpy.D2.WordList)
            print("D3 WORDLIST:", CSPcpy.D3.WordList)
            result = RecursiveBacktrackingSearch(Assignment, CSPcpy)
            if result is not False:
                return result
            print("POPED", Assignment.popitem())
            var.Word = "000"
            AddWords(CSPcpy, i, var)
        # if i in Lista:
        #     if i in var.WordList:
        #         var.WordList.remove(i)
    return False


def goalTest(CSP, Assigment):
    for i in CSP.Puzzle:
        if i.Word is "000":
            return False
    return Assigment

def selectUnassignedVar(CSP):
    num = 0
    Nr = 0
    var = copy.copy(CSP.A1)
    for x in var.WordList:
        num = num + 1
    for i in CSP.Puzzle:
        if i.Word is "000":
            for x in i.Word:
                Nr = Nr + 1
            if Nr < num:
                var = copy.copy(i)
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


    if domainEmptyTest(CSPcpy, var):
        return True


    #print("DOMAIN EMPTY")
    return False

def domainEmptyTest(CSPcpy, var):
    for i in CSPcpy.Puzzle:
        if i.NrWords is 0 and i.Word != "000":
            return False
    return True

def RemoveWords(CSPcpy, word, var):

    if var.Line < 3:
        Crossing = [CSPcpy.Puzzle[3], CSPcpy.Puzzle[4], CSPcpy.Puzzle[5]]
    else:
        Crossing = [CSPcpy.Puzzle[0], CSPcpy.Puzzle[1], CSPcpy.Puzzle[2]]

    for position in CSPcpy.Puzzle:
        if word in position.WordList:
            position.WordList.remove(word)
            position.NrWords = position.NrWords - 1

    i = 0
    for position in Crossing:
        cpyList = copy.deepcopy(position.WordList)
        for ORD in cpyList:
            if ORD[var.Index] is not word[i]:
                position.WordList.remove(ORD)
                position.NrWords = position.NrWords - 1

        i = i + 1

def AddWords(CSPcpy, word, var):
    if var.Line < 3:
        Crossing = [CSPcpy.Puzzle[3], CSPcpy.Puzzle[4], CSPcpy.Puzzle[5]]
    else:
        Crossing = [CSPcpy.Puzzle[0], CSPcpy.Puzzle[1], CSPcpy.Puzzle[2]]

    for position in CSPcpy.Puzzle:
        if word not in position.WordList:
            if position.Index is not var.Index and position.Line is not var.Line:
                    position.WordList.append(word)
                    position.NrWords = position.NrWords + 1

    i = 0
    for position in Crossing:
        OriginalList = copy.deepcopy(position.Original)
        for j in OriginalList:
            if j[var.Index] is not word[i]:
                if j not in position.WordList:
                    position.WordList.append(j)
                    position.NrWords = position.NrWords + 1
            if word not in position.WordList:
                position.WordList.append(word)

        i = i + 1
