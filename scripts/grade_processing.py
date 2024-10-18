import pandas as pd

# Function to calculate the yearly average marks from broadsheets
def calculate_yearly_average(broadsheets):
    classification_data = []

    for broadsheet in broadsheets:
        df = pd.read_excel(broadsheet)
        year = extract_year_from_filename(broadsheet)  # Assuming this function is defined elsewhere.

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
    output_file = f"output_files/Classification_{intake}.xlsx"
    df_classification.to_excel(output_file, index=False)
    print(f"Classification saved as {output_file}")
