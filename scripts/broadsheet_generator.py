import pandas as pd
import os

# Function to generate a consolidated broadsheet from multiple "BSF" files
def generate_broadsheet_from_multiple_files():
    input_dir = 'input/'  # Directory where BSF files are stored
    output_dir = 'output_files/'  # Directory where output will be saved
    broadsheets = [f for f in os.listdir(input_dir) if f.startswith("BSF") and f.endswith(".xlsx")]

    final_broadsheet = pd.DataFrame()  # Empty DataFrame to hold the final broadsheet data

    # Loop through each BSF file
    for broadsheet in broadsheets:
        input_file = os.path.join(input_dir, broadsheet)
        df = pd.read_excel(input_file)

        # Clean up column names (removes leading/trailing spaces)
        df.columns = df.columns.str.strip()

        # Check if necessary columns exist ('Student Name', 'Coursework', 'Exam')
        if 'Student Name' not in df.columns or 'Coursework' not in df.columns or 'Exam' not in df.columns:
            print(f"Error: Missing necessary columns in {broadsheet}")
            continue

        # Calculate total marks as an average of Coursework and Exam
        df['Total Marks'] = df[['Coursework', 'Exam']].mean(axis=1)

        # Append the current module data to the final broadsheet
        final_broadsheet = pd.concat([final_broadsheet, df], ignore_index=True)

    # Save the final consolidated broadsheet to the output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join(output_dir, "Consolidated_Broadsheet.xlsx")
    final_broadsheet.to_excel(output_file, index=False)
    print(f"Consolidated broadsheet saved to {output_file}")

    return final_broadsheet
