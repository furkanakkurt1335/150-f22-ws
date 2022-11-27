# Question and Solution

## Question

Write a function that takes a list and only prints the odd numbers in the list; list may contain strings.

| INPUT                               | OUTPUT                 |
| ----------------------------------- | ---------------------- |
| [1,5,2,3,5,6,82,"a","b",6,12,5,436] | [2, 6, 82, 6, 12, 436] |
| [0,12,4,21,53,346,234]              | [0, 12, 4, 346, 234]   |

## Solution

```python
def print_odds(list):
    for i in list:
        if type(i) == type(5):
            if i % 2 == 1:
                print(i)

print(print_odds([0,12,4,21,"a",346,234]))
```

## Note

Please explain the `type` function in the `Question.html` or `Main.py` files, as they may not have learned it.
