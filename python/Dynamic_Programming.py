def fib (n):
  if n < 3:
    return 1
  else:
    return (fib(n - 1) + fib (n - 2))

#print(fib(40))

def new_fib(n):
  if n < 3:
    return 1
  else:
    prev_prev = 1
    prev = 1

    for i in range (3, n+1):
      new = prev + prev_prev
      prev_prev = prev
      prev = new
    return new

print(new_fib(40))