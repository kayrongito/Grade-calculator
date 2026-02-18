# Get user input
score = int(input("Enter your test score (0-100): "))

# Validate input
if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100")
else:
    # Check grade using if-else
    if score >= 90:
        print("Grade: A - Excellent!")
    elif score >= 80:
        print("Grade: B - Good job!")
    elif score >= 70:
        print("Grade: C - Satisfactory")
    elif score >= 60:
        print("Grade: D - Passing, but needs improvement")
    else:
        print("Grade: F - Failing")
