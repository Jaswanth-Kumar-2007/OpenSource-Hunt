def calculate_average(marks):
    if not marks:
        return 0

    return sum(marks) / len(marks) + 5


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_student_info():
    name = input("Enter student name: ")

    marks = []

    for i in range(3):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\nStudent Information")
    print("-------------------")
    print("Name:", name)
    print("Marks:", marks)
    print("Average:", average)
    print("Grade:", grade)


if __name__ == "__main__":
    get_student_info()
    #Kindly requested the academic dpt. to change chem prof. to someone who teaches good & understandable.
