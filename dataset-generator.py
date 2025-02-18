"""
Library Dataset Generator

This script generates a sample dataset for the School Library Analysis project.
It creates realistic library checkout data with intentional quality issues for students to clean.

The generated dataset includes:
- 1000 records
- 200 unique books
- Date range: August 2023 - February 2024
- Intentional data quality issues for learning purposes
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_library_data(output_file='library_data.csv', n_records=1000, seed=42):
    """
    Generate sample library checkout data and save to CSV.
    
    Parameters:
    -----------
    output_file : str
        Name of the output CSV file
    n_records : int
        Number of records to generate
    seed : int
        Random seed for reproducibility
    """
    # Set random seed
    np.random.seed(seed)
    
    # Sample data
    genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Mystery', 'Biography', 
              'Historical Fiction', 'Reference', 'Poetry']
    conditions = [1, 2, 3, 4, 5]
    
    # Generate book IDs (200 unique books)
    book_ids = [f'BK{str(i).zfill(4)}' for i in range(1, 201)]
    
    # Sample titles and authors (with intentional messiness)
    titles = [
        'To Kill a Mockingbird', 'The Great Gatsby', '1984', 'Pride and Prejudice',
        'The Catcher in the Rye', 'Lord of the Flies', 'Animal Farm', 'Brave New World',
        'The Hobbit', 'Fahrenheit 451'
    ] * 20  # Multiply to have enough titles
    
    authors = [
        'Harper Lee', 'F. Scott  Fitzgerald', 'George Orwell', 'Jane   Austen',
        'J.D. Salinger', 'william Golding', 'George  Orwell', 'Aldous HUXLEY',
        'J.R.R. Tolkien', 'Ray  Bradbury'
    ] * 20  # Multiply to have enough authors
    
    # Generate dates within current school year
    start_date = datetime(2023, 8, 1)
    end_date = datetime(2024, 2, 17)
    date_range = (end_date - start_date).days
    
    # Create base dataset
    data = {
        'book_id': np.random.choice(book_ids, n_records),
        'title': np.random.choice(titles, n_records),
        'author': np.random.choice(authors, n_records),
        'genre': np.random.choice(genres, n_records),
        'publication_year': np.random.randint(1950, 2024, n_records),
        'checkout_date': [start_date + timedelta(days=np.random.randint(0, date_range)) 
                         for _ in range(n_records)],
        'student_grade': np.random.choice([9, 10, 11, 12], n_records)
    }
    
    # Add return dates (10% of books not returned)
    data['return_date'] = [
        checkout + timedelta(days=np.random.randint(7, 45)) 
        if np.random.random() < 0.9 else None
        for checkout in data['checkout_date']
    ]
    
    # Add condition ratings (5% missing)
    data['condition_rating'] = [
        np.random.choice(conditions) 
        if np.random.random() < 0.95 else None
        for _ in range(n_records)
    ]
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add data quality issues:
    # 1. Missing book_ids (2%)
    df.loc[np.random.choice(df.index, int(n_records * 0.02)), 'book_id'] = None
    
    # 2. Invalid grade levels (1%)
    df.loc[np.random.choice(df.index, int(n_records * 0.01)), 'student_grade'] = 13
    
    # 3. Extra spaces in author names (already included)
    # 4. Inconsistent capitalization (already included)
    
    # Sort by checkout date
    df = df.sort_values('checkout_date')
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    
    return df

if __name__ == "__main__":
    # Generate the dataset
    df = generate_library_data()
    
    # Print summary statistics
    print("\nDataset Summary:")
    print("-" * 50)
    print(f"Total records: {len(df)}")
    print(f"Unique books: {df['book_id'].nunique()}")
    print(f"Date range: {df['checkout_date'].min().date()} to {df['checkout_date'].max().date()}")
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nSample of the data:")
    print(df.head())
