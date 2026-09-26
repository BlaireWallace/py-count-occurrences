def count_occurrences(phrase: str, letter: str) -> int:
    n = 0
    for i in range(len(phrase)):
        char = str.lower(phrase[i])
        if char == str.lower(letter):
            n += 1
    return n


