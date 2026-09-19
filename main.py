```python
print("==== Simple Python Calculator ====")

while True:
    print("\nChoose an operation:")
    print("addition")
    print("sub")
    print("mul")
    print("div")
    print("q - Quit")

    c = input("\nEnter operation: ").lower()

    if c == "q":
        print("Calculator closed. Thank you!")
        break

    if c not in ["addition", "sub", "mul", "div"]:
        print("❌ You entered a wrong operation.")
        continue

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if c == "addition":
        print("Result:", a + b)

    elif c == "sub":
        print("Result:", a - b)

    elif c == "mul":
        print("Result:", a * b)

    elif c == "div":
        if b == 0:
            print("❌ Cannot divide by zero.")
        else:
            print("Result:", a // b)
```
