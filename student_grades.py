"""Student Grade Management System."""

MIN_GRADE = 0
MAX_GRADE = 100
PASSING_AVERAGE = 60
HONOR_ROLL_AVERAGE = 90
LETTER_THRESHOLDS = ((90, "A"), (80, "B"), (70, "C"), (60, "D"))


class Student:
    """A student with an ID, a name and a list of grades."""

    def __init__(self, student_id, name):
        if not str(student_id).strip():
            raise ValueError("Student ID cannot be empty.")
        if not str(name).strip():
            raise ValueError("Student name cannot be empty.")
        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.grades = []

    def add_grade(self, grade):
        """Add a numeric grade between 0 and 100."""
        try:
            grade = float(grade)
        except (TypeError, ValueError) as error:
            raise ValueError(f"Grade {grade!r} is not a number.") from error
        if not MIN_GRADE <= grade <= MAX_GRADE:
            raise ValueError(f"Grade {grade} must be between 0 and 100.")
        self.grades.append(grade)

    def remove_grade_by_value(self, value):
        """Remove the first grade equal to value."""
        if value not in self.grades:
            raise ValueError(f"Grade {value} does not exist.")
        self.grades.remove(value)

    def remove_grade_by_index(self, index):
        """Remove the grade at the given index (starts at 0)."""
        if not 0 <= index < len(self.grades):
            raise ValueError(f"Index {index} is out of bounds.")
        del self.grades[index]

    def calculate_average(self):
        """Return the average of all grades (0 if there are none)."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        """Return the letter grade (A, B, C, D or F)."""
        average = self.calculate_average()
        for threshold, letter in LETTER_THRESHOLDS:
            if average >= threshold:
                return letter
        return "F"

    def pass_status(self):
        """Return 'Passed' or 'Failed'."""
        if self.calculate_average() >= PASSING_AVERAGE:
            return "Passed"
        return "Failed"

    def is_honor_roll(self):
        """Return True if the average is 90 or above."""
        return self.calculate_average() >= HONOR_ROLL_AVERAGE

    def generate_report(self):
        """Return a formatted summary report of the student."""
        return (
            f"Student ID: {self.student_id}\n"
            f"Student Name: {self.name}\n"
            f"Number of Grades: {len(self.grades)}\n"
            f"Average Grade: {self.calculate_average():.2f}\n"
            f"Letter Grade: {self.letter_grade()}\n"
            f"Status: {self.pass_status()}\n"
            f"Honor Roll: {self.is_honor_roll()}"
        )


def main():
    """Demonstrate the system, including invalid inputs."""
    try:
        Student("", "")
    except ValueError as error:
        print(f"Error: {error}")

    student = Student("2021001", "Ana Perez")
    for grade in (100, "Fifty", 150, 85.5, 72.5):
        try:
            student.add_grade(grade)
        except ValueError as error:
            print(f"Error: {error}")

    try:
        student.remove_grade_by_index(5)
    except ValueError as error:
        print(f"Error: {error}")
    try:
        student.remove_grade_by_value(33)
    except ValueError as error:
        print(f"Error: {error}")

    student.remove_grade_by_value(72.5)
    print(student.generate_report())


if __name__ == "__main__":
    main()
