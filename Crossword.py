import copy

class WordObject(object):
    Name = ""
    Word = ""
    WordList = []
    NrWords = -1
    Line = -1
    Index = -1

    def CreateLine(self, index, line, name):
        self.Word = "000"
        self.NrWords = 40
        self.Index = index
        self.Line = line
        self.Name = name
        self.WordList = ["ADD", "ADO", "AGE", "AGO", "AID",
                         "AIL", "AIM", "AIR", "AND", "ANY",
                         "APE", "APT", "ARC", "ARE", "ARK",
                         "ARM", "ART", "ASH", "ASK", "AUK",
                         "AWE", "AWL", "AYE", "BAD", "BAG",
                         "BAN", "BAT", "BEE", "BOA", "EAR",
                         "EEL", "EFT", "FAR", "FAT", "FIT",
                         "LEE", "OAF", "RAT", "TAR", "TIE"]
        return self


class CSP(object):
    Puzzle = []
    Assignment = {}

    A1 = WordObject()
    A2 = WordObject()
    A3 = WordObject()
    D1 = WordObject()
    D2 = WordObject()
    D3 = WordObject()

    Puzzle.append(A1.CreateLine(0, 0, "A1"))
    Puzzle.append(A2.CreateLine(1, 1, "A2"))
    Puzzle.append(A3.CreateLine(2, 2, "A3"))
    Puzzle.append(D1.CreateLine(0, 3, "D1"))
    Puzzle.append(D2.CreateLine(1, 4, "D2"))
    Puzzle.append(D3.CreateLine(2, 5, "D3"))
    Original = copy.deepcopy(A1.WordList)
