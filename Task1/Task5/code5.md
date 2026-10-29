 Problem Statement:-
Develop a Python program to analyse students' academic performance using lists of marks, attendance percentages, and laboratory scores. The program classifies students into academic risk categories, identifies multiple risk factors affecting each student, and generates a summary report.

For this example, a student is considered at risk if any of these conditions apply:
- Low marks: less than 40%.
- Low attendance: less than 75%.
- Low laboratory score: less than 40%.
Students with two or more risk factors are classified as High Risk. Students with one risk factor are classified as Moderate Risk, and students with no risk factors are classified as Low Risk.

Algorithm:- 
1. Start the program.
2. Store student names, marks, attendance percentages, and laboratory scores in lists.
3. Initialize counters for High Risk, Moderate Risk, and Low Risk students.
4. Process each student using a for loop.
5. Check whether the student's marks are below 40%.
6. Check whether attendance is below 75%.
7. Check whether the laboratory score is below 40%.
8. Count the number of risk factors for each student.
9. Classify students based on the number of risk factors:
   - Two or more: High Risk.
   - One: Moderate Risk.
   - Zero: Low Risk.
10. Display each student's risk factors and classification.
11. Display the total number of students in each risk category.
12. Stop the program.

    
Flowchart :- 
    A([Start]) --> B[Store student names, marks, attendance and lab scores]
    B --> C[Initialize risk category counters]
    C --> D[Select next student]
    D --> E[Check marks below 40%]
    E --> F[Check attendance below 75%]
    F --> G[Check lab score below 40%]
    G --> H[Count risk factors]
    H --> I{Risk factors >= 2?}
    I -- Yes --> J[Classify as High Risk]
    I -- No --> K{Risk factors = 1?}
    K -- Yes --> L[Classify as Moderate Risk]
    K -- No --> M[Classify as Low Risk]
    J --> N[Display student details and risk factors]
    L --> N
    M --> N
    N --> O{More students?}
    O -- Yes --> D
    O -- No --> P[Display summary of risk categories]
    P --> Q([Stop])

     Sample input:- 
The program uses predefined lists as input.
Student	Marks (%)	Attendance (%)	Lab Score (%)
Ravi	35	60	30
Sita	65	85	55
Arjun	80	90	75
Priya	30	70	25
Kiran	55	80	60

Sample output:-

Student: Ravi
Marks: 35 %
Attendance: 60 %
Lab Score: 30 %
Risk Factors: Low Marks, Low Attendance, Low Lab Score
Category: High Risk

Student: Sita
Marks: 65 %
Attendance: 85 %
Lab Score: 55 %
Risk Factors: None
Category: Low Risk

Student: Arjun
Marks: 80 %
Attendance: 90 %
Lab Score: 75 %
Risk Factors: None
Category: Low Risk

Student: Priya
Marks: 30 %
Attendance: 70 %
Lab Score: 25 %
Risk Factors: Low Marks, Low Attendance, Low Lab Score
Category: High Risk

Student: Kiran
Marks: 55 %
Attendance: 80 %
Lab Score: 60 %
Risk Factors: None
Category: Low Risk

=== Academic Risk Summary ===
Total Students: 5
High Risk Students: 2
Moderate Risk Students: 0
Low Risk Students: 3

Conclusion:- 
The Student Academic Risk Classification program uses lists, loops, conditional statements, and list operations to analyse student performance. It identifies multiple academic risk factors, classifies students into three risk categories, and generates a summary that can help teachers identify students who may need additional academic support.
