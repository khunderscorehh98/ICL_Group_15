import pandas as pd
from broadsheet_generator import generate_broadsheet
from classification import generate_classification

# Define input files
input_files = [
    'input_files/BSF S1_SF0111.xlsx',
    'input_files/BSF S1_SF0112.xlsx',
    'input_files/BSF S1_SF0113.xlsx',
    'input_files/BSF S3_SF1111.xlsx',
    'input_files/BSF S3_SF2222.xlsx',
    'input_files/BSF S3_SF3333.xlsx'
]

# Read each file and store the sheets in a dictionary
def read_grade_sheets():
    grade_sheets = {}
    for file in input_files:
        major_1 = pd.read_excel(file, sheet_name='M1')  # Major 1
        major_2 = pd.read_excel(file, sheet_name='M2')  # Major 2
        grade_sheets[file] = {'M1': major_1, 'M2': major_2}
    return grade_sheets
    
# Main function to coordinate the process
def main():
    grade_sheets = read_grade_sheets()
    # Generate broadsheets for Major 1, Year 1 from each input file
    for file, data in grade_sheets.items():
        generate_broadsheet(data['M1'], 'M1', 'Intake_01', 1)  # Adjust intake/year as needed
    # Example list of generated broadsheet files (you can dynamically collect this)
    broadsheet_files = [
        'output_files/Broadsheet_M1_Intake_01_Y1.xlsx'
    ]
    # Generate the classification file using the broadsheets
    generate_classification(broadsheet_files)

# Ensure the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
