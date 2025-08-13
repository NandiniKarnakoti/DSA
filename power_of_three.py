def pow_three(n):
  if n<=0:
    return False
  while n%3==0:
    n=n//3
  return n==1
if __name__=='__main__':
  n=int(input("Enter a number:"))
  print("True" if pow_three(n) else "False")
