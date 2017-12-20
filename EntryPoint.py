from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
def test(iterations=1000,debug=False):
    if debug:
        seed(10)
    case = [randrange(0, 7) for x in range(7)]
    testCase = case[:]
    testCase.sort()
    failure = []
    import sys
    sys.setrecursionlimit(12000)
    for test in range(iterations):
        Bubble_Sort(case,tabulations)
        failure.append(case == testCase)
        shuffle(case)
        Shaker_Sort(case,tabulations)
        failure.append(case==testCase)
        shuffle(case)
        SelectionSort(case, tabulations)
        failure.append(case == testCase)
        shuffle(case)
        #QuickSort(case, tabulations)
        #failure.append(case == testCase)
        shuffle(case)
        #ModifiedQuickSort(case, tabulations)
        #failure.append(case == testCase)
        shuffle(case)
        HashSort(case, tabulations)
        failure.append(case == testCase)
        shuffle(case)
        MergeSort(case, tabulations)
        failure.append(case == testCase)

    if False in failure:
        print(False)
    else:
        print(True)
metrics = {"comparisons":0,"swaps":0}
tabulations = {"bubbleSort":metrics,
               "shakerSort":metrics,
               "selectionSort":metrics,
               "quickSort":metrics,
               "modifiedQuickSort":metrics,
               "mergeSort":metrics,
               "hashSort": metrics}

test()


