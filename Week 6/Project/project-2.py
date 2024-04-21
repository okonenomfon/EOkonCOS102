import tkinter as tk

# Arrays to store admitted and not admitted candidates
admitted = []
not_admitted = []

def check_admission():
    # Getting input values from the GUI
    jamb_score = int(jamb_entry.get())
    sub = [math_var.get(), english_var.get(), physics_var.get(), chemistry_var.get(), cs_var.get()]
    sub2 = [govt_var.get(), english_var2.get(), lit_var.get(), crk_var.get(), hist_var.get()]
    interview_result = interview_var.get()

    # Checking admission criteria for Computer Science department
    if jamb_score >= 250 and jamb_score <= 400 and all(sub) and interview_result:
        admitted.append("Computer Science")
        result_label.config(text="Congratulations! You are admitted to Computer Science.")
    # Checking admission criteria for Mass Communication department
    elif jamb_score >= 230 and jamb_score <= 400 and all(sub2) and interview_result:
        admitted.append("Mass Communication")
        result_label.config(text="Congratulations! You are admitted to Mass Communication.")
    else:
        not_admitted.append("Candidate")
        result_label.config(text="Sorry, you do not meet the admission requirements.")

# Creating the GUI
root = tk.Tk()
root.title("Admission Status")

# JAMB score entry
jamb_label = tk.Label(root, text="JAMB Score:")
jamb_label.grid(row=0, column=0)
jamb_entry = tk.Entry(root)
jamb_entry.grid(row=0, column=1)

# Key subjects checkboxes for Computer Science
math_var = tk.IntVar()
math_check = tk.Checkbutton(root, text="Mathematics", variable=math_var)
math_check.grid(row=1, column=0, sticky="w")
english_var = tk.IntVar()
english_check = tk.Checkbutton(root, text="English", variable=english_var)
english_check.grid(row=2, column=0, sticky="w")
physics_var = tk.IntVar()
physics_check = tk.Checkbutton(root, text="Physics", variable=physics_var)
physics_check.grid(row=3, column=0, sticky="w")
chemistry_var = tk.IntVar()
chemistry_check = tk.Checkbutton(root, text="Chemistry", variable=chemistry_var)
chemistry_check.grid(row=4, column=0, sticky="w")
cs_var = tk.IntVar()
cs_check = tk.Checkbutton(root, text="Computer Science", variable=cs_var)
cs_check.grid(row=5, column=0, sticky="w")

# Key subjects checkboxes for Mass Communication
govt_var = tk.IntVar()
govt_check = tk.Checkbutton(root, text="Government", variable=govt_var)
govt_check.grid(row=1, column=1, sticky="w")
english_var2 = tk.IntVar()
english_check2 = tk.Checkbutton(root, text="English", variable=english_var2)
english_check2.grid(row=2, column=1, sticky="w")
lit_var = tk.IntVar()
lit_check = tk.Checkbutton(root, text="Literature", variable=lit_var)
lit_check.grid(row=3, column=1, sticky="w")
crk_var = tk.IntVar()
crk_check = tk.Checkbutton(root, text="CRK", variable=crk_var)
crk_check.grid(row=4, column=1, sticky="w")
hist_var = tk.IntVar()
hist_check = tk.Checkbutton(root, text="History", variable=hist_var)
hist_check.grid(row=5, column=1, sticky="w")

# Interview result entry
interview_label = tk.Label(root, text="Interview Result:")
interview_label.grid(row=6, column=0)
interview_var = tk.BooleanVar()
interview_check = tk.Checkbutton(root, text="Passed", variable=interview_var)
interview_check.grid(row=6, column=1)

# Button to check admission
check_button = tk.Button(root, text="Check Admission", command=check_admission)
check_button.grid(row=7, columnspan=2)

# Label to display admission result
result_label = tk.Label(root, text="")
result_label.grid(row=8, columnspan=2)

root.mainloop()
