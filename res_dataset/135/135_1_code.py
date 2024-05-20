def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return set(s0) == set(s1)
print(same_chars(```python
same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
same_chars('abcd', 'dddddddabc')
same_chars('dddddddabc', 'abcd')
same_chars('eabcd', 'dddddddabc')
same_chars('abcd', 'dddddddabce')
same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
```))

# ['>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>']