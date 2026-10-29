Problem Statement :-
The Integrated University Fee and Eligibility Audit system combines student fee payment details, attendance percentages, internal marks, and examination eligibility records. It identifies students who have outstanding fees, insufficient attendance, low internal marks, or incomplete examination eligibility requirements. The program generates a reason-wise report showing each student's outstanding conditions and determines whether the student is eligible for examinations based on the specified rules.

 Algorithm :- 
1. Start the program.
2. Store student details, including name, fee due, attendance percentage, internal marks, and examination form status.
3. Set the minimum attendance and internal marks requirements.
4. Check each student's fee payment status.
5. Check whether attendance meets the minimum requirement.
6. Check whether internal marks meet the minimum requirement.
7. Check whether the examination form has been submitted.
8. Record every outstanding condition for each student.
9. If no outstanding conditions exist, mark the student as eligible; otherwise, mark the student as having pending requirements.
10. Display a reason-wise audit report.
11. Display the total number of eligible students and students with pending requirements.
12. Stop the program.


flowchart TD
    A([Start]) --> B[Store student records]
    B --> C[Set attendance and marks requirements]
    C --> D[Read a student's fee, attendance, marks and form status]
    D --> E[Check outstanding fees]
    E --> F[Check attendance requirement]
    F --> G[Check internal marks requirement]
    G --> H[Check examination form submission]
    H --> I[Record all outstanding reasons]
    I --> J{Any outstanding condition?}
    J -- Yes --> K[Mark requirements pending]
    J -- No --> L[Mark examination eligible]
    K --> M{More students?}
    L --> M
    M -- Yes --> D
    M -- No --> N[Generate reason-wise audit report]
    N --> O[Display eligibility summary]
    O --> P([Stop])

    
Sample Input :- 
The program uses these sample student records:
Student	Total fee (₹)	Fee paid (₹)	Attendance	Internal marks	Form submitted
Ravi	50,000	50,000	85%	65	Yes
Sita	50,000	40,000	90%	70	Yes
Arjun	50,000	50,000	65%	55	Yes
Priya	50,000	50,000	80%	30	Yes
Kiran	50,000	50,000	82%	60	No
Meena	50,000	30,000	60%	25	No

Audit rules:
- Minimum attendance: 75%.
- Minimum internal marks: 40.
- Outstanding fees must be paid.
- The examination form must be submitted.

Sample output :- 
  ===== UNIVERSITY FEE AND ELIGIBILITY AUDIT =====

Student: Ravi
Status: EXAMINATION ELIGIBLE
Outstanding Conditions: None

Student: Sita
Status: REQUIREMENTS PENDING
Outstanding Conditions:
- Outstanding fee: Rs. 10000

Student: Arjun
Status: REQUIREMENTS PENDING
Outstanding Conditions:
- Low attendance: 65%

Student: Priya
Status: REQUIREMENTS PENDING
Outstanding Conditions:
- Low internal marks: 30

Student: Kiran
Status: REQUIREMENTS PENDING
Outstanding Conditions:
- Examination form not submitted

Student: Meena
Status: REQUIREMENTS PENDING
Outstanding Conditions:
- Outstanding fee: Rs. 20000
- Low attendance: 60%
- Low internal marks: 25
- Examination form not submitted

===== AUDIT SUMMARY =====
Total Students: 6
Eligible Students: 1
Students with Pending Conditions: 5

===== REASON-WISE SUMMARY =====
Outstanding fee: 2
Low attendance: 2
Low internal marks: 2
Examination form not submitted: 2

Conclusion :- 
The Integrated University Fee and Eligibility Audit program checks fee payments, attendance, internal marks, and examination form submission in a single system. It identifies all pending requirements for each student and generates a reason-wise summary. This helps university staff review student records efficiently and identify issues that need attention before examinations.

Note: The eligibility thresholds in this example are sample values. Actual examination eligibility should follow the university's official rules.
