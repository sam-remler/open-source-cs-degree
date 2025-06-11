
def sum_list(lst : list[int]) -> int:
    """A recursive function sum_list(lst) that returns the sum of all elements in a list of integers."""
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])
    
def reverse_string(s : str) -> str:
    """Recursive function reverse_string(s) that returns the reversed version of a given string."""
    if len(s) == 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

def flatten(nested_list : list) -> list:
    """recursive function flatten(nested_list) that takes a nested list (e.g. [1, [2, [3, 4], 5], 6]) and returns a flat list (e.g. [1, 2, 3, 4, 5, 6])"""
    if not nested_list:
        return []
    
    head, *tail = nested_list
    if isinstance(head, list):
        return flatten(head) + flatten(tail)
    else:
        return [head] + flatten(tail)



def fib_memoized(n : int) -> int:
    cache = {0 : 0, 1 : 1}
    def fib(n : int) -> int:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib(n-1) + fib(n-2)
            return cache[n]
    
    return fib(n)

print(fib_memoized(10))