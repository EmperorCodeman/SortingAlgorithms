def MergeSort(arglist, tabulations):
    id = "mergeSort"
    tabulations[id]["comparisons"] += 1
    if len(arglist) <= 1:
        return#return nothing. this is a break to begin return from recursion
    midPoint = len(arglist) // 2
    leftList = arglist[:midPoint]
    rightList = arglist[midPoint:]
    #Sort the left and right side recursively.
    #list will be chopped recursively until 1. then we come back from recursion with at first two and then more elements in list.
    MergeSort(leftList, tabulations)
    MergeSort(rightList, tabulations)
    #sort lists what ever they may be. Relativity to outtermost is linked by C pointers to data postions.
    #there must be a element in the right and left list because arglist is size 2 or greater
    leftIndex = 0
    rightIndex = 0
    #NOTE LEFT AND RIGHT ARE NOW SORTED. We are only sorting arglist, arglist was rightList and leftList from recursion
    #it follows that the cumlitive size of left and rightLists must be equal to the size of arglist. Therefore the end of
    #arglist is the end of right and leftlists. Therefore by logic no index out of bounds will occure on argList
    #this loop is to load sorted values of left and right list into mother list
    for i in range (arglist.__len__()):
        #if one list has fully loaded its sorted values into mother list then load remaining list and break.
        tabulations[id]["comparisons"] += 1
        if leftIndex >= len(leftList):
            tabulations[id]["comparisons"] += 1
            while rightIndex < len(rightList):
                arglist[i] = rightList[rightIndex]
                tabulations[id]["swaps"] += 1
                i += 1
                rightIndex += 1
            break
        tabulations[id]["comparisons"] += 1
        if rightIndex >= len(rightList):
            while leftIndex < len(leftList):
                tabulations[id]["comparisons"] += 1
                arglist[i] = leftList[leftIndex]
                tabulations[id]["swaps"] += 1
                i += 1
                leftIndex += 1
            break
        #load values in order from left or right list into mother list based of which is lower.
        if leftList[leftIndex] <= rightList[rightIndex]:
            tabulations[id]["comparisons"] += 1
            #asign arglist pointer to value of leftlist pointer, thus no need to return data to outter scope of recursion
            arglist[i] = leftList[leftIndex]
            tabulations[id]["swaps"] += 1
            leftIndex += 1
            continue
        if rightList[rightIndex] < leftList[leftIndex]:
            tabulations[id]["comparisons"] += 1
            arglist[i] = rightList[rightIndex]
            tabulations[id]["swaps"] += 1
            rightIndex += 1
