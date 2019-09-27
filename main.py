from adya import *
from sub import *
from mul import *
from div import *
from cube import *
def calculator():
	a=12
	b=12
	print("enter 1 for addition 2 for subtraction 3 for multiplication 4 for subtraction and 5 for cube")
	c=int(input(""))
	if(c==1):
		print(add(a,b))
	elif(c==2):
		print(sub(a,b))
	elif(c==3):
		print(mul(a,b))
	elif(c==4):
		print(div(a,b))
	elif(c==5):
		print(cube(a,b))

'''
c=adya.add(4,5)
print(c)
a=sub.sub(4,5)
print(a)
b=mul.mul(4,5)
print(b)
f=div.div(4,5)
print(f)
k=cube.cube(8)
print(k)'''

calculator()


