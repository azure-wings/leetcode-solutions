class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        curr_contained: Defaultdict[int, int] = defaultdict(int)
        nonzero_elems: Set[int] = set()
        left: int = 0

        curr_contained[fruits[left]] += 1
        nonzero_elems.add(fruits[left])
        maxfruits: int = 1
        currfruits: int = 1

        for right in range(1, len(fruits)):
            curr_contained[fruits[right]] += 1
            nonzero_elems.add(fruits[right])
            currfruits += 1

            while len(nonzero_elems) > 2:
                curr_contained[fruits[left]] -= 1
                currfruits -= 1
                if curr_contained[fruits[left]] == 0:
                    nonzero_elems.remove(fruits[left])
                left += 1
                
            maxfruits = max(maxfruits, currfruits)

        return maxfruits
