def mySum(num):
    running_sum = 0
    addNumb = []
    for i in range(1, num+1):
        running_sum += i
        addNumb.append(running_sum)
    print(addNumb[-1])
    average = sum(addNumb)/len(addNumb)
    print(average)

mySum(10)