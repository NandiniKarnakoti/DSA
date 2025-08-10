def power(n):
  def sign(x):
    return ''.join(sorted(str(x)))
  powers_of_two={sign(1<<i) for i in range(31)}
  return sign(n) in powers_of_two
if __name__=='__main__':
  n=int(input())
  print("YES" if power(n) else "NO")
