"""Student Grade Management System."""

MIN_GRADE = 0
MAX_GRADE = 100
PASSING_AVERAGE = 60
HONOR_ROLL_AVERAGE = 90


class Student:
    """A student with an ID, a name and a list of grades."""

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Add a grade to the student."""
        self.grades.append(grade)

    def calculate_average(self):
        """Return the average of all grades (0 if there are none)."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def pass_status(self):
        """Return 'Passed' or 'Failed'."""
        if self.calculate_average() >= PASSING_AVERAGE:
            return "Passed"
        return "Failed"


    def is_honor_roll(self):
        """Return True if the average is 90 or above."""
        return self.calculate_average() >= HONOR_ROLL_AVERAGE

    def delete_grade(self, index):
        """Delete the grade at the given index."""
        del self.grades[index]

    def report(self):
        """Print a summary of the student."""
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Status: {self.pass_status()}")
        print(f"Honor Roll: {self.is_honor_roll()}")


def main():
    """Run a small demo."""
    student = Student("2021001", "Ana Perez")
    student.add_grade(100)
    student.add_grade(50)
    student.report()


main()