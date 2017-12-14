def Bubble_Sort(collection, tabulations,leastToGreatest=True):
    """
    Sort contents of list by reference
        bubble sort is the least efficient sorting algorithm
        complexity O(n**2)
    """
    id = "bubbleSort"
    complete = False
    if leastToGreatest:
        order = "collection[i] > collection[i+1]"
    else:
        order = "collection[i] < collection[i+1]"
    while not complete:
        complete = True
        for i in range(len(collection)-1):
            tabulations[id]["comparisons"] += 1
            if eval(order):
                tabulations[id]["swaps"] += 1
                collection[i], collection[i+1] = collection[i+1],collection[i]
                complete = False
