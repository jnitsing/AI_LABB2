import Crossword
import BacktrackingSearch

def main():
    cross = Crossword.CSP()
    BacktrackingSearch.BacktrackingSearch(cross)
    print(cross.Assignment)
main()