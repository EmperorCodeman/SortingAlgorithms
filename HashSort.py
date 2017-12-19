#O(n**2)
def HashSort(collection, tabulations):
    id = "hashSort"
    #start at first possible value, every time it occures increment counter in list with index as its value
    len = collection.__len__()
    occurences = [0] * len
    for i in range(len):
        #if i is greater then list size -1 then this algorithm will not work
        if collection[i] > (len - 1):
            raise Exception("Error in Hash sort: list element has greater value then size - 1")
            return []
        for element in collection:
            #n^2 for everytime i is in l store occurence in sortedList
            tabulations[id]["comparisons"] += 1
            if element == i:
                occurences[i] += 1
    sortedPosition = 0
    #sort originalList with above described list
    for number in range(len):
        for numberOfOccurences in range(occurences[number]):
            collection[sortedPosition] = number
            tabulations[id]["swaps"] += 1
            sortedPosition += 1
    return collection
