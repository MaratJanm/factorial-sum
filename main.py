a = 1
b = 2

def factorial(n):
	if n < 0:
		raise ValueError("Factorial not defined for negative numbers")
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result

sum_ab = a + b
first_factorial = factorial(sum_ab)
second_factorial = factorial(first_factorial)
print(second_factorial)
