operators

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print("add",a+b)
print("sub",a-b)
print("mul",a*b)
print("div",a/b)
print("exp",a**b)
print(a//b)








#simple interest

p=int(input("Enter principle amount:"))
t=int(input("Enter the time duration(In years):"))
r=int(input("Enter the interest rate:"))
print("Simple interest is:",((p*t*r)/100))
si=p*t*r
res=si/100
print(res)


#Area of the circle

r=int(input("Enter the radius of the circle:"))
print("Area of the circle is:",(3.14*r*r))
area=3.14*r*r
print("Area of the circle is:",area)


#Area of the triangle

b=int(input("Enter the length of base of a Triangle:"))
h=int(input("Enter the length of height of a Triangle:"))
print("Area of triangle is:",((b*h)/2),"square units")
a=int(input("Enter the side one of triangle:"))
b=int(input("Enter the side two of triangle:"))
c=int(input("Enter the side three of triangle:"))
s=((a+b+c)/2)
d=((s*(s-a)*(s-b)*(s-c))**0.5)
print(f"Area of Triangle of sides {a}, {b}, {c} is {d} square units")
length=int(input("enter the length of triangle"))
breadth=int(input("enter the breadth of triangle"))
triangle=(1/2)*length*breadth
print("area of the triangle is:",triangle)











#Temperature in Celsius to Fahrenheit.

c=int(input("Enter the temperature in Celsius:"))
print("Temperature in Fahrenheit is:",(((c*9)/5)+32))
celsius=int(input("enter the celsius"))
fahrenheit=celcius*1.8+32
print("after converting inti fahrenheit:",fahrenheit)







#Area of rectangle.

l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
print("Area of Rectangle is:",(l*b))
length=int(input("Enter the length of the rectangle:"))
breadth=int(input("Enter the breadth of the rectangle:"))
rect=length*breadth
print("area of rectangle:",rect)


#Perimeter of a square.

s=int(input("Enter the side of the Square:"))
print("Perimeter of the Square is:",(4*s))

square=int(input("Enter the side of the Square:"))
perimeter=4*square
print("Perimeter of the Square is:",perimeter)



#Circumference of a circle.

r=int(input("Enter the radius of the circle:"))
print("Circumference of the circle is:",(3.14*2*r))
radius=int(input("Enter the radius of the circle:"))
 circumference=2*3.14*radius
print("Circumference of the circle is:",circumference)


