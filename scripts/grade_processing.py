import pandas as pd
import os

# Function to classify students based on the consolidated broadsheet
def classify_students_from_broadsheet(broadsheet_df, intake):
    classification_data = []

    # Group by student name and calculate the average marks
    grouped = broadsheet_df.groupby('Student Name').agg({'Total Marks': 'mean'}).reset_index()

    # Classify students based on their average marks
    for _, row in grouped.iterrows():
        student_info = {
            'Student Name': row['Student Name'],
            'Yearly Average': row['Total Marks'],
        }

        avg = row['Total Marks']
        if avg >= 70:
            student_info['Classification'] = 'First Class'
        elif avg >= 60:
            student_info['Classification'] = 'Second Class Upper'
        elif avg >= 50:
            student_info['Classification'] = 'Second Class Lower'
        elif avg >= 40:
            student_info['Classification'] = 'Third Class'
        else:
            student_info['Classification'] = 'Fail'

        classification_data.append(student_info)

    # Convert the classification data to a DataFrame
    classification_df = pd.DataFrame(classification_data)

    # Save the classification data to "Classification M1_01.xlsx"
    output_file = 'input/Classification M1_01.xlsx'
    classification_df.to_excel(output_file, index=False)
    print(f"Classification saved to {output_file}")

    return classification_df