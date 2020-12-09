''' [Easy]

    Description
        Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
        If multiple values have the same frequency, sort them in decreasing order.

        Return the sorted array.

    Input
        nums = [2,3,1,3,2]
    Output
        [1,3,3,2,2]
    Explanation
        '1' has the least frequency, '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
'''


from typing import List
from collections import Counter
from functools import cmp_to_key


class Solution1:
    ''' use `cmp_to_key` to wrap the custom `compare` function.

        def cmp_to_key(mycmp):
            class K:
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0
                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0
                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0
                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0
                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0
                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0
            return K
    '''

    def frequencySort(self, nums: List[int]) -> List[int]:

        c = Counter()
        for n in nums:
            c[n] += 1

        def compare(a, b):
            nonlocal c

            if c[a] == c[b]:
                return b - a
            else:
                return c[a] - c[b]

        return sorted(nums, key=cmp_to_key(compare))


class Solution2:
    ''' Since the compare target is :int:,
        a < b <=> -a > -b

        This solution is faster than Solution1.
    '''

    def frequencySort(self, nums: List[int]) -> List[int]:

        c = Counter()
        for n in nums:
            c[n] += 1

        return sorted(nums, key=lambda n: (c[n], -n))


if __name__ == '__main__':
    nums = [2, 3, 1, 3, 2]
    print(Solution1().frequencySort(nums))
    print(Solution2().frequencySort(nums))
