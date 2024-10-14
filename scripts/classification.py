import pandas as pd

def calculateyearly_average(broadsheets):
    """Calculate yearly average for each intake."""
    classification_data = []

    for broadsheet in broadsheets:
        df = pd.read_excel(broadsheet)
        year = extract_year_from_filename(broadsheet)


        grouped = df.groupby('Student Name').agg({'Total Marks': 'mean'}).reset_index()
        for , row in grouped.iterrows():
            studentinfo = {
                'Student Name': row['Student Name'],
                'Yearly Average': row['Total Marks'],
                'Year': year
            }
            classification_data.append(student_info)

    return classification_data

def classify_students(classification_data):
    """Assign classifications based on average scores."""
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

def save_classification(classification_data, intake):
    """Save classification data to an Excel file."""
    df_classification = pd.DataFrame(classification_data)
    output_file = f"Classification{intake}.xlsx"
    df_classification.to_excel(output_file, index=False)
    print(f"Classification file saved as {output_file}")
def main():
    # Example usage
    broadsheets = ['BroadsheetM120241.xlsx', 'BroadsheetM1_2024_2.xlsx']  # Update with actual files
    intake = '2024'

    classification_data = calculate_yearly_average(broadsheets)
    classified_students = classify_students(classification_data)
    save_classification(classified_students, intake)

if __name == '__main':
    main()