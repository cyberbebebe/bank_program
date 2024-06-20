import tkinter as tk
from tkinter import font
from tkinter import messagebox, ttk
import json
import datetime

# Function to load client data from JSON file


def load_data():
    try:
        with open("clients.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"clients": []}


def save_data(data):
    with open("clients.json", "w") as file:
        json.dump(data, file, indent=4)


def create_client_info_form(parent):
    tk.Label(parent, text="Full name:", font=font_style).grid(row=0, column=0)
    name_entry = tk.Entry(parent, font=font_style)
    name_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="e")

    tk.Label(parent, text="Date of birth (D.M.Y):",
             font=font_style).grid(row=1, column=0)
    dob_entry = tk.Entry(parent, font=font_style)
    dob_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky="e")

    tk.Label(parent, text="Contact information:",
             font=font_style).grid(row=2, column=0)
    contact_entry = tk.Entry(parent, font=font_style)
    contact_entry.grid(row=2, column=1, padx=10,
                       pady=5, columnspan=2, sticky="e")

    tk.Label(parent, text="Residential address:",
             font=font_style).grid(row=3, column=0)
    address_entry = tk.Entry(parent, font=font_style)
    address_entry.grid(row=3, column=1, padx=10,
                       pady=5, columnspan=2, sticky="e")

    return name_entry, dob_entry, contact_entry, address_entry


def show_main_buttons():
    for widget in main_window.winfo_children():
        widget.destroy()
    button_frame = tk.Frame(main_window)
    button_frame.pack(expand=True)

    tk.Button(button_frame, text="Register Client", command=register_client,
              width=50, height=10, font=font_style).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Give Loan", command=give_loan,
              width=50, height=10, font=font_style).grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="Deposit/Withdraw Money", command=deposit_withdraw,
              width=50, height=10, font=font_style).grid(row=0, column=2, padx=10)


def register_client():
    for widget in main_window.winfo_children():
        widget.destroy()

    def submit_registration():
        client = {
            "Full name": name_entry.get(),
            "Date of birth": dob_entry.get(),
            "Contact information": contact_entry.get(),
            "Residential address": address_entry.get(),
            "score": 0,
            "balance": 0
        }

        if name_entry.get() == "" or dob_entry.get() == "" or contact_entry.get() == "" or address_entry.get() == "":
            messagebox.showerror("Error", "Some fields are missing!")

        else:
            data = load_data()

            existing_client = next((c for c in data["clients"] if c["Full name"] == client["Full name"] and c["Date of birth"] == client["Date of birth"] and
                                    c["Contact information"] == client["Contact information"] and
                                    c["Residential address"] == client["Residential address"]), None)

            if not existing_client:
                data["clients"].append(client)
                save_data(data)
                messagebox.showinfo(
                    "Success", "Client registered successfully!")
                show_main_buttons()
            else:
                messagebox.showerror("Error", "Client already registered!")

    registration_window = tk.Frame(main_window)
    registration_window.pack(expand=True)

    name_entry, dob_entry, contact_entry, address_entry = create_client_info_form(
        registration_window)

    tk.Button(registration_window, text="Submit", font=font_style,
              command=submit_registration).grid(row=4, column=0, padx=10, pady=5, columnspan=1, sticky="e")
    tk.Button(registration_window, text="Back", font=font_style, command=show_main_buttons).grid(
        row=4, column=1, padx=10, pady=5, columnspan=1, sticky="e")


