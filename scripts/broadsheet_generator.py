import pandas as pd
import os

# Function to generate broadsheets
def generate_broadsheet(broadsheets, intake, year):
    output_dir = "output_files/"
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for broadsheet in broadsheets:
        # Read the broadsheet file
        df = pd.read_excel(broadsheet)
        
        # Process the data as needed (modify this section based on your actual logic)
        # Here we'll assume that we just want to save the broadsheet with the intake and year information.
        # You can modify this to do any other processing as needed.
        
        output_file = f"{output_dir}/Broadsheet_{intake}_Year_{year}.xlsx"
        
        # Save the broadsheet to the output directory
        df.to_excel(output_file, index=False)
        print(f"Generated broadsheet for intake {intake}, year {year} from file: {broadsheet}")
    
    print("Broadsheet generation complete.")
