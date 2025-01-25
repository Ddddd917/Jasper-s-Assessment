"""
Algorithm EuclideanAlgorithm(a,b):
Input: Two positive integers a and b
Output: The greatest common divisor(GCD) of a and bool
Step 1: While b != 0, continue do the folloing:
    1.1: Compute the remainder r = a % b
    1.2: Update a = b
    1.3: Update b = r
Step 2: When b = 0, return a as the GCD
"""

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

# Main program
if __name__ == "__main__":
    # Prompt the user to input two integers
    num1 = int(input("Please enter the first integer: "))
    num2 = int(input("Please enter the second integer: "))

    # Call the gcd function and print the result
    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")