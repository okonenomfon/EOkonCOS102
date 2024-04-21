import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    location = entry_location.get().lower()
    weight = float(entry_weight.get())

    if location == "IbejuLekki":
        if weight >= 10:
            charge = 5000
        else:
            charge = 3500
    elif location == "Epe":
        if weight >= 10:
            charge = 10000
        else:
            charge = 5000
    else:
        messagebox.showerror("Error", "Invalid location entered.")
        return

    messagebox.showinfo("Charge", f"The delivery charge is ₦{charge}.")

root = tk.Tk()
root.title("Simi Services Delivery")

label_location = tk.Label(root, text="Enter Delivery Location:")
label_location.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

entry_location = tk.Entry(root)
entry_location.grid(row=0, column=1, padx=10, pady=5)

label_weight = tk.Label(root, text="Enter Package Weight (in kg):")
label_weight.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_charge)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
