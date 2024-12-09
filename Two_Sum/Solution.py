class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = []
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target and s == [] and i != j:
                    s.append(i)
                    s.append(j)
        return s
