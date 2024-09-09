#!/usr/bin/python3
""" contains Duplicate module """


def containsDuplicate(self, nums):
    """ 
    we will try to find the duplicate number in the list nums
    so we will use set because set as hashmap for us first we check
    if the element exists in the set or not if it exists we will return True
    if not we add it to are list and in case there no duplicates
    in the list of numbers we will return False
    in the end set will have all distinct number from the list nums
    """
    sete = set()
    for item in nums:
        if item in sete:
            return True
        else:
            sete.add(item)
    return False
