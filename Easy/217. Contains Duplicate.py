def containsDuplicate(slef, nums: List[int]) -> bool: # type: ignore
  if len(set(nums))==len(nums):
    return False
  else:
    return True