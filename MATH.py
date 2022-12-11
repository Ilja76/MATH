
import math
from random import randint
import random
k=0
l=0
p=0
i=0
choice=['+','-']
choice1=['*']
choice2=['/']
t=int(float(input("mis raskustase?")))
for i in range(4):
    r=random.choice(choice)
    j=random.choice(choice1)
    m=random.choice(choice2)
    A=randint(2,4,6,8,10,12)
    B=randint(2,4,6,8)
    if t==1:
     print(f"{A}{r}{B}")
     a=int(float(input("")))
    if t==2:
     print(f"{A}{j}{B}{r}{A}")
     a=int(float(input("")))
    if t==3:
     print(f"{A}{m}{B}{j}{A}{r}{B}^2")
     a=int(float(input("")))
    if a==A+B or a==A/B+A or a==A*B-A or a==A*B*A*B or a==A/B-A+A or a==A/B+A/B**2 or a==A-B or a==A*B+A or a==A/B*A+B**2 or a==A/B*A-B**2:
     print("oige")
     l+=1
    else:
     print("kahjuks, vale")
     k+=1
    p+=1
h=l/p*100
if h<=59:
    hinne="ekoolis on 2"
elif h>=60 and h<=74:
    hinne="ekoolis on 3"
elif h>=75 and h<=89:
    hinne="ekoolis on 4"
elif h>=90:
    hinne="ekoolis on 5, tubli!"
print(hinne)