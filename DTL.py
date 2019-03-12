import readFile
from decisionTree import *
import math

def NrOfAnswers(Examples, S):
    List = []
    Answers = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0} # Dict to hold nr of answers for each value
    for i in Examples:                                 # Append all values for S in to a list
        List.append(i.get(S))

    for i in List:                                    # for every answer, find the corresponding position
        for key in Answers:                           # in answer dict and add 1 to the value
            if key == i:
                Answers[key] += 1
    return Answers

def CalculateEntropy(Examples, S):
    HS = 0                                                  # Set to 0 every time function is called
    Answers = NrOfAnswers(Examples, S)
    len = Examples.__len__()
    D0 = []
    D1 = []

    for i in Examples:
        #For all D == 1 append in list D1
        if i.get('D') == '1':
            D1.append(i)
        else:
        # If D == 0 append in list D0
            D0.append(i)

    print('D1:', D1)
    print('D0:', D0)


    return HS


def InformationGain(Examples, A):
    HA = 0
    HS = CalculateEntropy(Examples, 'D')
    print('D:', HS)
    #for value in Examples:
     #   for i in value.get(A):
      #      E_v =
       #     HA = HA + abs(E_v.__len__)/abs(Examples.__len__()*CalculateEntropy(E_v, S))
    #print(HS-HA)
    return HS - HA

#Om en X1 är 1 och alla D är 0 = classcheck