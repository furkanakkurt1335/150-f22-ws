# Question and Solution

## Question

Write a function that takes a list full of integers that adds every 2 consecutive items together and prints them.

| INPUT               | OUTPUT                                                |
| ------------------- | ----------------------------------------------------- |
| [1,3,5,7,8]         | [1\n4\n3\n8\n5\n12\n7\n15\n8]                         |
| [3,5,4,124,5,3,9,7] | [3\n8\n5\n9\n4\n128\n124\n129\n5\n8\n3\n12\n9\n16\n7] |

## Solution

```python
def print_consecutives(l):
    early, late = 0, 0
    for i in l:
        early = late
        late = i
        print(early+late)

print(print_consecutives([1,3,5,7,8]))
```
