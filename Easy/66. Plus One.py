def plusOne(self, digit:List[int])-> List[int]:  # type: ignore
  s=""
  l=[]
  for i in digit:
    s+=str(i)
  n=int(s)+1
  for i in str(n):
    l.append(int(i))
  return l
