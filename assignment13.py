1.Checking whether a string is stars with specified character¶
In [3]:
a=input('enter the string')
if a.lower().startswith('a'):
  print('the string stars with : a ')
enter the stringanandh
the string stars with : a 

2.Index of the charactor in the string
In [5]:
i=a.index('a')
i1=a.index('a',1)
print(i)
print(i1)
0
2

3.Iterate over the dictionary using for loop
In [8]:
n={'a':1,'b':2,'c':4,'d':5}
for i,j in n.items():
  print(i,':',j,end=',')
a : 1,b : 2,c : 4,d : 5,

4.Removing keys from a dictionary
In [11]:
d={'a':4,'b':1,'c':3,'d':5,'e':0}
print(d)
del d['e']  #d.pop('e')
print(d)
{'a': 4, 'b': 1, 'c': 3, 'd': 5, 'e': 0}
{'a': 4, 'b': 1, 'c': 3, 'd': 5}