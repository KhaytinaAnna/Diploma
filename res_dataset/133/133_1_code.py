def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True
print(below_threshold([1, 2, 3, 4, 10], 11))

# ['>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '!']