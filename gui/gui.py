import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
from scripts.broadsheet_generator import generate_broadsheet_logic
from scripts.classification import classify_students_logic
from scripts.grade_processing import process_grades_logic

# Example helper function for extracting year from filename
def extract_year_from_filename(filename):
    # Example: Broadsheet_M1_2024_1.xlsx
    parts = filename.split('_')
    return parts[2]  # Extracting the year

# GUI Functions
def select_file():
    file_path = filedialog.askopenfilename(title="Select Grade Sheet", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        file_label.configure(text=file_path)

def generate_broadsheet():
    file_path = file_label.cget("text")
    if not file_path:
        messagebox.showerror("Error", "No file selected")
        return
    
    try:
        major = major_entry.get()
        intake = intake_entry.get()
        year = int(year_entry.get())
        sheets = pd.read_excel(file_path, sheet_name=None)
        generate_broadsheet_logic(sheets, major, intake, year)  # Call from broadsheet_generator.py
        messagebox.showinfo("Success", "Broadsheet generated successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate broadsheet: {str(e)}")

def classify_students():
    try:
        broadsheets = ['Broadsheet_M1_2024_1.xlsx', 'Broadsheet_M1_2024_2.xlsx']  # Update with actual files
        intake = '2024'

        classification_data = calculate_yearly_average(broadsheets)
        classified_students = classify_students_logic(classification_data)  # Call from classification.py
        save_classification(classified_students, intake)  # Save the classification data
        messagebox.showinfo("Success", "Classification done successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to classify students: {str(e)}")

def process_grades():
    file_path = file_label.cget("text")
    if not file_path:
        messagebox.showerror("Error", "No file selected")
        return

    try:
        process_grades_logic(file_path)  # Call from grade_processing.py
        messagebox.showinfo("Success", "Grades processed successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process grades: {str(e)}")

# GUI Layout using CustomTkinter
root = ctk.CTk()
root.title("University X Grade Management System")
root.geometry("500x500")

# File selection
file_label = ctk.CTkLabel(root, text="No file selected", width=50)
file_label.pack(pady=10)

select_button = ctk.CTkButton(root, text="Select Grade Sheet", command=select_file)
select_button.pack(pady=10)

# Broadsheet generation section
major_label = ctk.CTkLabel(root, text="Enter Major (e.g., M1, M2):")
major_label.pack()

major_entry = ctk.CTkEntry(root)
major_entry.pack()

intake_label = ctk.CTkLabel(root, text="Enter Intake Year (e.g., 2024):")
intake_label.pack()

intake_entry = ctk.CTkEntry(root)
intake_entry.pack()

year_label = ctk.CTkLabel(root, text="Enter Year (e.g., 1, 2, 3):")
year_label.pack()

year_entry = ctk.CTkEntry(root)
year_entry.pack()

generate_broadsheet_button = ctk.CTkButton(root, text="Generate Broadsheet", command=generate_broadsheet)
generate_broadsheet_button.pack(pady=20)

# Classification section
classify_button = ctk.CTkButton(root, text="Classify Students", command=classify_students)
classify_button.pack(pady=10)

# Grade processing section
process_grades_button = ctk.CTkButton(root, text="Process Grades", command=process_grades)
process_grades_button.pack(pady=10)

# Run the application
root.mainloop()