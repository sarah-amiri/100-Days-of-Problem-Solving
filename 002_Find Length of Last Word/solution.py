"""
    This problem is available on LeetCode.
    You can see the complete problem here:
    https://leetcode.com/problems/length-of-last-word/

    The problem asked to find length of the last word in a string
    that may have unknown number of spaces.
    I used two solutions for this problem:
        1) Use a custom way to split words and delete spaces.
        2) Use python split method to split words.
    Second approach is faster.
"""


def find_last_word(term):
    start, end = 0, 0
    words = []
    while end < len(term):
        while term[start] == ' ':
            start += 1
            if start == len(term):
                break

        end = start
        while end != len(term) and term[end] != ' ':
            end += 1

        if start != end:
            words.append(term[start:end])
        start = end

    return words


def length_of_last_word_1(term):
    words = find_last_word(term)
    return len(words[-1])


def length_of_last_word_2(term):
    words = term.split()
    return len(words[-1])


if __name__ == '__main__':
    # example 1
    s = "Hello World"
    print(length_of_last_word_1(s))
    print(length_of_last_word_2(s))

    # example 2
    s = "   fly me   to   the moon  "
    print(length_of_last_word_1(s))
    print(length_of_last_word_2(s))

    # example 3
    s = "fluffy is still joyboy"
    print(length_of_last_word_1(s))
    print(length_of_last_word_2(s))
