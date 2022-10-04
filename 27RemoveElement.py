from os import remove


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    try:
        while(True):
            nums.remove(val)
    except ValueError:
        pass

removeElement([2,2,3,3], 3)