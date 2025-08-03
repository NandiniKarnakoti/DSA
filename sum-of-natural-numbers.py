#Naive Approach
n=int(input())
sum_val=0
for i in range(n+1):
  sum_val+=i
print(sum_val)
#Another Approach
n=int(input())
val=0
for i in range(1,n+1):
  for j in range(i):
    val+=1
print(val)
#Optimized Approach
n=int(input("Enter a number:"))
print(n*(n+1)//2)

