def get_valid_score():
    """Get and validate user input for test score"""
    while True:
        try:
            score = float(input("Enter your test score (0-100): "))
            if score < 0 or score > 100:
                print("❌ Invalid score! Please enter a score between 0 and 100.")
                continue
            return score
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def get_letter_grade(score):
    """Determine letter grade based on score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_feedback(grade):
    """Get feedback message based on grade"""
    feedback = {
        "A": "Excellent work! Keep it up!",
        "B": "Great job! You're doing well.",
        "C": "Good effort! You passed.",
        "D": "You passed, but there's room for improvement.",
        "F": "You need to study more for the next test."
    }
    return feedback[grade]

def main():
    """Main program"""
    print("=" * 40)
    print("       GRADE CALCULATOR")
    print("=" * 40)
    
    # Get valid score from user
    score = get_valid_score()
    
    # Determine letter grade
    grade = get_letter_grade(score)
    
    # Get feedback
    feedback = get_feedback(grade)
    
    # Print results
    print("\n" + "=" * 40)
    print(f"Your score: {score}")
    print(f"Your grade: {grade}")
    print(f"Message: {feedback}")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    main()
