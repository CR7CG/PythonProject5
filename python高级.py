"""def sum(a):
    return a**2
num = [10,20,30]
result= (map(sum,num))
print(list(result))
#map函数使用要change list
def arr(a):
    return a*2
num = {"h":1,"2":10}"""

from functools import reduce

#a = num.keys()
#print(a)num.keys是一种tuple,不是有
"""result= (map(arr,a()))
print(list(result))
""""""
def ask(a):
    return a%3==1
num = [1,2,3,4,5]
result= filter(ask,num)
print(list(result)),"""


"""a = [1,2,3,4,5]
print(sorted(a))


a = [1,2,3,4,5.456,789,0.01]
re = sorted(a,reverse=True)
print(re)

def lens(a):
    return lens(a)
words = ["jgfj","fjghjg","cgr"]
re = sorted(words,key = lens)#按照什么方法排序
print(re)
""""""
def sum(a,b):
    return a+b
a = [1,2,3,4,5]
re = reduce(sum,a)
print(re)
a = lambda x,y: x+y
print(a(5,10))"""
"""
s = lambda x,y:x if x>y else y
print(s(100,200))
s = lambda x,y:x+y
print(s(100,200))
s = lambda x,y : x+y"""
""""
a = lambda x:x+1
num = [4,5,6]
res = list(map(a,num))
print(res)
a = lambda x:x**2
num = [4,5,6]
res = list(map(a,num))
print(res)
a = lambda x:x**2
num = [4,5,6]"""



a = lambda x:x%2==1
num = [4,5,6]
res = list(filter(a,num))
print(res)
a = lambda x:len(x)
name = {'cr7',49,'messi',37,}
