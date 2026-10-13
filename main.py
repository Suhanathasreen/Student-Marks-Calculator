def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    print("=" * 35)
    print("      STUDENT MARKS CALCULATOR")
    print("=" * 35)

    name = input("Enter student name: ").strip()
    try:
        subjects_count = int(input("Enter number of subjects: "))
        if subjects_count <= 0:
            print("Please enter at least one subject.")
            return

        marks = []
        for i in range(subjects_count):
            while True:
                try:
                    mark = float(input(f"Enter marks for subject {i + 1} (0-100): "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")

        total = sum(marks)
        maximum = subjects_count * 100
        percentage = (total / maximum) * 100
        grade = calculate_grade(percentage)
        result = "Pass" if all(mark >= 35 for mark in marks) else "Fail"

        print("\n" + "-" * 35)
        print("          STUDENT RESULT")
        print("-" * 35)
        print(f"Student name : {name or 'Not provided'}")
        print(f"Total marks  : {total:g} / {maximum}")
        print(f"Percentage   : {percentage:.2f}%")
        print(f"Grade        : {grade}")
        print(f"Result       : {result}")
        print("-" * 35)
    except ValueError:
        print("Please enter a valid whole number for the number of subjects.")


if __name__ == "__main__":
    main()
