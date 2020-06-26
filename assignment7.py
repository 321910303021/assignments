1.Sum of n natural naumbers
In [1]:
n=int(input('enter no of elements'))
sum=0
for i in range(n+1):
  sum+=i
print(sum)
enter no of elements5
15

2.Even and Odd numbers in series
In [11]:
y=set(input('enter the list elements').split())
l=[]
m=[]
for i in y:
  if int(i)%2==0:
    l.append(int(i))
  else:
    m.append(int(i))
print(len(l),'the even list is ',l)
print(len(m),'the odd list is',m)
enter the list elements6 4 2 6 4 3 1 8
4 the even list is  [2, 6, 8, 4]
2 the odd list is [3, 1]

3.Printing numbers
In [13]:
for i in range(0,7):
  if i%3==0:
    continue
  else:
    print (i)
1
2
4
5

4.squares of the numbers in list
In [15]:
x=input('enter the list numbers').split()
l=[]
for i in x:
  l.append(int(int(i)**2))
print(l)
enter the list numbers7 3 4 2 1
[49, 9, 16, 4, 1]

5.Sum and average of n integers
In [16]:
n=int(input('enter the number of integers'))
sum=0
for i in range(n+1):
  sum+=i
print(f'sum: {sum} and average is {sum/n}')
enter the number of integers5
sum: 15 and average is 3.0

6.Reverse a give number
In [29]:
n=input('enter a number with spaces between each digit').split( )
a=n[ : :-1]
b=''.join(a)
print(b)
enter a number with spaces between each digit5 3 4 2 3
32435
In [ ]:

7.Print odd numbers
In [30]:
n=int(input('enter the range'))
l=[]
for i in range(1,n+1):
  if i%2!=0:
    l.append(i)
  else:
    pass
print(l)
enter the range6
[1, 3, 5]

8.Count no of digits in number
In [31]:
n=int(input('enter the number'))
count=0
while n>0:
  n=n//10
  count+=1
print(count)
enter the number453672
6

9.Check number is palindrome
In [36]:
n=int(input('enter the number'))
temp=n
rev=0
while(n>0):
  dig=n%10
  rev=rev*10+dig
  n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
enter the number87655678
The number is a palindrome!

10.To print an Identity matrix
In [41]:
n=int(input('enter the matrix number'))
for i in range(0,n):
  for j in range(0,n):
    if i==j:
      print("1",sep=" ",end=" ")
    else:
     print("0",sep=" ",end=" ")
  print()
enter the matrix number3
1 0 0 
0 1 0 
0 0 1 

11.Check the number is perfect or not
In [42]:
n = int(input("Enter any number: "))
sum = 0
for i in range(1, n):
  if(n % i == 0):
    sum += i
if (sum == n):
  print("The number is a Perfect number ")
else:
  print("The number is not a Perfect number ")
Enter any number: 3
The number is not a Perfect number 