import customtkinter as ctk
from tkinter import messagebox
from scripts.broadsheet_generator import generate_broadsheet_from_multiple_files
from scripts.grade_processing import classify_students_from_broadsheet

# Function to generate broadsheet and classify students from multiple "BSF" files
def generate_broadsheet_and_classify_action():
    try:
        # Step 1: Generate the broadsheet from multiple "BSF" files
        broadsheet_df = generate_broadsheet_from_multiple_files()

        # Step 2: Classify students based on the consolidated broadsheet
        classify_students_from_broadsheet(broadsheet_df, "2024")

        messagebox.showinfo("Success", "Broadsheet and Classification Generated Successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate broadsheet and classification: {e}")

# Create the GUI
app = ctk.CTk()
app.geometry("400x300")
app.title("Broadsheet and Classification Generator")

# Button to trigger the broadsheet generation and classification
generate_button = ctk.CTkButton(app, text="Generate from BSF Files", command=generate_broadsheet_and_classify_action)
generate_button.pack(pady=20)

# Run the app
app.mainloop()
