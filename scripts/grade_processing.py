import pandas as pd
import traceback

# Function to classify students from a broadsheet
def classify_students_from_broadsheet(broadsheet_df):
    try:
        classification_data = []

        # Ensure the "Total Marks" column is available for classification
        if 'Total Marks' not in broadsheet_df.columns:
            print(f"Error: 'Total Marks' column not found in the broadsheet. Available columns: {broadsheet_df.columns}")
            return None

        # Group by student name and calculate their yearly average
        grouped = broadsheet_df.groupby('Student Name').agg({'Total Marks': 'mean'}).reset_index()

        # Classify students based on their yearly average
        for _, row in grouped.iterrows():
            student_info = {
                'Student Name': row['Student Name'],
                'Yearly Average': row['Total Marks'],
            }

            # Apply classification thresholds
            if row['Total Marks'] >= 70:
                student_info['Classification'] = 'First Class'
            elif row['Total Marks'] >= 60:
                student_info['Classification'] = 'Second Class Upper'
            elif row['Total Marks'] >= 50:
                student_info['Classification'] = 'Second Class Lower'
            elif row['Total Marks'] >= 40:
                student_info['Classification'] = 'Third Class'
            else:
                student_info['Classification'] = 'Fail'

            classification_data.append(student_info)

        # Convert classification data to DataFrame and return
        return pd.DataFrame(classification_data)

    except Exception as e:
        print(f"Failed to classify students: {e}")
        traceback.print_exc()  # Print detailed traceback of the error
        return None
