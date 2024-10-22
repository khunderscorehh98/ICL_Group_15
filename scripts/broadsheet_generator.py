import pandas as pd
import os
import traceback

# Function to classify students from the cleaned broadsheet
def classify_students(broadsheet_df):
    if broadsheet_df is not None:
        try:
            expected_column = 'SF1111_CW'
            if expected_column not in broadsheet_df.columns:
                print(f"Error: '{expected_column}' column not found in the broadsheet. Available columns: {broadsheet_df.columns}")
                return
            
            broadsheet_df[expected_column] = pd.to_numeric(broadsheet_df[expected_column], errors='coerce')
            grouped = broadsheet_df.groupby('Student Name').agg({expected_column: 'mean'}).reset_index()

            print("Classifying students...")
            print(grouped)
        except Exception as e:
            print(f"Failed to classify students: {e}")
            traceback.print_exc()
    else:
        print("Invalid broadsheet data; skipping classification.")

# Helper function to process broadsheet for a specific intake
def process_broadsheet(file_path, output_dir, intake):
    try:
        df = pd.read_excel(file_path, skiprows=12)

        print("Initial DataFrame:")
        print(df.head(10))

        df = clean_broadsheet_data(df)

        if df is not None and not df.empty:
            output_file = os.path.join(output_dir, f"Broadsheet_{intake}.xlsx")
            df.to_excel(output_file, index=False)
            print(f"Broadsheet for {intake} saved to {output_file}")
            return df
        else:
            print(f"No valid data to save for {intake} broadsheet.")
            return None
    except Exception as e:
        print(f"Failed to process {intake} broadsheet: {e}")
        traceback.print_exc()
        return None

# Function to clean broadsheet data
def clean_broadsheet_data(df):
    try:
        print(f"Actual number of columns before cleaning: {len(df.columns)}")
        print(f"Actual columns before cleaning: {df.columns}")

        df.columns = df.columns.map(str)
        df = df.dropna(axis=1, how='all')
        df = df.dropna(axis=0, how='all')

        valid_columns = [col for col in df.columns if df[col].notna().any()]
        df = df[valid_columns]

        print(f"Columns after cleaning: {df.columns}")
        num_columns = len(df.columns)

        print("DataFrame after cleaning:")
        print(df.head(10))

        if num_columns >= 6:
            df.columns = ['Roll No', 'Student Name', 'I.C. No', 'SF1111_CW', 'SF1111_UE', 'SF1111_GRADE']
        elif num_columns >= 12:
            df.columns = ['Roll No', 'Student Name', 'I.C. No', 'SF1111_CW', 'SF1111_UE', 'SF1111_GRADE',
                          'SF2222_CW', 'SF2222_UE', 'SF2222_GRADE', 'SF3333_CW', 'SF3333_UE', 'SF3333_GRADE']
        else:
            print(f"Warning: Unexpected number of columns: {num_columns}")
            df.columns = [f'Column_{i}' for i in range(num_columns)]
            print(f"Assigned generic column names: {df.columns}")

        if df.empty:
            print(f"Error: DataFrame is empty after cleaning.")
            return None

        return df

    except Exception as e:
        print(f"Error during broadsheet cleaning: {e}")
        traceback.print_exc()
        return None

# New function to generate broadsheets for each intake
def generate_broadsheet_for_each_intake():
    input_dir = 'input/'  # Directory where input files are stored
    output_dir = 'output_files/'  # Directory to save the broadsheets
    
    # Files representing M1 and M2 intakes
    m1_file = os.path.join(input_dir, 'Broadsheet M1_02_Y2.xlsx')
    m2_file = os.path.join(input_dir, 'Broadsheet_M2.xlsx')

    # Initialize an empty DataFrame to consolidate the data
    consolidated_df = pd.DataFrame()

    # Process the M1 broadsheet
    if os.path.exists(m1_file):
        m1_df = process_broadsheet(m1_file, output_dir, intake="M1")
        if m1_df is not None:
            consolidated_df = pd.concat([consolidated_df, m1_df], ignore_index=True)
    else:
        print(f"File {m1_file} not found, skipping M1 intake.")

    # Process the M2 broadsheet, but only if it exists
    if os.path.exists(m2_file):
        m2_df = process_broadsheet(m2_file, output_dir, intake="M2")
        if m2_df is not None:
            consolidated_df = pd.concat([consolidated_df, m2_df], ignore_index=True)
    else:
        print(f"File {m2_file} not found, skipping M2 intake.")

    # Return the consolidated broadsheet DataFrame
    return consolidated_df if not consolidated_df.empty else None

def clean_broadsheet_data(df):
    try:
        # Print actual column names and their count for debugging purposes
        print(f"Actual number of columns before cleaning: {len(df.columns)}")
        print(f"Actual columns before cleaning: {df.columns}")

        # Ensure all column headers are converted to string type
        df.columns = df.columns.map(str)

        # Drop columns that are completely empty (NaN)
        df = df.dropna(axis=1, how='all')

        # Drop rows that are completely empty (NaN)
        df = df.dropna(axis=0, how='all')

        # Select columns that have valid data (not all NaN)
        valid_columns = [col for col in df.columns if df[col].notna().any()]

        # Keep only the valid columns
        df = df[valid_columns]

        # Reprint the columns after cleaning for further verification
        print(f"Columns after cleaning: {df.columns}")

        # Ensure there are enough columns for meaningful data
        num_columns = len(df.columns)

        # Handle renaming dynamically based on the number of valid columns
        if num_columns == 6:
            df.columns = ['Roll No', 'Student Name', 'I.C. No', 'SF1111_CW', 'SF1111_UE', 'SF1111_GRADE']
        elif num_columns == 12:
            df.columns = ['Roll No', 'Student Name', 'I.C. No', 'SF1111_CW', 'SF1111_UE', 'SF1111_GRADE',
                          'SF2222_CW', 'SF2222_UE', 'SF2222_GRADE', 'SF3333_CW', 'SF3333_UE', 'SF3333_GRADE']
        else:
            print(f"Warning: Unexpected number of columns: {num_columns}")
            # Adjust to rename the first N columns dynamically and use generic names for the rest
            df.columns = [f'Column_{i}' for i in range(num_columns)]
            print(f"Assigned generic column names: {df.columns}")

        # If the DataFrame is empty, return None
        if df.empty:
            print(f"Error: DataFrame is empty after cleaning.")
            return None

        return df

    except Exception as e:
        print(f"Error during broadsheet cleaning: {e}")
        traceback.print_exc()  # Print detailed traceback of the error
        return None