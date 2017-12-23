'''
O(nlog(n))
'''
def MergeSort(arglist, tabulations):
    id = "mergeSort"
    tabulations[id]["comparisons"] += 1
    if len(arglist) <= 1:
        #return from recursion
        return
    midPoint = len(arglist) // 2
    leftList = arglist[:midPoint]
    rightList = arglist[midPoint:]
    #Sort the left and right side recursively.
    MergeSort(leftList, tabulations)
    MergeSort(rightList, tabulations)
    #left and right are now sorted, sort them into mother list
    for i in range(len(arglist)):
        tabulations[id]["comparisons"] += 1
        if len(rightList) != 0 and len(leftList) != 0:
            tabulations[id]["comparisons"] += 1
            tabulations[id]["swaps"] += 1
            if rightList[0] < leftList[0]:
                arglist[i] = rightList.pop(0)
            else:
                arglist[i] = leftList.pop(0)
        else:
            for leftOver in leftList+rightList:
                tabulations[id]["swaps"] += 1
                arglist[i] = leftOver
                i += 1
            return
