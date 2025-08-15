#Division Method
def isPowerOfFour(n):
  if n<=0:
    return False
  while n%4==0:
    n=n//4
  return n==1

#Logarithmic Approach
import math
def isPowerOfFour(n):
  if n<=0:
    return False
  logs=math.log(n,4)
  return 4**round(logs)==n
if __name__=="__main__":
  n=int(input("Enter n:"))
  print("Yes" if isPowerOfFour(n) else "No")

  
