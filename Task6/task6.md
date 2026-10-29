Problem Statement:- 
Develop a Python program to compare appliance-wise electricity consumption before and after an energy conservation intervention. The program calculates the electricity saved by each appliance, determines the savings percentage, and ranks appliances according to their achieved savings.

The program uses lists, loops, arithmetic operators, and conditional statements to identify which appliances have achieved the greatest reduction in electricity consumption.

 Algorithm
1. Start the program.
2. Store appliance names in a list.
3. Store electricity consumption before and after the intervention in separate lists, measured in kWh.
4. Calculate electricity saved for each appliance:
\[
\text{Energy Saved}=\text{Before Usage}-\text{After Usage}
\]
5. Calculate the savings percentage:
\[
\text{Savings \%}=\frac{\text{Energy Saved}}{\text{Before Usage}}\times100
\]
6. Display each appliance's original usage, new usage, energy saved, and savings percentage.
7. Rank appliances from highest to lowest energy savings.
8. Display the ranked results.
9. Stop the program.


flowchart TD
    A([Start]) --> B[Store appliance names and energy usage]
    B --> C[Read before and after consumption lists]
    C --> D[Calculate energy saved for each appliance]
    D --> E[Calculate savings percentage]
    E --> F[Store appliance savings results]
    F --> G{More appliances?}
    G -- Yes --> D
    G -- No --> H[Sort appliances by energy saved]
    H --> I[Display savings report and ranking]
    I --> J([Stop])

Sample Input:- 
The program uses predefined lists, so keyboard input is not required.
Appliance	Before (kWh)	After (kWh)
Fan	120	80
AC	300	210
Light	100	60
Refrigerator	200	180

Sample output:- 

Appliance: Fan
Before Usage: 120 kWh
After Usage: 80 kWh
Energy Saved: 40 kWh
Savings Percentage: 33.33 %

Appliance: AC
Before Usage: 300 kWh
After Usage: 210 kWh
Energy Saved: 90 kWh
Savings Percentage: 30.0 %

Appliance: Light
Before Usage: 100 kWh
After Usage: 60 kWh
Energy Saved: 40 kWh
Savings Percentage: 40.0 %

Appliance: Refrigerator
Before Usage: 200 kWh
After Usage: 180 kWh
Energy Saved: 20 kWh
Savings Percentage: 10.0 %

=== Appliance Savings Ranking ===
1 AC - Energy Saved: 90 kWh - Savings: 30.0 %
2 Fan - Energy Saved: 40 kWh - Savings: 33.33 %
3 Light - Energy Saved: 40 kWh - Savings: 40.0 %
4 Refrigerator - Energy Saved: 20 kWh - Savings: 10.0 %

Conclusion
The Energy Conservation Before-and-After Analysis program compares electricity consumption before and after an intervention. It calculates energy savings and savings percentages, ranks appliances by the amount of energy saved, and calculates overall electricity savings. In this example, 190 kWh of electricity is saved, representing an overall reduction of 26.39%.

=== Overall Summary ===
Total Before Usage: 720 kWh
Total After Usage: 530 kWh
Total Energy Saved: 190 kWh
Overall Savings: 26.39 %
