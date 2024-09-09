#!/usr/bin/python3
""" is Anagram module """


def isAnagram(self, s: str, t: str) -> bool:
    """
    we will try to find if the s word has the same letters of t word
    by storing the number of occurrences of the letter and after that
    we will iterate over the word t and if the letter exists we will
    decrease the number of occurrences of that letter by one
    after that we will check if the number of occurrences of all letter is 0
    or not if 0 it means that word s has the same letters of word t
    """
    if len(s) != len(t):
        return False

    words_hash_map = {}

    for index in range(0, len(s)):
        try:
            words_hash_map[s[index]] += 1
        except KeyError:
            words_hash_map[s[index]] = 1

    for letter in t:
        try:
            words_hash_map[letter] -= 1
        except:
            return False

    for key in words_hash_map:
        if words_hash_map[key] != 0:
            return False
    return True
