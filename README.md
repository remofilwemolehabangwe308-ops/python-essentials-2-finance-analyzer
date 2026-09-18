# Python Finance Transaction Analyzer

## Description
The Personal Finance Transaction Analyser is the Python application that reads the messy bank statement, cleans and validates transaction data, tracks running balances, analyses income and expenses by category, detects duplicate and unusual transactions, and generates a monthly summary report.This project aims to use concepts such as OOP, generators, closures, exception handling, file handling, and modules in Python Standard Library, all within the framework of the challenges of safely working with messy real-world data.

**Author:** Remofilwe Molehabangwe
**Cohort:** Data Science Practitioner, Jan 2026 - Melsoft Academy

## Features
1. Generate a messy sample statement file
2. Load and validate transactions
3. Display running balance
4. Show category breakdown
5. Detect duplicate transactions
6. Detect statistical outliers
7. Generate a monthly summary report
8. Run self-tests
9. Exit 

## How to run
1. Clone the repository.
2. Open the project folder in the terminal.
3. Install the requirements if needed: pip install -r requirements.txt
4. Run the program: /python main.py``
5. Run the program: /python tests.py``

## Project Structure
1. models.py - Transaction classes
2. parser.py - generates, loads, clean and validates transaction data
3. analytics.py - running balance, categories, duplicates and outliers
4. reporting.py - creates the monthly report and activity log
5. tests.py - tests the different functions
6. main.py - menu and connects everything together

## Concepts Demonstrated
This project demonstrates:
- Object - Oriented Programming
- File handling and data processing
- String cleaning and data validation
- Exception handling with (try-except)
- Generators using yield
- Closures
- Sets and tuples for duplicate detection
- Statistical calculations using mean and standard deviation
- Python Standard Library modules

## Edge Cases Handled
The analyser is designed to safely handle:
- Incorrect date separators and date normalization
- Missing fields or too few fields
- Completely invalid or junk lines
- Non-numeric transaction amounts
- Duplicate transactions
- Income and expenses sign/category mismatches
- Empty statement files
- Missing statement files
- Extra whitespace in transaction data

## Sample Output
=== Personal Finance Transaction Analyzer ===
1. Generate sample statement
2. Loads transactions
3. Show running balance
4. Show category breakdown
5. Find duplicates
6. Find outliers
7. Generate monthly report
8. Run self-test
9. Exit

Enter option: 4 
Income  15000.0
Food -850.0
Transport -450.0
Entertainment -200.0
Bills -1200.0


 
