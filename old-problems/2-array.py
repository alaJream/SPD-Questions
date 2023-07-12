# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

def closest_sum_pair(a, b, t):
    closest_pair = (None, None)
    diff = float('inf')
    
    for i in a:
        for j in b:
            if abs(i + j - t) < diff:
                diff = abs(i + j - t)
                closest_pair = (i, j)
    
    return closest_pair

a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
t = 20

print(closest_sum_pair(a, b, t)) 
