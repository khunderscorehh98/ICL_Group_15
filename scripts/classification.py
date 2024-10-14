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