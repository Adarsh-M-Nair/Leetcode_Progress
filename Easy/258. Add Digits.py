def addDigits(self, num: int) -> int:
  if num<10:
    return num
  else:
    while(num>=10):
      temp=num
      s=0
      while(temp>0):
        d=temp%10
        s+=d
        temp//=10
      num=s
    return s

