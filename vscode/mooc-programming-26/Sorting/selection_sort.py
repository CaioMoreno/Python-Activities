def selection_sort(items: list):
    for i in range(len(items)):
        item_index = i
        for j in range(i+1, len(items)):
            if items[j] < items[item_index]:
                item_index = j

        if item_index != i:
            item = items[i]
            items[i] = items[item_index]
            items[item_index] = item

    return items

print(selection_sort([33, 1, 89, 2, 67, 245]))
