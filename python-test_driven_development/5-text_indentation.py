#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ['.', '?', ':']:
            result += "\n\n"

            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1

    for line in result.split('\n'):
        print(line.strip())


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/5-text_indentation.txt", verbose=True)
