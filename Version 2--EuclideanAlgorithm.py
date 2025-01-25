def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean Algorithm.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The GCD of the two integers.
    """
    while b != 0:  # Continue the loop until the remainder is zero
        a, b = b, a % b  # Update 'a' with 'b', and 'b' with the remainder of a divided by b
    return a  # When 'b' becomes 0, 'a' contains the GCD

def get_positive_integer(prompt):
    """
    Prompt the user to input a positive integer and validate the input.

    Parameters:
    prompt (str): The input prompt to display to the user.

    Returns:
    int: A valid positive integer entered by the user.
    """
    while True:
        try:
            num = int(input(prompt))  # Attempt to convert user input to an integer
            if num > 0:  # Check if the number is positive
                return num
            else:
                print("Error: Please enter a positive integer.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

# Main program
if __name__ == "__main__":
    print("Euclidean Algorithm - Calculate GCD")
    # Prompt the user to input two positive integers
    num1 = get_positive_integer("Please enter the first positive integer: ")
    num2 = get_positive_integer("Please enter the second positive integer: ")

    # Call the gcd function and print the result
    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")
