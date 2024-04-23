def square(x):
    # Square the input
    return x ** 2

def add(a, b):
    # Add two numbers
    return a + b

def multiply(c, d):
    # Multiply two numbers
    return c * d

# Main function
def main():
    # Input values
    num1 = 5
    num2 = 3
    num3 = 2

    # Perform calculations
    result1 = square(num1)
    result2 = add(result1, num2)
    result3 = multiply(result2, num3)

    # Display the final result
    print("Final Result:", result3)

if __name__ == "__main__":
    main()
