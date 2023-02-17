from collections import Counter


def find_duplicate(nums):
    if not is_valid(nums):
        return False

    repeated = Counter(nums).most_common()
    if (len(repeated) > 1 and repeated[1][1] > 1) or repeated[0][1] == 1:
        return False

    return repeated[0][0]


def is_valid(nums):
    if len(nums) < 2:
        return False

    for num in nums:
        if type(num) != int or num < 1:
            return False

    return True
