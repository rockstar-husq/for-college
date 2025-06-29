import tkinter as tk
from tkinter import ttk

# Root window
root = tk.Tk()
root.title("Sign Up")
root.configure(bg="#1e1e36")
root.geometry("500x660")

# Header (orange, left-aligned text)
header = tk.Frame(root, bg="orange", height=40)
header.pack(fill="x")
tk.Label(header, text="Sign Up", bg="orange", fg="white", font=("Arial", 14, "bold"), anchor="w").pack(side="left", padx=10, pady=5)

# Main form container
frame = tk.Frame(root, bg="#1e1e36", padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Label style
label_opts = {"bg": "#1e1e36", "fg": "yellow", "anchor": "w"}

# Input fields dictionary
entries = {}

def create_label_entry(row, label_text, entry_name, show=None):
    tk.Label(frame, text=label_text, **label_opts).grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(frame, show=show) if show else tk.Entry(frame)
    entry.grid(row=row, column=1, columnspan=2, sticky="ew", pady=5)
    entries[entry_name] = entry

# First Name
create_label_entry(0, "First Name", "first_name")
# Last Name
create_label_entry(1, "Last Name", "last_name")
# Screen Name
create_label_entry(2, "Screen Name", "screen_name")

# Date of Birth
tk.Label(frame, text="Date of Birth", **label_opts).grid(row=3, column=0, sticky="w", pady=5)

# Date of Birth container
dob_frame = tk.Frame(frame, bg="#1e1e36")
dob_frame.grid(row=3, column=1, columnspan=2, sticky="w", pady=5)

month_var = tk.StringVar(value="May")
day_var = tk.StringVar(value="5")
year_var = tk.StringVar(value="1985")

ttk.Combobox(dob_frame, textvariable=month_var, values=[
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
], width=10).pack(side="left", padx=2)

ttk.Combobox(dob_frame, textvariable=day_var, values=[str(i) for i in range(1, 32)], width=5).pack(side="left", padx=2)

ttk.Combobox(dob_frame, textvariable=year_var, values=[str(i) for i in range(1900, 2026)], width=7).pack(side="left", padx=2)

# Gender
tk.Label(frame, text="Gender", **label_opts).grid(row=4, column=0, sticky="w", pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="#1e1e36", fg="white").grid(row=4, column=1, sticky="w")
tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="#1e1e36", fg="white").grid(row=4, column=2, sticky="w")

# Country
tk.Label(frame, text="Country", **label_opts).grid(row=5, column=0, sticky="w", pady=5)
country_var = tk.StringVar(value="USA")
ttk.Combobox(frame, textvariable=country_var, values=["USA", "Canada", "UK", "Australia", "Other"]).grid(row=5, column=1, columnspan=2, sticky="ew")

# Email
create_label_entry(6, "E-mail", "email")
# Phone
create_label_entry(7, "Phone", "phone")
# Password
create_label_entry(8, "Password", "password", show="*")
# Confirm Password
create_label_entry(9, "Confirm Password", "confirm_password", show="*")

# Terms checkbox
terms_var = tk.IntVar()
tk.Checkbutton(frame, text="I agree to the Terms of Use", variable=terms_var, bg="#1e1e36", fg="yellow").grid(row=10, column=0, columnspan=3, pady=10)

# Footer (orange)
footer = tk.Frame(root, bg="orange", height=50)
footer.pack(fill="x")

# Button container aligned right
btn_frame = tk.Frame(footer, bg="orange")
btn_frame.pack(side="right", padx=10, pady=10)

submit_btn = tk.Button(btn_frame, text="submit", bg="green", fg="white", padx=20)
submit_btn.pack(side="left", padx=10)

cancel_btn = tk.Button(btn_frame, text="Cancel", bg="red", fg="white", padx=20)
cancel_btn.pack(side="left", padx=10)

root.mainloop()
