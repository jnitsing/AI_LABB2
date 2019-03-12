import DTL
import readFile

def main():
    test=readFile.newFile()
    #for i in test:
    #    print(i)
    #DTL.NrOfAnswers(test, 'X1')
    DTL.CalculateEntropy(test, 'X1')
    #DTL.InformationGain(test, 'X1')

main()