def calculate_positive_power(base: int, exponent: int) -> int:
    """
    Calculate base^exponent using divide and conquer algorithm for positive exponents.
    
    This is an efficient O(log n) algorithm that works by:
    1. If exponent is 0, return 1 (base case)
    2. Calculate base^(exponent/2) recursively
    3. If exponent is even: result = (base^(exponent/2))^2
    4. If exponent is odd: result = base * (base^(exponent/2))^2
    
    Args:
        base: The base number (integer)
        exponent: The exponent (non-negative integer)
    
    Returns:
        The result of base^exponent as an integer
    
    Examples:
        >>> calculate_positive_power(3, 2)
        9
        >>> calculate_positive_power(5, 3)
        125
        >>> calculate_positive_power(2, 5)
        32
        >>> calculate_positive_power(7, 0)
        1
    """
    # Base case: any number to the power of 0 equals 1
    if exponent == 0:
        return 1
    
    # Divide: Calculate base^(exponent/2) recursively
    half_power_result = calculate_positive_power(base, exponent // 2)
    
    # Conquer: Combine the results based on whether exponent is even or odd
    if exponent % 2 == 0:
        # Even exponent: base^n = (base^(n/2))^2
        return half_power_result * half_power_result
    else:
        # Odd exponent: base^n = base * (base^(n/2))^2
        return base * half_power_result * half_power_result


def power(base: int, exponent: int) -> float:
    """
    Calculate base^exponent for any integer exponent (positive, negative, or zero).
    
    This function handles:
    - Positive exponents: Uses efficient divide-and-conquer algorithm
    - Zero exponent: Returns 1
    - Negative exponents: Returns 1/(base^|exponent|) as a float
    
    Args:
        base: The base number (integer)
        exponent: The exponent (integer, can be positive, negative, or zero)
    
    Returns:
        The result of base^exponent as a float (to handle negative exponents)
    
    Examples:
        >>> power(4, 6)
        4096.0
        >>> power(2, 3)
        8.0
        >>> power(-2, 3)
        -8.0
        >>> power(2, -3)
        0.125
        >>> power(-2, -3)
        -0.125
    """
    if exponent < 0:
        # For negative exponents: base^(-n) = 1/(base^n)
        positive_result = calculate_positive_power(base, -exponent)
        return 1.0 / positive_result
    else:
        # For non-negative exponents, use the efficient algorithm
        return float(calculate_positive_power(base, exponent))


def demonstrate_power_calculation():
    """
    Demonstrate the power calculation function with various examples.
    """
    test_cases = [
        (2, 3),      # Basic positive case
        (4, 6),      # Larger numbers
        (-2, 3),     # Negative base, odd exponent
        (-2, 4),     # Negative base, even exponent  
        (2, -3),     # Negative exponent
        (-2, -3),    # Negative base and exponent
        (5, 0),      # Zero exponent
        (0, 5),      # Zero base
    ]
    
    print("Power Calculation Examples:")
    print("=" * 30)
    
    for base, exp in test_cases:
        result = power(base, exp)
        print(f"{base}^{exp} = {result}")


if __name__ == "__main__":
    # Run the demonstration
    demonstrate_power_calculation()
    
    # Original example
    print(f"\nOriginal example: (-2)^(-3) = {power(-2, -3)}")
