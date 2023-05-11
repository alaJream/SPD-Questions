# Merge `M` sorted lists of variable length
# Google Translate Icon
# Given M sorted lists of variable length, merge them efficiently in sorted order.

# For example,

# Input:  4 sorted lists of variable length
 
# [10, 20, 30, 40]
# [15, 25, 35]
# [27, 29, 37, 48, 93]
# [32, 33]
 
# Output:
 
# [10, 15, 20, 25, 27, 29, 30, 32, 33, 35, 37, 40, 48, 93]


import heapq

def merge_sorted_lists(lists):
    merged_list = []
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)
        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1], list_ind, element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

lists = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
print(merge_sorted_lists(lists))
