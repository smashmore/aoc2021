subs={}
rev_subs = {}
start_key =0
import pprint

class output():
    def __init__(self):
        pass

    def compute(self,w,x,y,z,inputs):
        #print(w,x,y,z,inputs)
        return (w,x,y,z,inputs)

class start():
    def __init__(self):
        self.after = None

    def set_after(self, after):
        #print(after)
        self.after =after

    def compute(self,w,x,y,z,inputs):
        return self.after.compute(w,x,y,z,inputs)

class inp():
    def __init__(self, var):
        self.var = var
        self.after = None

    def set_after(self, after):
        self.after =after

    def compute(self,w,x,y,z,inputs):
        if self.var == "w":
            w = inputs[0]
        if self.var == "x":
            x = inputs[0]
        if self.var == "y":
            y = inputs[0]
        if self.var == "z":
            z = inputs[0]
        #print(w,x,y,z, inputs, "inp", self.var)
        return self.after.compute(w,x,y,z,inputs[1:])

def key_lookup(key):
    if key in rev_subs:
        return rev_subs[key]
    global start_key
    new_sub = "g"+str(start_key).zfill(3)
    start_key +=1
    rev_subs[key] = new_sub
    subs[new_sub] = key
    return new_sub


#add = lambda x,y: x+y
def add(x,y):
    if isinstance(x,list):
        rs = []
        for x0 in x:
            r = add(x0,y)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))
    if isinstance(y,list):
        rs = []
        for y0 in y:
            r = add(x,y0)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))

    if isinstance(x,int) and isinstance(y,int):
        return x+y
    if x == 0:
        return y
    if y ==0:
        return x
    if isinstance(y,int):
        a=x
        b=y
    elif x < y:
        a =x
        b = y
    else:
        b=x
        a=y
    key = "(%s) + (%s)" %(a,b)
    return key_lookup(key)
#mul = lambda x,y: x*y
def mul(x,y):
    if isinstance(x,list):
        rs = []
        for x0 in x:
            r = mul(x0,y)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))
    if isinstance(y,list):
        rs = []
        for y0 in y:
            r = mul(x,y0)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))

    if y ==0:
        return 0
    if x ==0:
        return 0
    if x ==1:
        return y
    if y ==1:
        return x
    if isinstance(x,int) and isinstance(y,int):
        return x*y
    #return "(%s) * (%s)" %(x,y)
    if isinstance(y,int):
        a=x
        b=y
    elif isinstance(x,int):
        b=x
        a=y
    elif x < y:
        a =x
        b = y
    else:
        b=x
        a=y
    return key_lookup("%s*%s" %(a,b))
#div = lambda x,y: x//y if x>0 and y>0 else (x+(-x%y))//y
def div(x,y):
    if isinstance(x,list):
        rs = []
        for x0 in x:
            r = div(x0,y)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))
    if isinstance(y,list):
        rs = []
        for y0 in y:
            r = div(x,y0)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))

    if y ==1:
        return x
    if x ==0:
        return 0
    if isinstance(x,int) and isinstance(y,int):
        return x//y if x>0 and y>0 else (x+(-x%y))//y
    #return "(%s) // (%s)" %(x,y)
    return key_lookup("%s//%s" %(x,y))
    #return "%s\n%s" %(x,y)
#mod = lambda x,y: x%y if x>=0 and y > 0 else None
def mod(x,y):
    if isinstance(x,list):
        rs = []
        for x0 in x:
            r = mod(x0,y)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))
    if isinstance(y,list):
        rs = []
        for y0 in y:
            r = mod(x,y0)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))
    if isinstance(x,int) and isinstance(y,int):
        return x%y
    #return "(%s) %% (%s)" %(x,y)
    return key_lookup("%s%%%s" %(x,y))
#eql = lambda x,y: 1 if x ==y else 0
def eql(x,y):
    if isinstance(x,list):
        rs = []
        for x0 in x:
            r = eql(x0,y)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))
    if isinstance(y,list):
        rs = []
        for y0 in y:
            r = eql(x,y0)
            if isinstance(r,list):
                rs.extend(r)
            else:
                rs.append(r)
        return list(set(rs))
    if isinstance(x,int) and isinstance(y,int):
        if x==y:
            return 1
        else:
            return 0
    if x==y:
        return 1
    #print(x,y)
    if isinstance(x, str) and x[0] == "e" and isinstance(y,int) and y > 9:
        return 0
    if isinstance(y, str) and y[0] == "e" and isinstance(x,int) and x > 9:
        return 0
    #return "(%s) == (%s)" %(x,y)
    if isinstance(y,int):
        a=x
        b=y
    elif x < y:
        a =x
        b = y
    else:
        b=x
        a=y
    return key_lookup("%s==%s" %(a,b))

class op():
    def __init__(self, var, other, op_func, name):
        self.var = var
        self.op_func = op_func
        self.name = name
        if other.isalpha():
            self.other_var = True
        else:
            self.other_var = False
            other = int(other)
            
        self.other =other
        self.after = None

    def set_after(self, after):
        self.after =after

    def compute(self,w,x,y,z,inputs):
        other_val =0
        if not self.other_var:
            other_val = self.other
        elif self.other == "w":
            other_val = w
        elif self.other == "x":
            other_val = x
        elif self.other == "y":
            other_val = y
        elif self.other == "z":
            other_val = z

        if self.var == "w":
            w = self.op_func(w, other_val)
        if self.var == "x":
            x = self.op_func(x, other_val)
        if self.var == "y":
            y = self.op_func(y, other_val)
        if self.var == "z":
            z = self.op_func(z, other_val)
        #print(w,x,y,z, inputs, self.name, self.var, self.other)
        return self.after.compute(w,x,y,z,inputs)


with open("input") as w:
    s = start()
    end = s
    for l in w.readlines():
        parts = l.strip().split(" ")
        new_op = None
        if l.strip() =="":
            continue
        if len(parts) ==2:
            new_op = inp(parts[1])
        else:
            if parts[0] == "add":
                o = add
            elif parts[0] == "mul":
                o = mul
            elif parts[0] == "mod":
                o = mod
            elif parts[0] == "div":
                o = div
            elif parts[0] == "eql":
                o = eql
            new_op = op(parts[1], parts[2], o, parts[0])
        end.set_after(new_op)
        end = new_op
    end.set_after(output())

    def guess_arrays(equation, prefix):
        if len(prefix) == 14:
            w,x,y,z,ip = equation.compute(0,0,0,0,prefix)
            if z==0 or 0 in z:
                return [prefix]
            else:
                return []
        else:
            r = []
            for g in range(1,10):
                st = []
                for p in prefix:
                    st.append(p)
                st.append(g)
                while len(st) < 14:
                    st.append(list(range(1,10)))
                w,x,y,z,ip = s.compute(0,0,0,0,st)
                if (isinstance(z,list) and 0 in z) or (isinstance(z,int) and z==0):
                    new_prefix =[]
                    for p in prefix:
                        new_prefix.append(p)
                    new_prefix.append(g)
                    r.extend(guess_arrays(equation, new_prefix))
            return r

    for a in [9,8,7,6,5,4,3,2,1]:
        for b in [9,8,7,6,5,4,3,2,1]:
            print(guess_arrays(s, [a,b]))

   
    
