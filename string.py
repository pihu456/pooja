Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> number =input("enter your number")
enter your number12
>>> number
'12'
>>> number=int(input("enter the number"))
enter the number12
>>> number
12
>>> str=int(input("enter your name"))
enter your namepooja
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    str=int(input("enter your name"))
ValueError: invalid literal for int() with base 10: 'pooja'
>>> str
<class 'str'>
>>> str=int(input("enter your name:"))
enter your name:pooja
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str=int(input("enter your name:"))
ValueError: invalid literal for int() with base 10: 'pooja'
>>> number=(str(input("enter your name:"))

	    bdfjghjf
	    
SyntaxError: invalid syntax
>>> number=str(input("enter name:"))
	    
enter name:pooja
>>> number
	    
'pooja'
>>> import os
	    
>>> os.windows('cls')
	    
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    os.windows('cls')
AttributeError: module 'os' has no attribute 'windows'
>>> import os
	    
>>> os.system('cls')
	    
0
>>> number=int(input("enter the number"))
	    
enter the number12
>>> print("your number is ",number)
	    
your number is  12
>>> 
