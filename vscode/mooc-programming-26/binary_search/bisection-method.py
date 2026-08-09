def square_root_bisection(number: int, tolerance: float, max_iterations: int):
    low = 0
    high = number

    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    for i in range(max_iterations):
        root = (low + high) / 2
        pow_root = root * root
        if pow_root + tolerance == number or pow_root - tolerance == number or pow_root == number:
            print(f"The square root of {number} is approximately {root}")
            return root
        elif pow_root > number:
            high = root
        else:
            low = root

    print(f"Failed to converge within {max_iterations} iterations")
    return None

print(square_root_bisection(225, 1e-7, 100))