def is_palindrome_iterative(word):
    if not word:
        return False

    for i in range(len(word)):
        if word[i] == word[-i -1]:
            return True
    return False
        
is_palindrome_iterative('ana')