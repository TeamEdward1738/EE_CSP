def fibonacci_sequence():
    # Prompt user for input
    try:
        n = int(input("Enter the number of Fibonacci numbers to print (1-20): "))
        if n < 1 or n > 20:
            print("Please enter a number between 1 and 20.")
            return
        
        # Generate Fibonacci sequence
        fib_sequence = []
        a, b = 0, 1
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b
        
        # Print the sequence on the same line
        print("Fibonacci sequence:", " ".join(map(str, fib_sequence)))
    
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 20.")

# Call the function
fibonacci_sequence()