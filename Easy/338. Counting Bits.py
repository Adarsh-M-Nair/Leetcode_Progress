def countBits(self, n: int) -> List[int]: # type: ignore
  ans=[]
  for i in range(n+1):
    b=bin(i)
    s=0
    for i in b[2:]:
      s+=int(i)
    ans.append(s)
  return ans