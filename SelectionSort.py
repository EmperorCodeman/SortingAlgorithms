"""Selection sort selects a element then iterates till selected compares less then and swaps, at end of each
inner loop selected element is appended to ordered list and so on
Forms show O(n**2) but I think it should be O(!n-1)
"""
def SelectionSort(collection, tabulations):
    id = "selectionSort"
    length = len(collection)
    for leftOfIsSorted in range(length - 1):#last element implicitly sorted
        selected = collection[leftOfIsSorted]
        for ii in range(leftOfIsSorted+1,length):
            tabulations[id]["comparisons"] += 1
            if collection[ii] < selected:
                tabulations[id]["swaps"] += 1
                collection[ii], selected = selected, collection[ii]
        collection[leftOfIsSorted] = selected
