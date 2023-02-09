def is_palindrome_recursive(word: str, low_index: int, high_index: int):
    """Vai retornar verdadeiro caso a palavra seja um palíndromo"""
    try:
        if low_index >= high_index:
            return True
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except Exception:
        return False

