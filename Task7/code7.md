Problem Statement :- 
The Multi-Stage Scholarship Shortlisting system selects eligible students for scholarships based on academic marks, attendance, family income, and ranking rules. First, it checks whether each student satisfies the minimum eligibility criteria. Then, it ranks eligible candidates according to their academic marks and selects students within a fixed scholarship quota. Finally, it displays the selected students and the number of scholarships awarded.

Algorithm :- 
1. Start the program.
2. Store the student details, including name, academic marks, attendance percentage, and annual family income.
3. Set the minimum academic marks, minimum attendance, maximum family income, and scholarship quota.
4. Check each student against all eligibility conditions.
5. Add students who satisfy every condition to the eligible candidates list.
6. Sort eligible candidates in descending order of academic marks.
7. Select candidates according to the scholarship quota.
8. Display the selected students and their ranks.
9. Display the number of scholarships awarded.
10. Stop the program


flowchart :-
    A([Start]) --> B[Store student details]
    B --> C[Set eligibility rules and quota]
    C --> D[Check academic marks, attendance and income]
    D --> E{Meets all conditions?}
    E -- Yes --> F[Add student to eligible list]
    E -- No --> G[Reject student]
    F --> H{More students?}
    G --> H
    H -- Yes --> D
    H -- No --> I[Sort eligible students by marks]
    I --> J[Select students within scholarship quota]
    J --> K[Display selected students and ranks]
    K --> L[Display total scholarships awarded]
    L --> M([Stop])

Sample Input :-
The program uses the following student records:
Student	Marks (%)	Attendance (%)	Annual family income (₹)
Ravi	85	90	1,50,000
Sita	92	95	1,80,000
Arjun	70	85	1,00,000
Priya	88	78	1,20,000
Kiran	80	85	1,90,000
Meena	95	92	1,50,000
Rahul	78	82	2,50,000

Sample output :-
Eligibility rules:
- Minimum marks: 75%
- Minimum attendance: 80%
- Maximum annual family income: ₹2,00,000
- Scholarship quota: 3 students

=== Eligible Students ===
Ravi - Marks: 85
Sita - Marks: 92
Kiran - Marks: 80
Meena - Marks: 95

=== Scholarship Selection List ===
Rank: 1 | Name: Meena | Marks: 95 | Attendance: 92% | Family Income: Rs. 150000
Rank: 2 | Name: Sita | Marks: 92 | Attendance: 95% | Family Income: Rs. 180000
Rank: 3 | Name: Ravi | Marks: 85 | Attendance: 90% | Family Income: Rs. 150000

Total Scholarships Awarded: 3
Scholarship Quota: 3


 Conclusion
The Multi-Stage Scholarship Shortlisting program applies academic, attendance, and family-income requirements to identify eligible students. It ranks eligible candidates by academic marks and selects the top three students according to the scholarship quota. This system makes scholarship selection systematic, consistent, and efficient.
