# Definition of the Teacher class
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    subjects_to_cover = set(subjects)
    assigned_teachers = []

    while subjects_to_cover:
        # Select teacher who can cover the most remaining subjects
        candidates = [
            t for t in teachers if t.can_teach_subjects & subjects_to_cover
        ]
        if not candidates:
            # No teacher can cover remaining subjects
            return None

        # Choose teacher covering the most subjects, break ties by youngest age
        best_teacher = max(candidates, key=lambda t: (len(t.can_teach_subjects & subjects_to_cover), -t.age))
        assigned = best_teacher.can_teach_subjects & subjects_to_cover
        best_teacher.assigned_subjects = assigned
        subjects_to_cover -= assigned
        assigned_teachers.append(best_teacher)

    return assigned_teachers

if __name__ == '__main__':
    # Set of subjects
    subjects = {'Mathematics', 'Physics', 'Chemistry', 'Informatics', 'Biology'}

    # Creating a list of teachers
    teachers = [
        Teacher("Alexander", "Evans", 45, "a.evans@example.com", {'Mathematics', 'Physics'}),
        Teacher("Maria", "Peterson", 38, "m.peterson@example.com", {'Chemistry'}),
        Teacher("George", "Collins", 50, "g.collins@example.com", {'Informatics', 'Mathematics'}),
        Teacher("Natalie", "Stevens", 29, "n.stevens@example.com", {'Biology', 'Chemistry'}),
        Teacher("Daniel", "Brown", 35, "d.brown@example.com", {'Physics', 'Informatics'}),
        Teacher("Helen", "Grant", 42, "h.grant@example.com", {'Biology'})
    ]

    # Calling the function to create the schedule
    schedule = create_schedule(subjects, teachers)

    # Outputting the schedule
    if schedule:
        print("Class Schedule:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} years old, email: {teacher.email}")
            print(f"   Teaches subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("It is impossible to cover all subjects with the available teachers.")