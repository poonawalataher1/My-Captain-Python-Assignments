#creating limit for fibonacci series
limit = int(input('Enter the Limit for Fibonacci series :'))

#defining first two variables
n1 = 0
n2 = 1

count = 0

while count < limit:
    print(n1)
    next_term = n1 + n2
    n1 = n2
    n2 = next_term

    count += 1



