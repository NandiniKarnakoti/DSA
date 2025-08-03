#Naive Approach
def lcm(a,b):
  res=max(a,b)
  while True:
    if res%a==0 and res%b==0:
      return res
    res+=1
if __name__=='__main__':
  a,b=map(int,input().split())
  print(lcm(a,b))
#Efficient Solution
#We know that a*b=gcd(a,b)*lcm(a,b)
def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)
def lcm(a,b):
  return a*b//gcd(a,b)
if __name__=='__main__':
  a,b=map(int,input().split())
  print(lcm(a,b))
  

  
