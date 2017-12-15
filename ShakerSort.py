"""
Shaker sort
Complexity O(n**2)
Shakersort is a bidirectional version of bubble sort.
Go from left to right, then right to left, till ordered, each cycle reducing the range by 2
"""
def Shaker_Sort(collection, tabulations):
    id = "shakerSort"
    leftBound = 0
    rightBound = len(collection)
    while leftBound < rightBound:
        tabulations[id]["comparisons"] += 1
        #left to right
        for i in range(leftBound, rightBound-1):
            tabulations[id]["comparisons"] += 1
            if collection[i] > collection[i+1]:
                tabulations[id]["swaps"] += 1
                collection[i], collection[i+1] = collection[i+1],collection[i]
        rightBound -= 1
        #right to left
        for i in reversed(range(leftBound+1, rightBound)):
            tabulations[id]["comparisons"] += 1
            if collection[i] < collection[i-1]:
                tabulations[id]["swaps"] += 1
                collection[i],collection[i-1] = collection[i - 1],collection[i]
        leftBound += 1