def give_loan():
    for widget in main_window.winfo_children():
        widget.destroy()

    def submit_loan():
        full_name = name_entry.get()
        dob = dob_entry.get()
        contact_info = contact_entry.get()
        address = address_entry.get()

        data = load_data()
        client = next((c for c in data["clients"] if c["Full name"] == full_name and c["Date of birth"] ==
                      dob and c["Contact information"] == contact_info and c["Residential address"] == address), None)

        if not client:
            messagebox.showerror("Error", "Client not found!")
            return

        for widget in main_window.winfo_children():
            widget.destroy()

        loan_form_window = tk.Frame(main_window)
        loan_form_window.pack(expand=True)
        tk.Label(loan_form_window,
                 text=f"Loan details for {client}", font=font_style)
        tk.Label(loan_form_window, text="Income per year:", font=font_style).grid(
            row=0, column=0)
        income_entry = tk.Entry(loan_form_window, font=font_style)
        income_entry.grid(row=0, column=1, padx=10,
                          pady=5, columnspan=2, sticky="e")

        tk.Label(loan_form_window, text="Job title:",
                 font=font_style).grid(row=1, column=0)
        job_entry = tk.Entry(loan_form_window, font=font_style)
        job_entry.grid(row=1, column=1, padx=10,
                       pady=5, columnspan=2, sticky="e")

        tk.Label(loan_form_window, text="Years of employment:", font=font_style).grid(
            row=2, column=0)
        employment_length_entry = tk.Entry(loan_form_window, font=font_style)
        employment_length_entry.grid(
            row=2, column=1, padx=10, pady=5, columnspan=2, sticky="e")

        tk.Label(loan_form_window, text="Additional Income Source:", font=font_style).grid(
            row=3, column=0)
        additional_income_source_entry = tk.Entry(
            loan_form_window, font=font_style)
        additional_income_source_entry.grid(
            row=3, column=1, padx=10, pady=5, columnspan=2, sticky="e")

        tk.Label(loan_form_window,
                 text="Additional Income per year:", font=font_style).grid(row=4, column=0)
        additional_income_entry = tk.Entry(loan_form_window, font=font_style)
        additional_income_entry.grid(
            row=4, column=1, padx=10, pady=5, columnspan=2, sticky="e")

        tk.Label(loan_form_window,
                 text="Loan needed:", font=font_style).grid(row=5, column=0)
        loan_needed = tk.Entry(loan_form_window, font=font_style)
        loan_needed.grid(
            row=5, column=1, padx=10, pady=5, columnspan=2, sticky="e")

        tk.Label(loan_form_window,
                 text="Loan terms (years):", font=font_style).grid(row=6, column=0)
        loan_terms = tk.Entry(loan_form_window, font=font_style)
        loan_terms.grid(
            row=6, column=1, padx=10, pady=5, columnspan=2, sticky="e")

        def process_loan():
            client_income = income_entry.get()
            job = job_entry.get()
            work_years = employment_length_entry.get()
            additional_income_source = additional_income_source_entry.get()
            additional_income = additional_income_entry.get()
            loan = loan_needed.get()
            terms = loan_terms.get()

            current_year = datetime.datetime.now().year
            client_birth_year = int(client["Date of birth"].split(".")[2])
            client_age = current_year - client_birth_year

            if client.get("Job title"):
                score += 2

            client_score = score
            client_workability = int(client["Date of birth"])
            maximum_loan = 0.25*client_income*client_score
            if loan < maximum_loan:
                messagebox.showerror("Error", "Loan declined!")

            else:
                messagebox.showinfo("Success", "Loan approved!")

            show_main_buttons()

        tk.Button(loan_form_window, text="Submit", font=font_style, command=process_loan).grid(
            row=7, column=0, padx=10, pady=5, columnspan=1)
        tk.Button(loan_form_window, text="Back", font=font_style, command=show_main_buttons).grid(
            row=7, column=1, padx=10, pady=5, columnspan=1)

    loan_window = tk.Frame(main_window)
    loan_window.pack(expand=True)

    name_entry, dob_entry, contact_entry, address_entry = create_client_info_form(
        loan_window)

    tk.Button(loan_window, text="Submit", font=font_style, command=submit_loan).grid(
        row=5, column=0, padx=10, pady=5, columnspan=1, sticky="e")
    tk.Button(loan_window, text="Back", font=font_style, command=show_main_buttons).grid(
        row=5, column=1, padx=10, pady=5, columnspan=1, sticky="e")


def deposit_withdraw():
    for widget in main_window.winfo_children():
        widget.destroy()

    def submit_action():
        full_name = name_entry.get()
        dob = dob_entry.get()
        contact_info = contact_entry.get()
        address = address_entry.get()

        data = load_data()

        client = next((c for c in data["clients"] if c["Full name"] == full_name and c["Date of birth"] ==
                      dob and c["Contact information"] == contact_info and c["Residential address"] == address), None)

        if not client:
            messagebox.showerror("Error", "Client not found!")
            return

        for widget in main_window.winfo_children():
            widget.destroy()

        action_window = tk.Frame(main_window)
        action_window.pack(expand=True)

        action_var = tk.StringVar(None)
        tk.Label(action_window, text=f"Money operation for {full_name}", font=font_style).grid(
            row=0, column=1, padx=10, pady=5)

        tk.Label(action_window, text="Action:", font=font_style).grid(
            row=2, column=0, padx=10, pady=5)
        tk.Radiobutton(action_window, text="Deposit", font=font_style,
                       variable=action_var, value="Deposit").grid(row=2, column=1, padx=10, pady=5)
        tk.Radiobutton(action_window, text="Withdraw", font=font_style,
                       variable=action_var, value="Withdraw").grid(row=2, column=2, padx=10, pady=5)

        tk.Label(action_window, text="Amount:", font=font_style).grid(
            row=3, column=0, padx=10, pady=5)
        amount_entry = tk.Entry(action_window, font=font_style)
        amount_entry.grid(row=3, column=1, padx=10,
                          pady=5, columnspan=2, sticky="w")

        def process_action():
            amount = float(amount_entry.get())
            if action_var.get() == "Deposit":
                client["balance"] += amount
                client["score"] += amount/1000

            elif action_var.get() == "Withdraw":
                if client["balance"] >= amount:
                    client["balance"] -= amount
                    client["score"] += amount/1000
                else:
                    messagebox.showerror("Error", "Insufficient funds!")
                    return

            save_data(data)
            messagebox.showinfo("Success", "Transaction completed!")
            show_main_buttons()

        tk.Button(action_window, text="Submit", font=font_style,
                  command=process_action).grid(row=4, column=1, pady=10)
        tk.Button(action_window, text="Back", font=font_style,
                  command=show_main_buttons).grid(row=4, column=2, pady=10)

    withdraw_window = tk.Frame(main_window)
    withdraw_window.pack(expand=True)

    name_entry, dob_entry, contact_entry, address_entry = create_client_info_form(
        withdraw_window)

    tk.Button(withdraw_window, text="Submit", font=font_style,
              command=submit_action).grid(row=4, column=1, padx=10, pady=5, columnspan=1, sticky="e")
    tk.Button(withdraw_window, text="Back", font=font_style,
              command=show_main_buttons).grid(row=4, column=2, padx=10, pady=5, columnspan=1, sticky="e")


font_style = ("Helvetica", 16)


main_window = tk.Tk()
main_window.state("zoomed")
main_window.title("SimpleBank")
show_main_buttons()

main_window.mainloop()
