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
  pprint(m)
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
  points = []
  for i in range(0, end_i +1):
    points.append((i,0))
  for j in range(0, end_j +1):
    points.append((end_i, j))
  points.reverse()
  cost[(end_i,end_j)] =0
  while len(points) > 0:
    if index % 10 == 0:
      pm = []
      for j in range(0, end_j+1):
        row =[]
        for i in range(0, end_i +1):
          c = ' '
          if (i,j) in cost:
            c = '*'
          row.append(c)
        rs = ''.join(row).strip()
        if rs == "":
          continue
        pm.append(rs)
      pprint(pm)
    index +=1
    (x,y) =points.pop(0)
    if (x,y) == (0,0):
      continue
    c = m[(x,y)] +cost[(x,y)]
    if (0,0) in cost and c > cost[(0,0)]:
      continue
    for i in range(x-1, x+2):
      if (i,y) not in m:
        continue
      if (i,y) not in cost or cost[(i,y)] > c:
        cost[(i,y)] = c
        points.append((i,y))
    for j in range(y-1, y+2):
      if (x,j) not in m:
        continue
      if (x,j) not in cost or cost[(x,j)] > c:
        cost[(x,j)] = c
        points.append((x,j))
  pprint(cost[(0,0)])
  pprint(m[(end_i,end_j)])




