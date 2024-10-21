import pandas as pd
import os

# Function to extract the year from the filename (modify this to suit your filename structure)
def extract_year_from_filename(filename):
    # Assuming the filename is like "Broadsheet_M1_02_Y2.xlsx"
    # Extract the "Y2" or just the "2" part
    year_part = filename.split('_')[-1].replace('.xlsx', '')  # This extracts the last part like "Y2"
    return year_part  # Or modify to return just the number, e.g., year_part[-1]

# Function to calculate the yearly average marks from broadsheets
def calculate_yearly_average(broadsheets):
    classification_data = []

    for broadsheet in broadsheets:
        df = pd.read_excel(broadsheet)
        
        # Extract the year from the filename using the defined function
        year = extract_year_from_filename(broadsheet)

        # Ensure the columns "Student Name" and "Marks" exist in the dataframe
        if 'Student Name' not in df.columns or 'Marks' not in df.columns:
            print(f"Error: 'Student Name' or 'Marks' column not found in {broadsheet}")
            continue

        # Group by 'Student Name' and calculate the average 'Marks'
        grouped = df.groupby('Student Name').agg({'Marks': 'mean'}).reset_index()

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
    
    # Ensure output directory exists
    output_dir = "output_files/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = f"{output_dir}/Classification_{intake}.xlsx"
    df_classification.to_excel(output_file, index=False)
    print(f"Classification saved as {output_file}")
