def is_palindrome_recursive(word: str, low_index: int, high_index: int):
    """Vai retornar verdadeiro caso a palavra seja um palíndromo"""
    if len(word) <= 0:
        return False
    if low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

