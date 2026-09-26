def count_occurrences(phrase: str, letter: str) -> int:
    n = 0
    for i in range(len(phrase)):
        char = phrase[i]
        if char == letter:
            n += 1
    return n


