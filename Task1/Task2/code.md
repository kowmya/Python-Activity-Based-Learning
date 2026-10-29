Problem statement:- 
Water is supplied to different areas over several days, but the quantity supplied may be less than the actual demand. The aim of this program is to analyse area-wise water supply using a nested list (matrix), calculate the shortage of water for each area on each day, compare the distribution levels, and identify the most underserved area.
The program calculates the total demand, total supply, water shortage, and shortage percentage for each area.

 Algorithm:-
1. Start the program.
2. Read the number of areas and number of days.
3. Input the water demand and actual water supply for each area on each day.
4. Store the data in nested lists.
5. Calculate the shortage using:
\[
\text{Shortage}=\text{Demand}-\text{Supply}
\]

   If supply exceeds demand, shortage is considered zero.
6. Calculate the total demand and total supply for each area.
7. Calculate the shortage percentage for each area.
8. Compare the shortage percentages to identify the most underserved area.
9. Display the results.
10. Stop the program.

Flowchart :-
    Start
Input number of areas anddays
Input demand and supply foreach area and day
Store values in nested lists
Calculate shortage for eachday
Calculate area-wise totaldemand and supply
Calculate shortage percentage
Identify the most underservedarea
Display area-wise results
      Stop
      
   Sample input :-
Enter number of areas: 3
Enter number of days: 2

Area 1
Day 1 demand (litres): 100
Day 1 supply (litres): 80
Day 2 demand (litres): 120
Day 2 supply (litres): 100

Area 2
Day 1 demand (litres): 150
Day 1 supply (litres): 140
Day 2 demand (litres): 150
Day 2 supply (litres): 130

Area 3
Day 1 demand (litres): 80
Day 1 supply (litres): 50
Day 2 demand (litres): 100
Day 2 supply (litres): 60

 Sample output :-

Area 1
Total Demand: 220.00 litres
Total Supply: 180.00 litres
Total Shortage: 40.00 litres
Shortage Percentage: 18.18%

Area 2
Total Demand: 300.00 litres
Total Supply: 270.00 litres
Total Shortage: 30.00 litres
Shortage Percentage: 10.00%

Area 3
Total Demand: 180.00 litres
Total Supply: 110.00 litres
Total Shortage: 70.00 litres
Shortage Percentage: 38.89%

Most Underserved Area: Area 3
Shortage Percentage: 38.89%


 Conclusion:- 
The Water Distribution Fairness Analysis program uses nested lists, loops, arithmetic operations, and conditional statements to compare water demand and supply across different areas and days. It calculates shortages and identifies Area 3 as the most underserved area in the sample data. This analysis can help authorities identify areas that need better water distribution.
