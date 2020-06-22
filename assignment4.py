In [1]:
def greater(a,b,c):
  print(max(a,b,c))
In [2]:
greater(4,6,7)
7

In [16]:
def search_elenment(a,n):
   if  a in range(0,n+1):
     print(a,'is in the range')
   else:
    print(a,'is not in the range')
In [24]:
search_elenment(4,6)
4 is in the range

In [31]:
def factorial(n):
  res=1
  i=0
  if n>0:
    for i in range (1,n+1):
      res*=i
    return res
  elif(n==0):
    return 1
  else:
    print(n,'is a non negetive number')
In [36]:
factorial(6)
Out[36]:
720
In [ ]: