''' [Easy]

    Desciption
        Given an array of distinct integers `arr`, find all pairs of elements with the minimum absolute difference of
        any two elements. Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows:
            1. a, b are from arr
            2. a < b
            3. b - a equals to the minimum absolute difference of any two elements in arr

    Input
        arr = [4,2,1,3]
    Output
        [[1,2],[2,3],[3,4]]
    Explanation
        The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
'''


from typing import List
from collections import defaultdict


class Solution1:
    ''' This one is faster. Time complexity is approximately O(nlogn) + O(n),
        and use less memory.
    '''

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result, min_abs_diff = [[arr[0], arr[1]]], arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            j = i + 1
            diff = arr[j] - arr[i]

            if diff > min_abs_diff:
                continue
            elif diff == min_abs_diff:
                result.append([arr[i], arr[j]])
            else:
                result = [[arr[i], arr[j]]]
                min_abs_diff = diff

        return result


class Solution2:
    ''' This one is slower. Time complexity is approximately O(nlogn) + O(n)
        and use more memory
    '''

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)
        d = defaultdict(list)
        min_abs_diff = float("inf")
        for i in range(len(sorted_arr) - 1):
            diff = sorted_arr[i + 1] - sorted_arr[i]
            if diff < min_abs_diff:
                min_abs_diff = diff
            d[diff].append([sorted_arr[i], sorted_arr[i + 1]])

        return d[min_abs_diff]


if __name__ == '__main__':
    sol1 = Solution1()
    sol2 = Solution2()

    arr = [4, 2, 1, 3]
    print(sol1.minimumAbsDifference(arr))
    print(sol2.minimumAbsDifference(arr))
