def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)











total_sum = sum(range(1, 100))
print(total_sum)

numbers = [5, 6, 7, 8]
for num in numbers:
    print(f"The factorial of {num} is: {factorial(num)}")