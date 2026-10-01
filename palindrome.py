word = input("Enter a word: ").lower()
reversed_word = word[::-1]

if word == reversed_word:
	print("It is a palindrome.")
else:
	print("It is not a palindrome.")
