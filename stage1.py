# Q1: How does Python's program structure differ from other languages (braces, semicolons)?
# Answer: Python uses indentation (4 spaces) instead of curly braces {} to define blocks, 
# and does not require semicolons at the end of statements.

# Q2: What are int, float, str, and bool? What does type() do?
# Answer: They represent integers, floating-point numbers, strings, and booleans. 
# type() returns the data type of a given object.

# Q3: Try "5" + 5 and int("5") + 5. What happens and why?
# Answer: "5" + 5 raises a TypeError because you cannot concatenate a string and an integer. 
# int("5") + 5 works and evaluates to 10 because "5" is explicitly converted to an integer.


# Task 1.1: Total and average
name = input("Enter student name: ")
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

total = score1 + score2 + score3
average = total / 3

print(name + " -", f"Total: {total:.2f}, Average: {average:.2f}")

# Task 1.2: Inspect the types
print(type(name))
print(type(score1))
print(type(total))

# Task 1.3: Predict, then run
# Predictions: 3.5, 3, 49, 8, "ababab"
print(7 / 2)
print(7 // 2)
print(7 ** 2)
print(2 ** 3)
print("ab" * 3)