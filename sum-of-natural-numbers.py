#Naive Approach
n=int(input()
sum_val=0
for i in range(n):
  sum_val+=i
print(sum_val)
#Efficient Solution
n=int(input()
val=0
for i in range(1,n):
  for j in range(1,i):
    val+=1
print(val)
#Optimized Approach
n=int(input("Enter a number:"))
print(n*(n+1)//2)

