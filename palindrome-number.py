def isPal(n):
  temp=n
  rev=0
  while temp>0:
    d=temp%10
    rev=rev*10+d
    temp=temp//10
  return rev==n
if __name__=='__main__':
  n=int(input("Enter n:"))
  print(isPal(n))
    
