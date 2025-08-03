#Euclidean Algorithm
def gcd(a,b):
  while a!=b:
    if a>b:
      a=a-b
    else:
      b=b-a
  return a
if __name__=='__main__':
  a,b=map(int,input().split())
  print(gcd(a,b))
#Optimized Euclidean Algorithm
def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)
if __name__=='__main__':
  a,b=map(int,input().split())
  print(gcd(a,b))
