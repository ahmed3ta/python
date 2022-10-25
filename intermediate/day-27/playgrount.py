def add(*ar):
    sum = 0
    print(ar[2])
    for i in ar:
        sum += i
    return sum

print(add(3, 10, 20,500))

def calculate(n, **kw):
    n+= kw["add"]
    n*= kw["multiply"]
    print(n)
calculate(2, add=3, multiply=4)