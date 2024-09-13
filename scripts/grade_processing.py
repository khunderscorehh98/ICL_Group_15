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