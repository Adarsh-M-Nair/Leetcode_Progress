def addBinary(self, a:str, b:str) -> str:
  sums=int(a,2)+int(b,2)
  bina=bin(sums)
  return bina[2:]