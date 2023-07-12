# Find all n-digit binary numbers with an equal sum of bits in their two halves
# Google Translate Icon
# Find all n–digit binary numbers with an equal sum of left and right half, where n varies from 1 to 9 and the binary number should not start with 0.

# For example,

# 6–digit numbers with an equal sum of left and right half
 
# 100001 100010 101011 110011 100100 101101 101110 110101 110110 111111
 
 
# 7–digit numbers with an equal sum of left and right half (middle element can be 0 or 1 for odd numbers)
 
# 1000001 1001001 1000010 1001010 1010011 1011011 1100011 1101011 1000100 1001100 1010101 1011101 1010110 1011110 1100101 1101101 1100110 1101110 1110111 1111111

def print_binary(n, l, r, diff):
    if n == 0:
        if diff == 0:
            print(l + r)
        return
    if n % 2 == 0:
        print_binary(n - 1, l + '1', r + '0', diff - 1)
        print_binary(n - 1, l + '0', r + '1', diff + 1)
    else:
        print_binary(n - 1, l + '0', r, diff + 1)
        print_binary(n - 1, l + '1', r, diff - 1)

n = 6
print_binary(n, '', '', 0)
