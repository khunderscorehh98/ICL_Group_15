import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
from scripts.broadsheet_generator import generate_broadsheet
from scripts.classification import classify_students_logic
from scripts.grade_processing import process_grades_logic

# Function to allow file selection for broadsheets
def select_input_files():
    files = filedialog.askopenfilenames(initialdir="input/", title="Select Broadsheets",
                                        filetypes=[("Excel Files", "*.xlsx")])
    return list(files)  # Returns a list of file paths selected

# Function to generate broadsheets
def generate_broadsheet_action():
    try:
        broadsheets = select_input_files()  # Select the input broadsheets
        intake = intake_entry.get()  # Get intake value from user input
        year = year_entry.get()  # Get year value from user input

        # Ensure that both intake and year are provided
        if not intake or not year:
            raise ValueError("Intake and year must be provided!")

        # Call generate_broadsheet with intake and year
        generate_broadsheet(broadsheets, intake, year)

        messagebox.showinfo("Success", "Broadsheets Generated Successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate broadsheets: {e}")

# Create a basic GUI for file input and actions
app = ctk.CTk()

# Set up the GUI window
app.geometry("400x300")
app.title("Broadsheet Generator")

# Intake entry
intake_label = ctk.CTkLabel(app, text="Enter Intake:")
intake_label.pack(pady=10)
intake_entry = ctk.CTkEntry(app)
intake_entry.pack(pady=10)

# Year entry
year_label = ctk.CTkLabel(app, text="Enter Year:")
year_label.pack(pady=10)
year_entry = ctk.CTkEntry(app)
year_entry.pack(pady=10)

# Button to trigger the broadsheet generation
generate_button = ctk.CTkButton(app, text="Generate Broadsheet", command=generate_broadsheet_action)
generate_button.pack(pady=20)

# Run the app
app.mainloop()
