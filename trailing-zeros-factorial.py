def trailing_zeros(n):
  if n<0:
    return -1
  count=0
  i=5
  while n//i>=1:
    count+=n//i
    i=i*5
  return count
if __name__=='__main__':
  n=int(input("Enter n:"))
  print(trailing_zeros(n))
