class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def calculate_grade(self):
        if self.gpa >= 3.9:
            return 'A+'
        elif 3.5 <= self.gpa < 3.9:
            return 'A'
        elif 3.0 <= self.gpa < 3.5:
            return 'B'
        elif 2.5 <= self.gpa < 3.0:
            return 'C'
        else:
            return 'F'
    
    # Function to display student information and grade
    def display_student_info(self):
        grade = self.calculate_grade()
        print(f"{self.name}'s Grade: {grade}")
    
    # Function to check if a student is on the honor roll
    def is_honor_roll(self):
        grade = self.calculate_grade()
        return grade >= 'A'  # Consider 'A' and above as honor roll
    
    # Function to congratulate a student on the honor roll
    def congratulate_honor_roll(self):
        if self.is_honor_roll():
            print(f"Congratulations, {self.name}! You made the honor roll.")
    
    # Function to compare two students based on GPA
    @staticmethod
    def compare_students(student1, student2):
        # Display information for both students
        student1.display_student_info()
        student2.display_student_info()
        
        # Compare students based on GPA
        if student1.gpa > student2.gpa:
            return f"{student1.name} has a higher GPA than {student2.name}."
        elif student1.gpa < student2.gpa:
            return f"{student2.name} has a higher GPA than {student1.name}."
        else:
            return "Both students have the same GPA."

def main():
    student1 = Student("Alice", 3.8)
    student2 = Student("Bob", 4.2)
    
    # Display information for student1
    student1.display_student_info()
    
    # Display information for student2
    student2.display_student_info()
    
    # Check if student1 is on the honor roll and congratulate if true
    student1.congratulate_honor_roll()
    
    # Compare students based on GPA
    comparison_result = Student.compare_students(student1, student2)
    print(comparison_result)

if __name__ == "__main__":
    main()
