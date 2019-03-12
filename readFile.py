def newFile():
    dictList = []
    dictKey = ['D', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6']

    file = open("C:\SomervilleHappinessSurvey2015.csv", "r")
    tst = file.read()
    tst = tst.split('\n')
    del tst[0]
    del tst[-1]

    for i in tst:
        pos = 0
        tmp = {}
        for var in i:
            if var is not ';':
                tmp[dictKey[pos]] = var
                pos = pos + 1
        dictList.append(tmp)

    return dictList