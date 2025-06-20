student_scores = {
    "Alice" : 85,
    "bob" : 92,
    "Charlie" : 78,
    "David" : 95,

}

print("---initial student scores---")

for name, score in student_scores.items():
    print(f"{name}:{score}")
print("\n")

new_student = "grace"
new_student_score = 90
student_scores[new_student] = new_student_score
print(f"---adding new student : {new_student} with score : {new_student_score}---")

for name, score in student_scores.items():
    print(f"{name}:{score}")
print("\n")

print(student_scores)

if student_scores:
    high_score = 0
    high_scorer_name = ""

    for name, score in student_scores.items():
        if score > high_score:
            high_score = score
            high_scorer_name = name

    print("--- Student with Highest Score ---")
    print(f"{high_scorer_name} : {high_score}")
else:
    print("Empty")
