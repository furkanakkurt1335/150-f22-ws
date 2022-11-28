# Question and Solution

## Question

Write a program that takes a list. If the list has more than 5 items in it and the number of items is odd, the program prints the list, one by one, without the 3 items in the middle. If the list is shorter than 5 or the number of items are even, the original list is printed one by one.

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
    for i in range(a):
        if i < int((a-3)/2) or i > (a - int((a-3)/2)):
            print(i)
else:
    for i in the_list:
        print(i)
```

## Note

Please explain the `len` function in the `Question.html` or `Main.py` files, as they may not have learned it. They won't be using slicing for the solution.
