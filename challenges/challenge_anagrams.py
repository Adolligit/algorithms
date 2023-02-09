def quicksort(word):
    if not word:
        return word
    return (
        quicksort([char for char in word[1:] if char < word[0]])
        + [word[0]] +
        quicksort([char for char in word[1:] if char >= word[0]])
    )


def is_anagram(first_string, second_string):
    """Retornará verdadeiro caso as palavras sejam anagramas"""
    first = quicksort(first_string.lower())
    second = quicksort(second_string.lower())

    if not first_string or not second_string:
        return ("".join(first), "".join(second), False)
    if first != second:
        return ("".join(first), "".join(second), False)
    else:
        return ("".join(first), "".join(second), True)
