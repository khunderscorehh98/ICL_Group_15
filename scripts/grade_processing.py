import pandas as pd
import os

# Function to extract the year from the filename
def extract_year_from_filename(filename):
    return filename.split('_')[2][-1]  # Adjust this logic based on your file naming convention.

# Function to calculate the yearly average marks from broadsheets
def calculate_yearly_average(broadsheets):
    classification_data = []

    for broadsheet in broadsheets:
        df = pd.read_excel(broadsheet)

        # Ensure the file has the necessary columns
        if 'Student Name' not in df.columns or 'Marks' not in df.columns:
            print(f"Error: 'Student Name' or 'Marks' column not found in {broadsheet}")
            continue

        # Extract year from the filename
        year = extract_year_from_filename(broadsheet)

        # Group by student name and calculate the mean of their marks
        grouped = df.groupby('Student Name').agg({'Marks': 'mean'}).reset_index()

        # Append student info
        for _, row in grouped.iterrows():
            student_info = {
                'Student Name': row['Student Name'],
                'Yearly Average': row['Marks'],
                'Year': year
            }
            classification_data.append(student_info)

    return classification_data

# Function to classify students based on their yearly average marks
def classify_students_logic(classification_data):
    for student in classification_data:
        avg = student['Yearly Average']
        if avg >= 70:
            student['Classification'] = 'First Class'
        elif avg >= 60:
            student['Classification'] = 'Second Class Upper'
        elif avg >= 50:
            student['Classification'] = 'Second Class Lower'
        elif avg >= 40:
            student['Classification'] = 'Third Class'
        else:
            student['Classification'] = 'Fail'

    return classification_data

# Function to save the classified students to an Excel file
def save_classification(classification_data, intake):
    df_classification = pd.DataFrame(classification_data)

    # Ensure the output directory exists
    output_dir = "output_files/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the classification data to an Excel file
    output_file = f"{output_dir}/Classification_{intake}.xlsx"
    df_classification.to_excel(output_file, index=False)
    print(f"Classification saved as {output_file}")

# Function to process grades, this is the missing function in your error
def process_grades_logic(broadsheets):
    # Step 1: Calculate yearly averages
    classification_data = calculate_yearly_average(broadsheets)

    # Step 2: Classify students based on their yearly averages
    classified_data = classify_students_logic(classification_data)

    # Step 3: Save the classification to an output file
    return classified_data
