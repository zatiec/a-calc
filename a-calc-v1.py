def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

print("a-calc. easy caculating. modifed by zatiecstudios. original code here:https://www.programiz.com/python-programming/examples/calculator ")
print("Addition(A)")
print("Subtraction(S)")
print("Multiplacation(M)")
print("Division(D)")

while True:
    choice = input("Press Letter to select: ")
    if choice in ('A', 'S', 'M', "D"):
        try:
            Number1 = float(input("First Number"))
            Number2 = float(input("Second Number"))
        except ValueError:
            print("Only Numbers are aloud.")
            continue

        if choice == 'A':
            print(Number1, "+", Number2, "=", addition(Number1, Number2))

        elif choice == 'S':
            print(Number1, "-", Number2, "=", subtract(Number1, Number2))

        elif choice == 'M':
            print(Number1, "*", Number2, "=", multiplication(Number1, Number2))

        elif choice == 'D':
            print(Number1, "/", Number2, "=", division(Number1, Number2))

            More_Calculations = input("Would you like to do another calculation? (y/n): ")
            if More_Calculations == "n":
                break
        