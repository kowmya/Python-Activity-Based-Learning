Problem Statement :- 
The Smart Electricity Billing system calculates electricity bills for multiple apartments based on their monthly electricity consumption. It applies progressive tariff rates, fixed charges, and rebates to calculate the final bill for each apartment. The program also identifies billing discrepancies by comparing the calculated bill with the recorded bill and ranks apartments according to their electricity consumption from highest to lowest.

Algorithm
1. Start the program.
2. Store apartment numbers, electricity consumption, and recorded bills.
3. Define the progressive tariff rates, fixed charges, and rebate rules.
4. Calculate the electricity charge using the applicable tariff slabs.
5. Add fixed charges to the electricity charge.
6. Apply a rebate if the apartment qualifies.
7. Calculate the final bill amount.
8. Compare the calculated bill with the recorded bill to identify discrepancies.
9. Display the apartment-wise billing report.
10. Sort apartments by electricity consumption in descending order.
11. Display the consumption ranking.
12. Stop the program


flowchart TD
    A([Start]) --> B[Store apartment records]
    B --> C[Set tariff slabs, fixed charge and rebate]
    C --> D[Read apartment consumption]
    D --> E[Calculate progressive tariff charge]
    E --> F[Add fixed charges]
    F --> G{Eligible for rebate?}
    G -- Yes --> H[Subtract rebate]
    G -- No --> I[Keep bill without rebate]
    H --> J[Calculate final bill]
    I --> J
    J --> K[Compare calculated and recorded bills]
    K --> L[Report any discrepancy]
    L --> M{More apartments?}
    M -- Yes --> D
    M -- No --> N[Display apartment-wise bill report]
    N --> O[Rank apartments by consumption]
      O --> P[Display ranking]
    P --> Q([Stop])

    Sample input :- 
Apartment	Units consumed	Recorded bill (₹)
A101	80	210
A102	150	450
A103	250	1,000
A104	90	230
A105	320	1,400

The recorded bills are sample values used to demonstrate discrepancy detection.

sample output :- 
  ===== SMART ELECTRICITY BILLING REPORT =====

Apartment: A101
Units Consumed: 80
Energy Charge: Rs. 160
Fixed Charge: Rs. 50
Rebate: Rs. 16
Calculated Bill: Rs. 194
Recorded Bill: Rs. 210
Difference: Rs. 16
Billing Status: DISCREPANCY FOUND

Apartment: A102
Units Consumed: 150
Energy Charge: Rs. 350
Fixed Charge: Rs. 50
Rebate: Rs. 0
Calculated Bill: Rs. 400
Recorded Bill: Rs. 450
Difference: Rs. 50
Billing Status: DISCREPANCY FOUND

Apartment: A103
Units Consumed: 250
Energy Charge: Rs. 750
Fixed Charge: Rs. 50
Rebate: Rs. 0
Calculated Bill: Rs. 800
Recorded Bill: Rs. 1000
Difference: Rs. 200
Billing Status: DISCREPANCY FOUND

Apartment: A104
Units Consumed: 90
Energy Charge: Rs. 180
Fixed Charge: Rs. 50
Rebate: Rs. 18
Calculated Bill: Rs. 212
Recorded Bill: Rs. 230
Difference: Rs. 18
Billing Status: DISCREPANCY FOUND

Apartment: A105
Units Consumed: 320
Energy Charge: Rs. 1100
Fixed Charge: Rs. 50
Rebate: Rs. 0
Calculated Bill: Rs. 1150
Recorded Bill: Rs. 1400
Difference: Rs. 250
Billing Status: DISCREPANCY FOUND

===== APARTMENT CONSUMPTION RANKING =====
1 A105 - 320 units
2 A103 - 250 units
3 A102 - 150 units
4 A104 - 90 units
5 A101 - 80 units

===== SUMMARY =====
Total Apartments: 5
Apartments with Discrepancies: 5
Verified Apartments: 0

Units Consumed: 250
Energy Charge: Rs. 750
Fixed Charge: Rs. 50
Rebate: Rs. 0
Calculated Bill: Rs. 800
Recorded Bill: Rs. 1000
Difference: Rs. 200
Billing Status: DISCREPANCY FOUND

Apartment: A104
Units Consumed: 90
Energy Charge: Rs. 180
Fixed Charge: Rs. 50
Rebate: Rs. 18
Calculated Bill: Rs. 212
Recorded Bill: Rs. 230
Difference: Rs. 18
Billing Status: DISCREPANCY FOUND

Apartment: A105
Units Consumed: 320
Energy Charge: Rs. 1100
Fixed Charge: Rs. 50
Rebate: Rs. 0
Calculated Bill: Rs. 1150
Recorded Bill: Rs. 1400
Difference: Rs. 250
Billing Status: DISCREPANCY FOUND

===== APARTMENT CONSUMPTION RANKING =====
1 A105 - 320 units
2 A103 - 250 units
3 A102 - 150 units
4 A104 - 90 units
5 A101 - 80 units

===== SUMMARY =====
Total Apartments: 5
Apartments with Discrepancies: 5
Verified Apartments: 0

Conclusion
The Smart Electricity Billing program calculates apartment-wise electricity charges using progressive tariff slabs, fixed charges, and rebates. It compares calculated bills with recorded amounts to identify discrepancies and ranks apartments by electricity consumption. This system supports accurate billing, transparent reporting, and easier identification of unusually high electricity usage.
