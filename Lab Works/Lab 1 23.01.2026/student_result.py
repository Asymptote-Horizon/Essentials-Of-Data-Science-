marks = []
pass_count = 0

for i in range(5):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)
    
    # Calculate grade for the individual subject
    if m >= 91:
        sub_grade = "A1"
    elif m >= 81:
        sub_grade = "A2"
    elif m >= 71:
        sub_grade = "B1"
    elif m >= 61:
        sub_grade = "B2"
    elif m >= 51:
        sub_grade = "C1"
    elif m >= 41:
        sub_grade = "C2"
    elif m >= 33:
        sub_grade = "D"
    else:
        sub_grade = "E (Fail)"

    # Print individual result immediately
    status = "Pass" if m >= 33 else "Fail"
    print(f"Result for Subject {i+1}: {status} | Grade: {sub_grade}")
    
    if m >= 33:
        pass_count += 1

# Final aggregate calculation
total = sum(marks)
percent = (total / 500) * 100

print("\n" + "="*30)
print("      FINAL REPORT 2026")
print("="*30)

# Student passes only if they passed all 5 subjects
if pass_count == 5:
    if percent >= 75:
        final_division = "Distinction"
    elif percent >= 60:
        final_division = "First Division"
    elif percent >= 50:
        final_division = "Second Division"
    elif percent >= 33:
        final_division = "Third Division"
    
    print(f"Final Status: PASSED")
    print(f"Total Percentage: {percent}%")
    print(f"Overall Division: {final_division}")
else:
    print(f"Final Status: FAILED")
    print(f"Backlogs: {5 - pass_count} subject(s)")
print("="*30)
