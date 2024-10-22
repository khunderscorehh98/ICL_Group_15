import pandas as pd
import os

def extract_year_from_filename(filename):
    year_part = filename.split('_')[-1].replace('.xlsx', '')
    return year_part

def calculate_yearly_average(broadsheets):
    classification_data = []

    for broadsheet in broadsheets:
        df = pd.read_excel(broadsheet)
        year = extract_year_from_filename(broadsheet)

        if 'Student Name' not in df.columns or 'Marks' not in df.columns:
            print(f"Error: 'Student Name' or 'Marks' column not found in {broadsheet}")
            continue

        grouped = df.groupby('Student Name').agg({'Marks': 'mean'}).reset_index()

        for _, row in grouped.iterrows():
            student_info = {
                'Student Name': row['Student Name'],
                'Yearly Average': row['Marks'],
                'Year': year
            }
            classification_data.append(student_info)

    return classification_data

def save_classification(classification_data, intake):
    df_classification = pd.DataFrame(classification_data)
    
    output_dir = "output_files/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = f"{output_dir}/Classification_{intake}.xlsx"
    df_classification.to_excel(output_file, index=False)
    print(f"Classification saved as {output_file}")
