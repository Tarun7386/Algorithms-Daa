def place(x,row,col):
  for r in range(1,row):
    if x[r]==col or abs(x[r]-col)==abs(r-row):
      return False
  return True

def n_queen(x,row,n):
  for col in range(1,n+1):
    if place(x,row,col)==1:
      x[row]=col
      if row==n:
        return x[1:n+1]
      else:
        result=n_queen(x,row+1,n)
        if result:
          return result
  return None

def solve_n_queen(n):
  x=[0]*(n+1)
  solution=n_queen(x,1,n)
  if solution:
    return solution
  else:
    return "solution does not exist"
solution = solve_n_queen(4)
if isinstance(solution, list):
  print("A solution exists:")
  print(solution)
else:
  print(solution)
