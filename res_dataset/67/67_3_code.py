def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)
print(is_bored("I am happy. What happened! I won. He found something. I see? I understand. I think therefore I am."))

# ['>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>', '>']