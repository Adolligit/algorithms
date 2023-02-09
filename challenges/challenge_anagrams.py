def quicksort(word):
    if not word:
        return []
    return (
        quicksort([char for char in word[1:] if char < word[0]])
        + [word[0]] +
        quicksort([char for char in word[1:] if char >= word[0]])
    )


def is_anagram(first_string, second_string):
    first_string_sorted = quicksort(first_string.lower())
    second_string_sorted = quicksort(second_string.lower())

    if not first_string or not second_string:
        return ("".join(first_string_sorted), "".join(second_string_sorted), False)
    if first_string_sorted != second_string_sorted:
        return ("".join(first_string_sorted), "".join(second_string_sorted), False)
    else:
        return ("".join(first_string_sorted), "".join(second_string_sorted), True)
