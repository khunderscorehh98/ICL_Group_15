import pandas as pd

# Function to generate a broadsheet
def generate_broadsheet(major_data, major_name, intake, year):
    """
    Generates a broadsheet for a specific major and saves it as an Excel file.
    
    :param major_data: DataFrame of student data for a specific major
    :param major_name: Name of the major (e.g., 'Computer Science')
    :param intake: Year of intake (e.g., '2024')
    :param year: Academic year (e.g., '1', '2', '3')
    :return: None
    """
    # Define the broadsheet columns
    broadsheet_columns = ['Roll No', 'Student Name', 'IC No', 'Module Code', 'CV', 'CW%', 'UE%', 'Marks', 'Remarks']
    broadsheet = pd.DataFrame(columns=broadsheet_columns)

    # Populate the broadsheet with relevant data from the major sheet
    for index, row in major_data.iterrows():
        new_row = {
            'Roll No': row['Roll No'],
            'Student Name': row['Student Name'],
            'IC No': row['IC No'],
            'Module Code': row.get('Module Code', 'SF1111'),  # Default module code if missing
            'CV': row.get('CV', 4),  # Default CV value
            'CW%': row['Coursework'],
            'UE%': row['Examination'],
            'Marks': row['Final Mark'],
            'Remarks': 'Pass' if row['Final Mark'] >= 50 else 'Fail'
        }
        broadsheet = broadsheet.append(new_row, ignore_index=True)

    # Save the broadsheet as an Excel file based on the major, intake, and year
    output_file = f'output_files/Broadsheet_{major_name}_Intake_{intake}_Year_{year}.xlsx'
    broadsheet.to_excel(output_file, index=False)
    print(f'Broadsheet for {major_name} Year {year} saved to {output_file}')
