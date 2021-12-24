from pprint import pprint
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
  points= [(end_i, end_j)]
  cost[(end_i,end_j)] =0



  while len(points) > 0:
    (x,y) =points.pop(0)
    #print(index, (x,y), len(points))
    #if index % 10 == 0:
    #  for j in range(0, end_j+1):
    #    row =[]
    #    for i in range(0, end_i +1):
    #      c = ' '
    #      if (i,j) in points:
    #        c = '*'
    #      #c = cost[(i,j)]
    #      row.append(c)
    #    rs = ''.join(row)
    #    print(rs)
    index +=1
    if (x,y) == (0,0):
      continue
    c = m[(x,y)] +cost[(x,y)]
    if (0,0) in cost and c > cost[(0,0)]:
      continue
    checkpoints = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    for i,j in checkpoints:
      if i < 0 or j < 0:
        continue
      if i > end_i or j > end_j:
        continue
      if (i,j) not in cost:
        #print(i,j,c,None)
        cost[(i,j)] = c
        points.append((i,j))
        if (i,j) not in points:
          points.append((i,j))
      elif cost[(i,j)] > c:
        #print(i,j,c,cost[(i,j)])
        cost[(i,j)] = c
        if (i,j) not in points:
          points.append((i,j))
    points = sorted(set(points), key=lambda x: 0 if x not in cost else cost[x])
  print("$$$$$$$$$$")
  pprint(cost[(0,0)])




