# goit-neo-algo2-hw-10

# Task 1. Comparison of Randomized and Deterministic QuickSort



Implement both the randomized and deterministic QuickSort sorting algorithms. Conduct a comparative analysis of their efficiency by measuring the average execution time on arrays of various sizes.



Technical Requirements



For the implementation of the randomized QuickSort algorithm, implement the function randomized_quick_sort(arr), where the pivot element is selected randomly.
For the implementation of the deterministic QuickSort algorithm, implement the function deterministic_quick_sort(arr), where the pivot element is selected according to a fixed rule: first, last, or middle element.
Create a set of test arrays with different sizes: 10_000, 50_000, 100_000, and 500_000 elements. Fill the arrays with random integers.
Measure the execution time of both algorithms on each array. To ensure a more accurate estimate, repeat the sorting of each array five times and calculate the average execution time.


Acceptance Criteria

📌 The acceptance criteria for the homework are mandatory for the mentor’s review of the task.


The functions randomized_quick_sort and deterministic_quick_sort correctly implement the sorting algorithms and sort the arrays (20 points).
The execution time of the algorithms is measured and presented in the form of a table and graph (10 points).
The graphs are plotted with axis labels and a legend (5 points).
A detailed analysis of the results has been carried out, and conclusions have been made regarding the efficiency of the randomized and deterministic QuickSort algorithms (10 points).
The code demonstrates an example usage and produces the expected results (5 points).


Example of graph generation by the program




Example of program execution output in the terminal



Array size: 10000
   Randomized QuickSort: 0.0189 seconds
   Deterministic QuickSort: 0.0189 seconds

Array size: 50000
   Randomized QuickSort: 0.1104 seconds
   Deterministic QuickSort: 0.1090 seconds

Array size: 100000
   Randomized QuickSort: 0.2333 seconds
   Deterministic QuickSort: 0.2435 seconds

Array size: 500000
   Randomized QuickSort: 1.4166 seconds
   Deterministic QuickSort: 1.4815 seconds



# Task 2. Creating a timetable using a greedy algorithm



Implement a program for creating a university timetable using a greedy algorithm for the set cover problem. The goal is to assign lecturers to subjects in such a way that the number of lecturers is minimized while covering all subjects.



Technical Requirements



Given a set of subjects: {'Mathematics', 'Physics', 'Chemistry', 'Informatics', 'Biology'}



List of lecturers:



Alexander Evans, 45 years old, a.evans@example.com, subjects: {'Mathematics', 'Physics'}
Maria Peterson, 38 years old, m.peterson@example.com, subjects: {'Chemistry'}
George Collins, 50 years old, g.collins@example.com, subjects: {'Computer Science', 'Mathematics'}
Natalie Stevens, 29 years old, n.stevens@example.com, subjects: {'Biology', 'Chemistry'}
Daniel Brown, 35 years old, d.brown@example.com, subjects: {'Physics', 'Computer Science'}
Helen Grant, 42 years old, h.grant@example.com, subjects: {'Biology'}


Task Description



Implement a Teacher class with the following attributes:
first_name (first name)
last_name (last name)
age (age)
email (email address)
can_teach_subjects (set of subjects the teacher can teach)
Implement a function create_schedule(subjects, teachers) that uses a greedy algorithm to assign teachers to subjects. The function should return a list of teachers and the subjects assigned to them.
When selecting a teacher at each step, prioritise the teacher who can teach the largest number of remaining subjects. If there are several candidates with the same number of subjects, choose the youngest teacher.




Acceptance Criteria



The program covers all subjects from the set of subjects (20 points).
If it is impossible to cover all subjects with the available teachers, the program should output a message indicating this (15 points).
All subjects should be covered by teachers, and all teachers should be assigned to their respective subjects (15 points).




Program Template



# Definition of the Teacher class
class Teacher:
    pass

def create_schedule(subjects, teachers):
   pass

if __name__ == '__main__':
    # Set of subjects
    subjects = {}
    # Creating a list of teachers
    teachers = []

    # Calling the function to create the schedule
    schedule = create_schedule(subjects, teachers)

    # Outputting the schedule
    if schedule:
        print("Class Schedule:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} years old, email: {teacher.email}")
            print(f"   Teaches subjects: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("It is impossible to cover all subjects with the available teachers.")