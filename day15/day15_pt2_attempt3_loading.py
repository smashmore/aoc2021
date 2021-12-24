from pprint import pprint
from collections import defaultdict
with open("input") as w:
  m = {}
  cost={}
  j=0
  for l in w.readlines():
    l =l.strip()
    for i in range(0,len(l)):
      m[(i,j)] = int(l[i])
    j+=1
  index =0
  max_i = i +1
  max_j = j
  for i5 in range(0,5):
    for j5 in range(0,5):
      if i5 ==0 and j5==0:
        continue
      for i in range(0,max_i):
        for j in range(0,max_j):
          val =  (((m[(i,j)] + i5 +j5) -1 ) %9) +1
          m[(i5*max_i+i, j5*max_j+j)] = val
  end_i = 5*max_i -1
  end_j = 5*max_j -1
  points = defaultdict(list)
  points[None].append((end_i, end_j))
  cost[(end_i,end_j)] =0
  minkey = None
