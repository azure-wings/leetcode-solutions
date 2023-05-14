class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size = len(nums)
        def next_elem(idx: int) -> int:
            return (idx + nums[idx]) % size
        
        for i in range(size):
            fast = slow = i

            while True:
                fast = next_elem(next_elem(fast))
                slow = next_elem(slow)
                if fast == slow:
                    break

            if next_elem(fast) == fast:
                continue
            else:
                while True:
                    fast = next_elem(fast)
                    if nums[fast] * nums[slow] < 0:
                        break
                    if fast == slow:
                        return True
                    
        return False