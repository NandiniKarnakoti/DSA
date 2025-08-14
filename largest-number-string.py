def largestNumber(num):
  res=''
  for i in range(len(num)-2):
    sub=num[i:i+3]
    if len(set(sub))==1:
      if sub>res:
        res=sub
  return res
