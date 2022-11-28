# Question and Solution

## Question

Write a function that takes a list and an integer, and prints the list without the "N"th item on that list.

| INPUT                                                      | OUTPUT                                  |
| ---------------------------------------------------------- | --------------------------------------- |
| ["apples","oranges", "tamato", "potato","tomato"] <br /> 3 | "apples"\n"oranges"\n"potato"\n"tomato" |
| ["euro","dollar","won","yen","tl"] <br /> 5                | "euro"\n"dollar"\n"won"\n"yen"          |

## Solution

```python
def print_without(list,N):
    for i in range(len(l)):
        if i != N:
            print(l[i])

print(print_without(["apples","oranges", "tamato", "potato","tomato"], 3))
```

## Note

Please explain the `len` function in the `Question.html` or `Main.py` files, as they may not have learned it.
