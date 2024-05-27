def job_sequence(profit,deadlines,jobs):
  P=sorted(profit,reverse=True)
  n=len(deadlines)
  m=max(deadlines)
  timeslot=[0]*(m+1)
  for i in range(n):
    k=min(deadlines[i],m)
    while k>=1:
      if timeslot[k] ==0:
        timeslot[k]+=P[i]
        job=jobs[i]
        break
      else:
        k-=1
  total=sum(timeslot)
  return total
j = job_sequence([200, 180, 190, 300, 120, 100], [5, 3, 3, 2, 4, 2], ["j1", "j2", "j3", "j4", "j5", "j6"])
print(j)
