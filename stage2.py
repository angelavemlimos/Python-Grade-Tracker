# Task 2.1: Grade classifier
average = 82.5
if average < 0 or average > 100:
    print("Invalid average.")
elif average >= 80: 
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# Task 2.2: Input validation using while
while True:
    try:
        score = float(input("Enter score (0-100): "))
        if 0 <= score <= 100:
            print(f"Valid score: {score}")
            break
        else:
            print("Invalid. Score must be between 0 and 100. Try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Task 2.3: Repeat for N students
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name for student {i + 1}: ")
    score1 = float(input(f"Enter score 1 for {name}: "))
    score2 = float(input(f"Enter score 2 for {name}: "))
    score3 = float(input(f"Enter score 3 for {name}: "))
    
    total = score1 + score2 + score3
    average = total / 3
    
    print(name + " -", f"Total: {total:.2f}, Average: {average:.2f}")

# Task 2.4: Mini challenge (break/continue)
number = int(input("Enter a number: "))
print(f"Table for {number}:")
for i in range(1, 13):
    product = number * i
    if product > 100:
        break
    if i % 5 == 0:
        continue
    print(f"{number} x {i} = {product}")