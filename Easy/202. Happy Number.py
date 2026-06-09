def isHappy(self, n:int)->bool:
  seen = set()

  while n!=1 and n not in seen:
    seen.add(n)
    current_sum__of_squares = 0
    temp = n
    while temp>0:
      digit = temp%10
      current_sum_of_squares+=digit**2
      temp//=10
    n=current_sum_of_squares
  
  return n==1