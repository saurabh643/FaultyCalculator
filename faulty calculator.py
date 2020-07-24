# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:20:21 2020

@author: Saurabh
"""




print("Enter 1st Number")
num1 = int(input())
print("Enter 2nd Number")
num2 = int(input())
print('Select Operation--+,-,/,*')
num3 =input()

if num1==30 and num2==20 and num3=='+':
    print('100')
elif num1==20 and num2==30 and num3=='+':
    print(100)
elif num1==10 and num2==5 and num3=='*':
    print('1')
elif num1==5 and num2==10 and num3=='*':
    print('1')
elif num1==20 and num2==10 and num3=='/':
    print('1')
elif num1==10 and num2==20 and num3=='/':
    print('1')
elif num1==50 and num2==50 and num3=='-':
    print('1000')
elif num3=='+':
    plus=num1+num2
    print(plus)
elif num3=='*':
    multi=num1*num2
    print(multi)
elif num3=='/':
    devide=num1/num2
    print(devide)
elif num3=='-':
    sub=num1-num2
    print(sub)

