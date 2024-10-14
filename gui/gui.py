import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

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
        generate_broadsheet_logic(sheets, major, intake, year)  # Replace with actual function
        messagebox.showinfo("Success", "Broadsheet generated successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate broadsheet: {str(e)}")

def classify_students():
    # Logic for student classification
    try:
        # Assume classify_students_logic is implemented
        classify_students_logic()  # Replace with actual function
        messagebox.showinfo("Success", "Classification done successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to classify students: {str(e)}")

def process_grades():
    file_path = file_label.cget("text")
    if not file_path:
        messagebox.showerror("Error", "No file selected")
        return

    try:
        process_grades_logic(file_path)  # Replace with actual function
        messagebox.showinfo("Success", "Grades processed successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process grades: {str(e)}")

root = ctk.CTk()
root.title("University X Grade Management System")
root.geometry("500x500")

file_label = ctk.CTkLabel(root, text="No file selected", width=50)
file_label.pack(pady=10)

select_button = ctk.CTkButton(root, text="Select Grade Sheet", command=select_file)
select_button.pack(pady=10)

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

classify_button = ctk.CTkButton(root, text="Classify Students", command=classify_students)
classify_button.pack(pady=10)

process_grades_button = ctk.CTkButton(root, text="Process Grades", command=process_grades)
process_grades_button.pack(pady=10)

root.mainloop()