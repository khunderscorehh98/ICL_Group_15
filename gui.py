import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
from scripts.broadsheet_generator import generate_broadsheet
from scripts.classification import classify_students_logic
from scripts.grade_processing import process_grades_logic


# Function to allow file selection for broadsheets
def select_input_files():
    files = filedialog.askopenfilenames(initialdir="input_files/", title="Select Broadsheets",
                                        filetypes=[("Excel Files", "*.xlsx")])
    return list(files)  # Returns a list of file paths selected


# Function to generate broadsheets
def generate_broadsheet_action():
    try:
        broadsheets = select_input_files()
        intake = intake_entry.get()
        year = year_entry.get()

        for broadsheet in broadsheets:
            major_name = extract_major_from_filename(broadsheet)  # Define this function based on your file naming convention
            major_data = pd.read_excel(broadsheet)
            generate_broadsheet(major_data, major_name, intake, year)

        messagebox.showinfo('Success', "Broadsheets generated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate broadsheets: {str(e)}")


# Function to classify students
def classify_students_action():
    try:
        broadsheets = select_input_files()  # Allow user to select broadsheets
        intake = intake_entry.get()

        classification_data = calculate_yearly_average(broadsheets)
        classified_students = classify_students_logic(classification_data)
        save_classification(classified_students, intake)

        messagebox.showinfo('Success', "Classification done successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to classify students: {str(e)}")


# Create the main GUI window
app = ctk.CTk()
app.geometry("600x400")
app.title("Student Broadsheet and Classification Generator")

# Labels and inputs for intake and year
intake_label = ctk.CTkLabel(app, text="Enter Intake Year:")
intake_label.pack(pady=10)

intake_entry = ctk.CTkEntry(app)
intake_entry.pack(pady=10)

year_label = ctk.CTkLabel(app, text="Enter Academic Year:")
year_label.pack(pady=10)

year_entry = ctk.CTkEntry(app)
year_entry.pack(pady=10)

# Buttons for generating broadsheets and classifying students
generate_button = ctk.CTkButton(app, text="Generate Broadsheet", command=generate_broadsheet_action)
generate_button.pack(pady=20)

classify_button = ctk.CTkButton(app, text="Classify Students", command=classify_students_action)
classify_button.pack(pady=20)

# Run the app
app.mainloop()