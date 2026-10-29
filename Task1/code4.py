registrations = [
    (101, "Python"),
    (102, "Java"),
    (101, "Python"),
    (103, "")
]

seen = []

for student, course in registrations:
    if (student, course) in seen:
        print("Duplicate:", student, course)
    elif course == "":
        print("Invalid course for:", student)
    else:
        print("Valid:", student, course)

    seen.append((student, course))
