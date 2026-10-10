def count_characters(text):
    result = {"letters": 0, "numbers": 0, "spaces": 0, "special": 0}
    for ch in text:
        if ch.isalpha():               # a-z and A-Z
            result["letters"] += 1
        elif ch.isdigit():             # each digit counts once, so "12" is 2 numbers
            result["numbers"] += 1
        elif ch == " ":
            result["spaces"] += 1
        else:                          # everything else: punctuation, symbols, tabs
            result["special"] += 1
    return result