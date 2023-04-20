# given a string of digits 2 to 9 a user has pressed on an old T9 "old school" telephone keypad, return a list of all letter combinations they could have been trying to type. A recursive problem

# t9_letters("23") ->
# ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# t9_letters("4663") ->
# ["gmmd", ..., "gone", ..., "good", ..., "home", ..., "ioof"]

def t9_letters(digits):
    digit_to_letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    if len(digits) == 0:
        return []

    if len(digits) == 1:
        return digit_to_letters[digits]

    current_digit = digits[0]
    remaining_digits = digits[1:]

    result = []
    for letter in digit_to_letters[current_digit]:
        for combination in t9_letters(remaining_digits):
            result.append(letter + combination)

    return result

print(t9_letters("224"))
print(t9_letters("4663"))