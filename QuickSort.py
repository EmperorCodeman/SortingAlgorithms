'''
O(n**2)
all elements > last element: to right
all element < last element: to left
last element moved between them
recurse on left and right
append results and return
'''
def QuickSort(collection, tabulations, id="quickSort"):
    #written for readability not speed
    size = len(collection)
    tabulations[id]["comparisons"] += 1
    if size <= 1:
        return collection
    pivot = collection[size-1]
    collectionMinusPivot = collection[:size-1]
    lessThenPivot, greaterThenPivot = [],[]
    for element in collectionMinusPivot:
        if element < pivot:
            lessThenPivot.append(element)
        else:
            greaterThenPivot.append(element)
    #sort left and right sides
    lessThenPivot = QuickSort(lessThenPivot, tabulations, id)
    greaterThenPivot = QuickSort(greaterThenPivot, tabulations, id)
    return lessThenPivot + [pivot] + greaterThenPivot
def ModifiedQuickSort(collection, tabulations):
    tabulations["modifiedQuickSort"]["comparisons"] += 1
    if len(collection) > 1:
        midPoint = collection.__len__() // 2
        tabulations["modifiedQuickSort"]["swaps"] += 1
        collection[0],collection[midPoint] = collection[midPoint], collection[0]
        collection = QuickSort(collection, tabulations, "modifiedQuickSort")
    return collection
