def fancy(start,end):
    #Here we will write the logc to check if n is facny number or not
    for num in range(start, end):
        numTemp = num
        remainder = []
        while (numTemp != 0):
            remainder.append(int(numTemp % 10))
            numTemp = int(numTemp/10)
            #for i in range(0, 1):
             #   if (remainder[i] > remainder[i+1]):
              #      print(remainder[i])
            print(remainder)

#Call the function
fancy(1000,1005)