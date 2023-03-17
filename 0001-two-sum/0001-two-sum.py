class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx: Dict[int, int] = dict()
        for i, n in enumerate(nums):
            if n not in idx:
                idx[n] = []
            idx[n].append(i)

        for k in idx:
            if target-k in idx:
                if k == target-k and len(idx[k]) > 1:
                    return idx[k]
                elif k != target-k:
                    return [idx[k][0], idx[target-k][0]]
                else:
                    continue
                