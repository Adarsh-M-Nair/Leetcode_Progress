def missingNumber(self, nums: List[int]) -> int: # type: ignore
  for i in range(len(nums)+1):
    if i not in nums:
      return i
    
#OR
#O(n) time and O(1) space
def missingNumber(self, nums: List[int]) -> int: # type: ignore
  n=len(nums)
  expected_sum=n*(n+1)//2
  actual_sum=sum(nums)
  return expected_sum-actual_sum