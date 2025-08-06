#Naive Approach
def isPrime(x):
  for i in range(2,x):
    if x%i==0:
      return False
  return True
def primeFactors(n):
  for i in range(2,n+1):
    if isPrime(i):
      x=i
      while n%x==0:
        print(i)
      x=x*i
if __name__=='__main__':
  n=int(input())
  print(primeFactors(n))
