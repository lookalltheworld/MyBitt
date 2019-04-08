

#函数作用域
name='alex'
def foo():
    name='sb'
    def tt():
        name='super'
        def rr():
            print(name)
        return rr
    return tt
foo()()()

#匿名函数
li=lambda x,y,z:(x+1,y+1,z+1)
print(li(5,5,5))

#map()原理和认识
m='liyujun'
print(list(map(lambda x:x.upper(),m)))

def chang_map(y,m):
    c=[]
    for i in m:
        res=y(i)
        c.append(res)
    return c
def y(x):
    return x.upper()
print(chang_map(y,m))


#filter（）原理
f=['chen_sb','skd_sb','skfl_sb','fhja']
def filter_sb(sb,f):
    h=[]
    for i in f:
        if sb(i):
            h.append(i)
    return h

def sb(x):
    return not x.endswith('sb')

print(filter_sb(sb,f))

print(list(filter(lambda x:not x.endswith('sb'),f)))

num=[1,2,3,3,100]
def reduce_1(x,num,init=None):
    if init==None:
        res=num.pop(0)
    else:
        res=init
    for i in num:
            res=x(res,i)
    return res
print(reduce_1(lambda m,n:m*n,num))
from functools import reduce
print(reduce(lambda m,n:m*n,num))


print(list(zip('12345',['a','b','c','d'])))