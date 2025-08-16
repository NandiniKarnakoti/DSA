def maxNumber(n):
  val=list(str(n))
  for i, ch in enumerate(val):
    if ch=='6':
      val[i]='9'
      break
  return int(''.join(val))
if __name__=='__main__':
  n=int(input("Enter n:"))
  print(maxNumber(n))
