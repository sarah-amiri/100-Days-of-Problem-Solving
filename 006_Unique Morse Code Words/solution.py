"""
    This problem is available on LeetCode.
    You can see the complete problem here:
    https://leetcode.com/problems/unique-morse-code-words/

    The problem asked to transform a list of words to International Morse Code
    and return number of different transformations.

    I also found this approach useful:
    '''
        def uniqueMorseRepresentations(self, words: List[str]) -> int:
            morse, a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."], ord('a')
            return len(set(["".join(morse[ord(c) - a] for c in word) for word in words]))
    '''
"""
from typing import List


INTERNATION_MORSE_CODE_CODING = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--.."
]

ENGLISH_LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


class Solution:
    def __init__(self):
        self.letters_mapping = {
            ENGLISH_LETTERS[i]: INTERNATION_MORSE_CODE_CODING[i]
            for i in range(len(ENGLISH_LETTERS))
        }

    def transform(self, word: str):
        return ''.join(self.letters_mapping[w] for w in word)

    def unique_morse_representations(self, words: List[str]) -> int:
        transformations = [self.transform(word) for word in words]
        return len(set(transformations))


if __name__ == '__main__':
    solution = Solution()

    # example 1
    words = ["gin", "zen", "gig", "msg"]
    print('Output: ', solution.unique_morse_representations(words))

    # example 2
    words = ["a"]
    print('Output: ', solution.unique_morse_representations(words))
