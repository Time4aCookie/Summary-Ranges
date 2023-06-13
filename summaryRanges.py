class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        # handling 2 corner cases
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        ans = []
        first = 0
        last = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                last = i
            elif last == first:
                ans.append(str(nums[i - 1]))
                first = i
                last = i
            else:
                ans.append(f"{nums[first]}->{nums[last]}")
                first = i
                last = i
            if i == len(nums) - 1:
                if nums[i] == nums[i - 1] + 1:
                    ans.append(f"{nums[first]}->{nums[last]}")
                else:
                    ans.append(str(nums[i]))
        return ans



