import Crossword
import BacktrackingSearch
import copy

def main():
    cross = Crossword.CSP()
    print(cross.Puzzle)
    #print(BacktrackingSearch.selectUnassignedVar(cross))
    print(BacktrackingSearch.TestingConstraints(cross.A1, cross, "BAT"))
    print("D1:", cross.D1.WordList)
    print("D2:", cross.D2.WordList)
    print("D3:", cross.D3.WordList)
    cross.A1.Word = "BAT"
    #print(BacktrackingSearch.TestingConstraints(cross.D1, cross, "ADD"))
    #print(BacktrackingSearch.TestingConstraints(cross.D2, cross, "ADD"))


    #BacktrackingSearch.BacktrackingSearch(cross)



main()