try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError as e:
    print(f"You cannot divide by zero, sorry.")
    print(f"Error details: {e}")
except ValueError as e:
    print(f"You must enter an integer value.")
    print(f"Error details: {e}")
except Exception as e:
    print(f"Unespected error. {e}")
    print(f"Error details: {e}")
except BaseException as e:
    print(f"Unespected error. {e}")
    print(f"Error details: {e}")

print("THE END.")

"""
Expcetion Hierarchy:

1. BaseException
2. Exception
3. ArithmeticError
4. ZeroDivisionError
"""