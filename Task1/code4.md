 Problem Statement
Develop a Python program to validate student course registrations stored as tuples. The program identifies duplicate registrations, detects invalid course combinations based on predefined rules, and determines which students have violated the registration rules.

For this example, a student cannot register for the same course twice, and Python Programming and Advanced Python cannot be selected together because they are treated as conflicting courses.

 Algorithm
1. Start the program.
2. Store student registration details as tuples containing student ID and course name.
3. Define the list of valid courses.
4. Define the conflicting course combinations.
5. Check each registration for invalid course names.
6. Identify duplicate registrations for the same student and course.
7. Compare each student's selected courses with the conflicting course rules.
8. Display duplicate registrations, invalid courses, and students who violate the rules.
9. Stop the program.


flowchart TD
    A([Start]) --> B[Store registrations as tuples]
    B --> C[Define valid courses and conflict rules]
    C --> D[Check each registration]
    D --> E{Course valid?}
    E -- No --> F[Record invalid course]
    E -- Yes --> G[Check duplicate registrations]
    F --> G
    G --> H[Group courses by student]
    H --> I[Check conflicting course combinations]
    I --> J[Display duplicates and violations]
    J --> K([Stop]

Sample input:
    Student ID        Course Name
S101              Python Programming
S101              Data Structures
S101              Python Programming
S102              Python Programming
S102              Advanced Python
S103              Web Development
S104              AI Basics


sample output:-

Duplicate Registrations:
S101 - Python Programming

Invalid Course Registrations:
S104 - AI Basics

Invalid Course Combinations:
S102 - Python Programming and Advanced Python

Students Violating Registration Rules:
S104
S101
S102

Explanation:-
- S101: Registered for Python Programming twice, so a duplicate is detected.
- S102: Selected Python Programming and Advanced Python, which form a prohibited combination.
- S103: Registered for Web Development, which is valid.
- S104: Registered for AI Basics, which is not included in the valid course list.
  Conclusion
The Tuple-Based Course Registration Validation program uses tuples, lists, loops, conditional statements, and dictionary operations to validate course registrations. It identifies duplicate registrations, invalid courses, and conflicting course combinations, helping institutions maintain accurate student registration records.
