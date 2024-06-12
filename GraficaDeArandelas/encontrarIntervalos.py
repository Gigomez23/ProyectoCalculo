import numpy as np
from scipy.optimize import fsolve
from sympy import sympify, symbols, lambdify

# Define a function to get user input and parse it into a callable function
def get_function_from_input(prompt):
    user_input = input(prompt)
    x = symbols('x')
    parsed_function = sympify(user_input)
    return lambdify(x, parsed_function)

# Get user input for the two functions
print("Please enter the two functions of x.")
g_func = get_function_from_input("Enter the first function g(x): ")
h_func = get_function_from_input("Enter the second function h(x): ")

# Define the function representing the difference
def diff_func(x):
    return g_func(x) - h_func(x)

# Initial guesses for the roots
initial_guesses = np.linspace(-10, 10, 100)

# Find the roots using fsolve
roots = []
for guess in initial_guesses:
    root = fsolve(diff_func, guess)[0]
    # Check if the root is already in the list (with a tolerance for floating point errors)
    if not any(np.isclose(root, existing_root, atol=1e-5) for existing_root in roots):
        roots.append(root)

# Sort the roots
roots = sorted(roots)

print("Intersection points:", roots)
