def equalizeSize(teamSize, k):
    maxcount = 0
    element_having_max_freq = 0
    n = len(teamSize)
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if(teamSize[i] == teamSize[j]):
                count += 1
        if(count > maxcount):
            maxcount = count
            element_having_max_freq = teamSize[i]

    if (k < len(teamSize)):
        counter_of_done_reductions = 0
        for x in teamSize:
            if(x > element_having_max_freq and counter_of_done_reductions < k):
                counter_of_done_reductions += 1
        result = maxcount + counter_of_done_reductions
        print(result)

    else: print(len(teamSize))



array1 = [1,2,3,2,4]
k1 = 2 #output should be 4 // hi

array2 = [1,2,3,5,4,6,7]
k2 = 10 #output should be 7 //

array3 = [1,8,3,7]
k3 = 1 #output should be 2 / hi

#mostFrequent(array1,k1)
equalizeSize(array1,k1)
#mostFrequent(array2,k2)
equalizeSize(array2,k2)
equalizeSize(array3,k3)
