def singleNumber(slef, nums: List[int])-> int:  # type: ignore
  for i in nums:
    if nums.count(i)==1:
      return i
    