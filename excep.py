try:
	numerator = float(input("Enter the first number: "))
	denominator = float(input("Enter the second number: "))
	result = numerator / denominator
except ValueError:
	print("Please enter numbers only.")
except ZeroDivisionError:
	print("You cannot divide by zero.")
else:
	print("Result:", result)
finally:
	print("Program finished.")
