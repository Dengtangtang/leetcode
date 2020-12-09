''' [Easy]

    Description
        Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
        A lucky number is an element of the matrix such that it is the minimum element in its row
        and maximum in its column.

    Input
        matrix = [[3,7,8],[9,11,13],[15,16,17]]
    Output
        [15]

    Hint
        for 2-d array (matrix), you can retrieve columns by `zip(*matrix)`
'''


from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_values = {min(r) for r in matrix}
        max_values = {max(c) for c in zip(*matrix)}

        return list(min_values & max_values)


if __name__ == '__main__':
    sol = Solution()
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    ans = sol.luckyNumbers(matrix)
    print(ans)
