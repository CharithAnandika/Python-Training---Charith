student_scores = {
    "Alice": 85,
    "bob": 92,
    "Charlie": 78,
    "David": 95,
}

print("--- initial student scores ---")
for name, score in student_scores.items():
    print(f"{name}: {score}")
print()

# Add a new student
new_student = "grace"
new_student_score = 90
student_scores[new_student] = new_student_score

print(f"--- adding new student: {new_student} with score: {new_student_score} ---")
for name, score in student_scores.items():
    print(f"{name}: {score}")
print()

# Print the entire dictionary
print(student_scores)
print()

# Find the student with the highest score
if student_scores:
    high_score = -1
    high_scorer = None
    for name, score in student_scores.items():
        if score > high_score:
            high_score = score
            high_scorer = name
    print("--- Student with highest score ---")
    print(f"{high_scorer}: {high_score}")
else:
    print("Empty")
print()

# Create a new dictionary for top achievers (>= 90)
high_achievers = {name: score for name, score in student_scores.items() if score >= 90}

print("--- High Achievers (score 90 or above) ---")
if high_achievers:
    for name, score in high_achievers.items():
        print(f"{name}: {score}")
else:
    print("No student above 90")
