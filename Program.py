def prime_numbers(n):
    if n%2  == 0:
        return False
    else:        return True


total_sum = sum(range(1, 100))
print(total_sum)

n = [20, 7, 40, 50, 60, 70, 80, 90, 100]
for num in n:
    print(f" {num} is : {prime_numbers(num)}")