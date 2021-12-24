import collections
import math
class grid():
    def __init__(self, pos, cost=None, move_train=None):
        self.curcost = 0
        self.pos = pos
        self.move_train = []
        if cost is not None:
            self.curcost = cost
        if move_train is not None:
            self.move_train = move_train
        self.make_key()

    def get_char(self,x,y):
        for k,v in self.pos.items():
            if v[0] == x and v[1] ==y:
                return k
        if x ==0:
            return "#"
        if y ==0: 
            return "#"
        if x ==4 :
            return "#"
        if y == 12:
            return "#"
        if x ==1:
            if y == 3 or y ==5 or y ==7 or y ==9:
                return '`'
            return '.'
        if y == 3 or y ==5 or y ==7 or y ==9:
            return '.'
        return '#'


    def str(self):
        for i in range(0,4):
            for j in range(0,12):
                print(self.get_char(i,j), end='')
            print()

    def make_pos(grid):
        seen_chars ={}
        pos = {}
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                c = grid[i][j]
                if c.isalpha():
                    if c in seen_chars:
                        c=c.lower()
                    seen_chars[c]=True
                    pos[c] = (i,j)
        return pos



    def make_key(self):
        key = 0
        for start in 'ABCDabcd':
            x,y = self.pos[start]
            key = key * 60 + x * 12 +y 
        self.in_key =key

    def key(self):
        return self.in_key

    def possible_moves(self, c):
        x,y = self.pos[c]
        moves = []
        possible = [(x-1,y), (x+1,y), (x,y-1), (x, y+1)]
        ignore = [(x,y)]
        dist = {}
        for p in possible:
            dist[p] = 1

        while len(possible) > 0:
            p = possible.pop(0)
            if p in moves:
                continue
            if p in ignore:
                continue
            d = dist[p]
            i,j = p[0], p[1]
            rc = self.get_char(i,j)
            if rc == '#':
                ignore.append(p)
                continue
            if rc == ' ':
                ignore.append(p)
                continue
            if rc.isalpha():
                ignore.append(p)
                continue
            if j !=y and i != 1:
                if c == 'a' or c == 'A':
                    if j !=3:
                        ignore.append(p)
                        continue
                if c == 'b' or c == 'B':
                    if j ==5:
                        ignore.append(p)
                        continue
                if c == 'c' or c == 'C':
                    if j ==7:
                        ignore.append(p)
                        continue
                if c == 'd' or c == 'D':
                    if j ==9:
                        ignore.append(p)
                        continue
            if rc == '`':
                ignore.append(p)
            else:
                moves.append(p)

            for np in [(i-1,j), (i+1,j), (i,j-1), (i, j+1)]:
                if np not in dist or dist[np] > d +1:
                    possible.append(np)
                    dist[np] = d +1
        return moves, dist

    def cost(self, c, d):
        c = c.upper()
        base_cost = {"A":1, "B":10, "C":100, "D":1000}
        return d * base_cost[c]

    def move(self, c, x,y, dists):
        newcost = self.cost(c, dists[(x,y)])
        new_pos = {}
        for k,v in self.pos.items():
            if k ==c:
                v = (x,y)
            new_pos[k] = v
        new_train = []
        for m in self.move_train:
            new_train.append(m)
        new_train.append(c)
        return grid(new_pos, self.curcost + newcost, new_train)

    def finished(self):
        if not (self.pos["A"] == (2,3) or self.pos["A"] == (3,3)):
            return False
        if not (self.pos["a"] == (2,3) or self.pos["a"] == (3,3)):
            return False
        if not (self.pos["B"] == (2,5) or self.pos["B"] == (3,5)):
            return False
        if not (self.pos["b"] == (2,5) or self.pos["b"] == (3,5)):
            return False
        if not (self.pos["C"] == (2,7) or self.pos["C"] == (3,7)):
            return False
        if not (self.pos["c"] == (2,7) or self.pos["c"] == (3,7)):
            return False
        if not (self.pos["D"] == (2,9) or self.pos["C"] == (3,9)):
            return False
        if not (self.pos["d"] == (2,9) or self.pos["c"] == (3,9)):
            return False
        return True


def main():
    with open("input") as w:
        pos = grid.make_pos(list(w.readlines()))
        g = grid(pos)
    
        grids = collections.defaultdict(list)
        grids[0] = [g]
        costs = {}
        finished_str = ""
        finished_grid = None
        mil_print = False
        min_key =0
        visited = {}
        while len(grids) > 0:
            if len(grids[min_key]) ==0:
                del grids[min_key]
                min_key = min(grids.keys())
                print(min_key, len(grids))
            cur_grid = grids[min_key].pop(0)
            s = cur_grid.key()
            if s in costs and costs[s] < cur_grid.curcost:
                continue
            if s in costs and costs[s] == cur_grid.curcost and s in visited:
                continue
            visited[s] = True
            if finished_str in costs and costs[finished_str] < cur_grid.curcost:
                continue
            costs[s] = cur_grid.curcost
            if cur_grid.finished():
                finished_str = s
                finished_grid = cur_grid
                continue
            for start in 'ABCDabcd':
                pm, d =  cur_grid.possible_moves(start)
                for p in pm:
                    new_g = cur_grid.move(start, p[0], p[1], d)
                    new_s = new_g.key()
                    if new_s in costs and costs[new_s] <= new_g.curcost:
                        continue
                    if finished_str in costs and costs[finished_str] < new_g.curcost:
                        continue
                    costs[new_s] = new_g.curcost
                    grids[new_g.curcost].append(new_g)
                    
    
    
        print(costs[finished_str]) 
        print(finished_grid.cur_cost)
        print(finished_grid.move_train)

    

    
main()    
#with open("input_sample") as w:
#    g = grid(w.readlines())
#    g.mark_no_stops()
#    g.change_chars()
#
#    cur_grid = g
#    pm, d =  cur_grid.possible_moves('A')
#    print(pm)
#    for p in pm:
#        print('--------------')
#        print(p)
#        new_g = g.move('A', p[0], p[1], d)
#        print(new_g.str())
