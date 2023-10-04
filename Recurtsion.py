def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(4)

def recursion(n):
  if n==1:
    return 1
  else:
    return n*recursion(n-1)
print(recursion(4))