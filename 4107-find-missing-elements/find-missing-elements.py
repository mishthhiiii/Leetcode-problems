class Solution:
    def findMissingElements(self, nums):
        mini = min(nums)
        maxi = max(nums)

        present = set(nums)

        ans = []

        for i in range(mini + 1, maxi):
            if i not in present:
                ans.append(i)

        return ans