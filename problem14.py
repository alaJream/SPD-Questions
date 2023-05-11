# Replace all non-overlapping occurrences of a pattern
# Google Translate Icon
# Given a string and a pattern, in-place replace all non-overlapping occurrences of the pattern in the string by a specified character.

# 1st Variant: Replace each occurrence of the pattern
# Input:
 
# String = “ABCABCXABC”;
# Pattern = “ABC”;
# Character = ‘@’;
 
# Output: @@X@

def replace_string(input_string, pattern, char):
    return input_string.replace(pattern, char)

input_string = "ABCABCXABC"
pattern = "ABC"
char = '@'
print(replace_string(input_string, pattern, char))
