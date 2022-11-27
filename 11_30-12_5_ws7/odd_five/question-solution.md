# Question and Solution

## Question

Write a program that takes a list. If the list has more than 5 items in it and the number of items is odd, the program prints the list without the 3 items in the middle. If the list is shorter than 5 or the number of items are even, the original list is printed.

| INPUT                                                       | OUTPUT                                                      |
| ----------------------------------------------------------- | ----------------------------------------------------------- |
| [3,325,12365,21,41,3,5,1,5]                                 | [3, 325, 12365, 5, 1, 5]                                    |
| ["horse","chicken","pig","lamb","cow","ox","rooster","dog"] | ["horse","chicken","pig","lamb","cow","ox","rooster","dog"] |
| [1,22,333,444]                                              | [1,22,333,444]                                              |

## Solution

```python
the_list=["horse","chicken","pig","lamb","cow","ox","rooster"]

if len(the_list)>= 5 and len(the_list)%2!=0:
    a=len(the_list)
    the_list=the_list[0:int((a-3)/2)]+the_list[-int((a-3)/2):a]
    print(the_list)
else:
    print(the_list)
```
