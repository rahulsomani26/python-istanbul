def sum_list(markslist):
    sum=0
    for item in markslist:
        sum=sum+item
    return sum

def getMin(markslist):
    # return min(markslist)
    minval=0
    for item in markslist:
        if item < minval:
            minval=item
    return minval

def getMax(markslist):
    # return min(markslist)
    maxval=0
    for item in markslist:
        if item > maxval:
            maxval=item
    return maxval



    
    
if __name__ == '__main__':
    print(" Sum of numbers in a List")
    marks=[-1,2,3,4,5]
    sum=sum_list(marks)
    print(sum)
    min = getMin(marks)
    print(min)    
    max = getMax(marks)
    print(max)
    