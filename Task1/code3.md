Problem Statement
Develop a Python program to calculate the percentage change in prices of different products by comparing their old and new prices. The program should display the price change for each product and identify products whose prices have increased by more than 20%.

Algorithm
1. Start the program.
2. Store product names, old prices, and new prices in separate lists.
3. Use a for loop to process each product.
4. Calculate the percentage price change using the formula:
\[
\text{Price Change (\%)} =
\frac{\text{New Price}-\text{Old Price}}{\text{Old Price}}\times100
\]

5. Display the product name and percentage change.
6. Check whether the price increase is greater than 20%.
7. If true, display High price increase.
8. Repeat for all products.
9. Stop the program.

    
flowchart TD
    A([Start]) --> B[Store product names and prices in lists]
    B --> C[Set i = 0]
    C --> D{More products?}
    D -- Yes --> E[Calculate percentage price change]
    E --> F[Display product and price change]
    F --> G{Change > 20%?}
    G -- Yes --> H[Display High Price Increase]
    G -- No --> I[Continue]
    H --> I
    I --> J[Increment i]
    J --> D
    D -- No --> K([Stop])
    
Sample input:-
Products:     ["Book", "Bag", "Pen"]
Old prices:   [100, 500, 20]
New prices:   [130, 550, 25]
Threshold:    20%

Sample output:-
Book Change: 30.0 %
High price increase
Bag Change: 10.0 %
Pen Change: 25.0 %
High price increase

Conclusion:-
The program uses lists, a for loop, arithmetic operators, and an if statement to calculate product price changes. It identifies the Book and Pen as products with price increases greater than 20%.
