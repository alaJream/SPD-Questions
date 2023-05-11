# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

def k_largest_elements(a, k):
    # sorting the array in descending order
    a.sort(reverse=True)
    
    # Returning k elements
    return a[:k]

a = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3

print(k_largest_elements(a, k))  #output: [8, 7, 6]
