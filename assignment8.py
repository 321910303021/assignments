1.length of the string
In [ ]:
a=input('enter the string')
c=0
for i in a:
  c+=1
print(c)
enter the stringRavi
4
2.count of the character of the string
In [33]:
a=input('enter the string')
n=a.split()
c=0
for i in n:
  for j in i:
    c+=1
print(c)
enter the stringwrite your name here
17
3.No of 'o' in given string
In [ ]:
n='hello world'
c=0
for i in n:
    if i=='o':
        c+=1
print(c)
2
4.Script in upper and lower case
In [8]:
a=input('enter the script')
u=a.upper()
l=a.lower()
print('the upper case of the script is: ',u)
print('the lower case of the script is: ',l)
enter the scriptthere is an Apple
the upper case of the script is:  THERE IS AN APPLE
the lower case of the script is:  there is an apple
5.Substrings in a String
In [9]:
a=input('enter the string')
n=a.split()
print('the substrings of the string is: ',n)
enter the stringthey are boys
the substrings of the string is:  ['they', 'are', 'boys']
6.Comparing two strings
In [13]:
a=input('enter the string')
n=a.split()
for i in n:
  if i=='book':
    print(i,' :is present in the given string')
  elif(i<'book'):
    print(i,' :word is smaller than the apple')
  else:
    print(i,' :word is greater than the apple')
enter the stringboth the book and apple are present on the table
both  :word is greater than the apple
the  :word is greater than the apple
book  :is present in the given string
and  :word is smaller than the apple
apple  :word is smaller than the apple
are  :word is smaller than the apple
present  :word is greater than the apple
on  :word is greater than the apple
the  :word is greater than the apple
table  :word is greater than the apple
7.Deletion of a character
In [32]:
a=input('enter the string')
print(a.replace('s',''))
enter the stringenglish
englih
8.printing characters in a string
In [24]:
a=input('enter the string')
n=a.split()
for i in n:
  for j in i:
    print(j,'is the character in ',i)
enter the stringthere is a apple
t is the character in  there
h is the character in  there
e is the character in  there
r is the character in  there
e is the character in  there
i is the character in  is
s is the character in  is
a is the character in  a
a is the character in  apple
p is the character in  apple
p is the character in  apple
l is the character in  apple
e is the character in  apple
9.length of the string without len function¶
In [25]:
a='refrigerator'
c=0
for i in a:
  c+=1
print(c)
12
10.Substrings are present in string or not
In [26]:
a=input('enter the string')
n=a.split()
c=0
for i in n:
  if len(i)==1:
    c+=1
  else:
    pass
if c in [0,1,2]:
  print('the string contains substrings')
else:
  print('the string does not have substrings')
enter the stringthere is a apple in the tree
the string contains substrings
In [28]:

In [ ]:
