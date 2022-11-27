# Question and Solution

## Question

Write a program that only prints the strings and integers from a given list. The outputs should look like the example

| INPUT                                               | OUTPUT                   |
| --------------------------------------------------- | ------------------------ |
| ["pasta",14, False, "True", 3.5,"makarna",(3,8),12] | pasta 14 True makarna 12 |
| [13,51.5,(False,3),"9"]                             | 13 9                     |

## Solution

```python
list=["pasta",14, False, "True", 3.5,"makarna",(3,8),12]

for item in list:
    if type(item)==str or type(item)==int:
        print (item, end=" ")
```
