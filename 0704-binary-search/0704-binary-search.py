class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if mid == lo:
                if nums[lo] == target:
                    return lo
                elif nums[hi] == target:
                    return hi
                else:
                    break
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid
            else:
                lo = mid
        
        return -1