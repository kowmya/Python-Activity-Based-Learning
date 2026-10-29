Problem Statement
Develop a Python program to analyse production quantities and defective units across multiple products and batches using a matrix (nested list). The program should calculate the defect percentage for each batch and identify batches that exceed a specified quality threshold.

Algorithm

1. Start the program.
2. Read the number of products and batches.
3. Input the production quantity and defective units for each batch.
4. Store the data in nested lists (matrices).
5. Calculate the defect percentage using the formula:
\[
\text{Defect Percentage}=\frac{\text{Defective Units}}{\text{Production Quantity}}\times100
\]
6. Compare each batch's defect percentage with the given quality threshold.
7. If the percentage exceeds the threshold, mark the batch as Above Threshold; otherwise, mark it as Within Threshold.
8. Display the production quantity, defective units, defect percentage, and quality status for every batch.
9. Stop the program.

   
flowchart 
    A([Start]) --> B[/Input number of products, batches and threshold/]
    B --> C[Read production and defective units]
    C --> D[Store data in nested list]
    D --> E[Calculate defect percentage]
    E --> F{Defect percentage > threshold?}
    F -- Yes --> G[Mark as Exceeds Threshold]
    F -- No --> H[Mark as Within Threshold]
    G --> I[Display batch details]
    H --> I
    I --> J{More batches?}
    J -- Yes --> E
    J -- No --> K([Stop])

Sample input

Enter number of products: 2
Enter number of batches per product: 2
Enter defect threshold (%): 5

Product 1
Batch 1 production quantity: 100
Batch 1 defective units: 3
Batch 2 production quantity: 200
Batch 2 defective units: 15

Product 2
Batch 1 production quantity: 150
Batch 1 defective units: 12
Batch 2 production quantity: 100
Batch 2 defective units: 2

sample output

Product 1
Batch 1:
Production Quantity: 100
Defective Units: 3
Defect Percentage: 3.00%
Status: Within Quality Threshold

Batch 2:
Production Quantity: 200
Defective Units: 15
Defect Percentage: 7.50%
Status: Exceeds Quality Threshold

Product 2
Batch 1:
Production Quantity: 150
Defective Units: 12
Defect Percentage: 8.00%
Status: Exceeds Quality Threshold

Batch 2:
Production Quantity: 100
Defective Units: 2
Defect Percentage: 2.00%
Status: Within Quality Threshold

Conclusion

The Manufacturing Quality Control Matrix program uses nested lists, loops, arithmetic operators, and conditional statements to analyse production quality. It calculates the defect percentage for each batch and identifies batches that exceed the specified threshold. This helps manufacturers identify quality problems and improve production processes.
