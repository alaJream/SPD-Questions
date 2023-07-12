
# There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

# multiply the number on display by 2, or
# subtract 1 from the number on display.
# Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

# Example:
# Input: startValue = 2, target = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        while target > startValue:
            operations += target % 2 + 1  # add 2 if target is odd, 1 if even
            target = (target + 1) // 2
        return operations + startValue - target
