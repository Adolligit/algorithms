def quicksort(list):
    if not list:
        return []
    return (
        quicksort([x for x in list[1:] if x < list[0]])
            + [list[0]] +
        quicksort([x for x in list[1:] if x >= list[0]])
    )


def is_anagram(first_string, second_string):
    """Meu código seŕa feito aqui"""
