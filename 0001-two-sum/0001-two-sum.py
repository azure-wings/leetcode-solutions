class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx: Dict[int, int] = dict()
    
        for i, n in enumerate(nums):
            if target-n in idx:
                return [i, idx[target-n]]
            else:
                idx[n] = i
                