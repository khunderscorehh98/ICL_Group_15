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
