Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fruits=['orange','apple','banana','dates','mango']
>>> fruits.count('orange')
1
>>> fruits.index('dates')
3
>>> fruits.reverse()
>>> fruits
['mango', 'dates', 'banana', 'apple', 'orange']
>>> fruits.append('grapes')
>>> fruits
['mango', 'dates', 'banana', 'apple', 'orange', 'grapes']
>>> fruits.index('banana',4)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    fruits.index('banana',4)
ValueError: 'banana' is not in list
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'dates', 'grapes', 'mango', 'orange']
>>> fruits.append('pears')
>>> fruits
['apple', 'banana', 'dates', 'grapes', 'mango', 'orange', 'pears']
>>> fruits.pop()
'pears'
>>> stack=[3,2,4,5]
>>> stack
[3, 2, 4, 5]
>>> stack.append(6)
>>> stack
[3, 2, 4, 5, 6]
>>> stack.append(1)
>>> stack
[3, 2, 4, 5, 6, 1]
>>> [3, 2, 4, 5, 6, 1]
[3, 2, 4, 5, 6, 1]
>>> stack
[3, 2, 4, 5, 6, 1]
>>> stack.pop()
1
>>> 
