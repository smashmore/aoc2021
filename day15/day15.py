from pprint import pprint
with open("input") as w:
  m = {}
  cost={}
  i=0
  for l in w.readlines():
    l =l.strip()
    for j in range(0,len(l)):
      m[(i,j)] = int(l[j])
    i+=1
  points = [(i-1,j)]
  cost[(i-1,j)] =0
  index =0
  max_i = i-1
  max_j = j
  while len(points) > 0:
    index +=1
    (x,y) =points.pop()
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
    points.sort()
  pprint(index)
  pprint(cost[(0,0)])




