def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    mid_index = len(word) // 2
    for index in range(mid_index):
        if word[index] != word[-(index + 1)]:
            return False
    return True
