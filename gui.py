import customtkinter as ctk
from tkinter import messagebox
from scripts.broadsheet_generator import generate_broadsheet_for_each_intake
from scripts.grade_processing import classify_students_from_broadsheet

# Function to generate broadsheet and classify students from multiple "BSF" files
def generate_broadsheet_and_classify_action():
    try:
        # Step 1: Generate the broadsheet from multiple "BSF" files
        broadsheet_df = generate_broadsheet_for_each_intake()

        # Step 2: Classify students based on the consolidated broadsheet
        if broadsheet_df is not None:
            classify_students_from_broadsheet(broadsheet_df)
            messagebox.showinfo("Success", "Broadsheet and Classification Generated Successfully!")
        else:
            messagebox.showerror("Error", "Broadsheet generation failed; no data to classify.")

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
