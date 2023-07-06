class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = set(nums)
        l = list(k)
        l.sort()
        c = 0
        for i in l:
            nums[c] = i
            c+=1
        return len(k)