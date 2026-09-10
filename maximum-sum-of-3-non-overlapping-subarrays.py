from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        num_windows = n - k + 1

        # sums[i] = sum of the window starting at index i, length k
        sums = [0] * num_windows
        window_sum = sum(nums[:k])
        sums[0] = window_sum
        for i in range(1, num_windows):
            window_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = window_sum

        # left[i] = the starting index (in sums) of the best window in sums[0..i]
        # ties broken by choosing the leftmost (smallest index)
        left = [0] * num_windows
        best = 0
        for i in range(num_windows):
            if sums[i] > sums[best]:
                best = i
            left[i] = best

        # right[i] = the starting index (in sums) of the best window in sums[i..end]
        # ties broken by choosing the leftmost (smallest index) as well,
        # since that keeps the overall triple lexicographically smallest
        right = [0] * num_windows
        best = num_windows - 1
        for i in range(num_windows - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best

        # Try every possible middle window start j, look up the best
        # non-overlapping left and right windows around it
        max_total = -1
        result = [0, 0, 0]

        for j in range(k, num_windows - k):
            l = left[j - k]
            r = right[j + k]
            total = sums[l] + sums[j] + sums[r]
            if total > max_total:
                max_total = total
                result = [l, j, r]

        return result