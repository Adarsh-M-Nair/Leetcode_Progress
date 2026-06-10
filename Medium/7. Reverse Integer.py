def reverse(self, x: int) -> int:
  rev=0
  if x<0:
    s=str(x)
    rev=1*int(s[::-1])
  else:
    while x>0:
      d=x%10
      rev=rev*10+d
      x//=10
  if rev>=(-2)**31 and rev<=(2)**31-1:
    return rev
  else:
    return 0