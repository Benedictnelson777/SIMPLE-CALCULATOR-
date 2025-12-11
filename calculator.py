
   # WELCOME THE USER
print("Welcome to the Basic Calculator!")
print("You can perform addition, subtraction, multiplication, and division.")

# START THE LOOP
while True:
    print("\n--- New Calculation ---")
    
    # GET THE USERS' INPUTS
    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: ")) 
        operation = input("Please choose an operation (+, -, *, /): ")

        # PERFORM CALCULATIONS
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} : {result}")

        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} : {result}")

        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} : {result}")

        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} : {result}")
            else:
                print("Error: Division by zero is not allowed.")

        else:
            print("Invalid operation selected.")

    except ValueError:
        print("Error: Please enter valid numbers only.")

    # --- FIXED SECTION ---
    choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    
    # If the user types 'yes' OR 'y', we loop. If they type anything else, we break.
    if choice != "yes" and choice != "y":
        print("Goodbye!")
        break
