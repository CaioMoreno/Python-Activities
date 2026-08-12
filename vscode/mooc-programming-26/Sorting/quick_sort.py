def quick_sort(array: list):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    less = [l for l in array if l < pivot]
    equal = [l for l in array if l == pivot]
    greater = [l for l in array if l > pivot]

    less = quick_sort(less)
    greater = quick_sort(greater)

    return less + equal + greater

  
n = [5, 2, 8, 3, 7, 1, 6]
print(quick_sort(n))
