class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = Counter(nums)
        print("Counts:", hash)  # Debugging line
        for value in hash.values():
            if value >= 2:
                return True
        
        return False