def is_palindrome_iterative(word):
    if not word:
        return False
    for i in range(len(word)):
        print(word[i])
        
is_palindrome_iterative('ana')