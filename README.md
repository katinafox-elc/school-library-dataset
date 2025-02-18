# School Library Dataset Analysis

## Overview
In this project, you'll analyze a school library dataset to understand book checkout patterns and practice fundamental data analysis skills using Python. You'll work with real-world data similar to what school librarians use to track book circulation and make inventory decisions.

## Learning Objectives
By completing this project, you will:
- Import and read CSV files using pandas
- Clean and prepare data for analysis
- Create basic data visualizations
- Write functions to process data
- Apply basic statistical concepts
- Practice core Python programming concepts:
  - Variables and data types
  - Conditional statements
  - Functions
  - List and dictionary operations
  - String manipulation

## Dataset Description
The `library_data.csv` file contains the following columns:
- `book_id`: Unique identifier for each book (string)
- `title`: Book title (string)
- `author`: Author name (string)
- `genre`: Book genre/category (string)
- `publication_year`: Year of publication (integer)
- `checkout_date`: Date the book was checked out (datetime)
- `return_date`: Date the book was returned (datetime)
- `student_grade`: Grade level of student who checked out the book (integer)
- `condition_rating`: Book condition at return (integer, 1-5 scale)

## Step-by-Step Tasks

### Part 1: Data Import and Exploration (15 points)
1. Import the required libraries (pandas, matplotlib)
2. Read the CSV file into a pandas DataFrame
3. Display the first 5 rows of the dataset
4. Check basic information about the dataset (data types, missing values)
5. Print the shape of the DataFrame

### Part 2: Data Cleaning (25 points)
1. Create a function to check for missing values in each column
2. Handle missing values appropriately:
   - Remove rows where book_id is missing
   - Fill missing condition_ratings with the median value
   - Fill missing return_dates with 'Not Returned'
3. Convert date columns to datetime format
4. Create a function to standardize author names (remove extra spaces, standardize case)
5. Create a function to validate grade levels (should be between 9-12)

### Part 3: Basic Analysis (30 points)
1. Calculate the total number of books checked out
2. Find the most popular genres (create a frequency table)
3. Calculate average condition ratings by genre
4. Create a function to calculate the checkout duration for each book
5. Identify books that are currently overdue
6. Find the most active grade level in terms of checkouts

### Part 4: Visualization (30 points)
1. Create a bar chart showing the number of checkouts by genre
2. Create a line plot showing checkouts over time
3. Create a box plot of condition ratings by genre
4. Plot the distribution of checkout duration
5. Save all visualizations as PNG files

## Submission Instructions

### Required Files
Your submission should include:
- `library_analysis.py`: Your Python script containing all code
- `analysis_results.txt`: Text file containing your findings
- Generated visualization PNG files
- (Optional) Any additional analysis or visualizations you created

### How to Submit
1. Fork this repository
2. Clone your forked repository to your local machine
3. Create a new branch named `project-submission`
4. Add your files to the branch
5. Commit your changes with meaningful commit messages
6. Push your changes to GitHub
7. Create a Pull Request from your `project-submission` branch to the main repository

### Code Style Requirements
- Use clear, descriptive variable names
- Include comments explaining your code
- Follow PEP 8 style guidelines
- Each function should have a docstring explaining:
  - Purpose of the function
  - Parameters
  - Return values
  - Example usage

## Grading Rubric
Total Points: 100
- Part 1: 15 points
- Part 2: 25 points
- Part 3: 30 points
- Part 4: 30 points

Bonus Points (up to 10):
- Creating additional meaningful visualizations
- Implementing error handling in functions
- Adding input validation
- Writing unit tests for functions

## Getting Help
- Use the GitHub Issues tab for technical questions
- Reference the provided resources in the course materials
- Attend office hours for conceptual questions
- Check the FAQ document for common issues
