1.Read an entire text file
In [1]:
f=open('example.txt')
f.seek(0)
x=f.read()
print(x)
Hello World
In [2]:
f.close()

2.Append text to a file and display the text
In [9]:
f=open('example2.txt','a+')
f.write('\nhello world')
f.write('\nmy name is ravi chandra')
Out[9]:
24
In [10]:
f.seek(0)
print(f.read())
hello world
my name is ravi chandra
In [7]:
f.close()

3.Read a file line by line
In [14]:
f=open('example3.txt')
x=f.readlines()
f.seek(0)
print(x)
['good morning to all\n', 'i am going to say wounderful topic \n', 'to day']
In [15]:
f.close()

4.Read contents of a file using for loop
In [16]:
f=open('example3.txt','r+')
lines=f.readlines()
for l in lines:
    print(l)
good morning to all

i am going to say wounderful topic 

to day
In [17]:
f.close()

5.Remove leading and traling spacesfrom a string
In [27]:
a=input('enter the string')
print(f'before appling strip function is : {a}')
print(f'after removing all lstrips and rstrips in string is : {a.strip()}')
enter the string    hello    
before appling strip function is :     hello    
after removing all lstrips and rstrips in string is : hello