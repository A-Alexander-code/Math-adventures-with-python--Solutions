def fcg(num1, num2):
    print('returns a list of the factors of num')
    factorList1 = []
    factorList2 = []
    commonFactor = []
    for i in range(1, num1+1):
        if num1%i == 0:
            factorList1.append(i)
    for i in range(1, num2+1):
        if num2%i == 0:
            factorList2.append(i)
    for i in factorList1:
        for j in factorList2:
            if i == j:
                commonFactor.append(i)
    maxValue = max(commonFactor)
    print(str(maxValue))

fcg(150, 138)