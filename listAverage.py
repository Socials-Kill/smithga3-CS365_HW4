def findAverage(myList):
    
    avg = 0
    count = 0

    for x in myList:
        avg += x
        count += 1

    avg = avg / count

    print("The average value of the list is ", avg, "\n")
    return avg
