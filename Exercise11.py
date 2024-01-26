def extract_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits[::-1]

number = int(input("Enter a number: "))
result = extract_digits(number)
print("Result: ", " ".join(map(str, result)))