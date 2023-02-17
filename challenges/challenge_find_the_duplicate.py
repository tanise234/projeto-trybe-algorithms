from collections import Counter

def find_duplicate(nums):
    if len(nums) >= 2 and valid(nums):
        repeated = Counter(nums).most_common()
        
        if repeated[1][1] and repeated[1][1] > 1:
            return False

        return repeated[0][0]

    return False


def valid(nums):
    for num in nums:
        if type(num) != int or num <= 1:
            return False
