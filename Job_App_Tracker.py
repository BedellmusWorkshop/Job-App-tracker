import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('job_applications.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS applications
                      (id INTEGER PRIMARY KEY,
                       company TEXT,
                       title TEXT,
                       application_date TEXT,
                       status TEXT,
                       notes TEXT,
                       cover_letter_included INTEGER,
                       job_replied INTEGER)''')
    conn.commit()
    conn.close()
    print("Database initialized")


# Function to add an application
def add_application():
    company = entry_company.get()
    title = entry_title.get()
    application_date = entry_date.get()
    status = entry_status.get()
    notes = entry_notes.get("1.0", tk.END).strip()
    cover_letter_included = cover_letter_var.get()
    job_replied = job_replied_var.get()

    print("Captured Data: ", company, title, application_date, status, notes, cover_letter_included, job_replied)

    if company and title and application_date and status:
        try:
            conn = sqlite3.connect('job_applications.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO applications (company, title, application_date, status, notes, "
                "cover_letter_included, job_replied) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (company, title, application_date, status, notes, cover_letter_included, job_replied)
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Job application added successfully")
            clear_entries()
            print("Data inserted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            print(f"Error: {e}")
    else:
        messagebox.showwarning("Input Error", "Please fill in all required fields")


# Function to clear entry fields
def clear_entries():
    entry_company.delete(0, tk.END)
    entry_title.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_status.delete(0, tk.END)
    entry_notes.delete("1.0", tk.END)
    cover_letter_var.set(0)
    job_replied_var.set(0)


# Function to display the main entry form
def display_entry_form():
    clear_frame()

    tk.Label(root, text="Company Name", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    entry_company.grid(row=0, column=1, padx=20, pady=5, sticky='ew')

    tk.Label(root, text="Job Title", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    entry_title.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

    tk.Label(root, text="Application Date (YYYY-MM-DD)", font=label_font).grid(row=2, column=0, padx=10, pady=5,
                                                                               sticky='w')
    entry_date.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

    tk.Label(root, text="Application Posted Date (YYYY-MM)", font=label_font).grid(row=3, column=0, padx=10, pady=5,
                                                                                   sticky='w')
    entry_status.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

    tk.Label(root, text="Notes", font=label_font).grid(row=4, column=0, padx=10, pady=5, sticky='w')
    entry_notes.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

    cover_letter_check.grid(row=5, column=0, columnspan=2, sticky='w')
    job_replied_check.grid(row=6, column=0, columnspan=2, sticky='w')

    tk.Button(root, text="Add Application", command=add_application).grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Clear Fields", command=clear_entries).grid(row=8, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Back to Main Menu", command=display_main_menu).grid(row=9, column=0, columnspan=2, pady=10)

    root.grid_columnconfigure(1, weight=1)  # Allow the second column to expand


# Function to clear the current frame
def clear_frame():
    for widget in root.winfo_children():
        widget.grid_remove()


# Function to view the applications
def view_applications():
    clear_frame()

    tk.Label(root, text="Search:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
    search_entry = tk.Entry(root)
    search_entry.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
    search_button = tk.Button(root, text="Search", command=lambda: search_records(search_entry.get()))
    search_button.grid(row=0, column=2, padx=10, pady=5)

    # Set up the treeview
    columns = ("ID", "Company", "Job Title", "Date Applied", "Job Posted Date", "Notes", "Cover Letter", "Job Replied")
    tree = ttk.Treeview(root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='w')

    tree.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='nsew')

    scrollbar_y = tk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    scrollbar_y.grid(row=1, column=4, sticky='ns')
    tree.configure(yscrollcommand=scrollbar_y.set)

    # Edit fields and buttons
    tk.Label(root, text="Company Name").grid(row=2, column=0, padx=10, pady=5, sticky='w')
    edit_company = tk.Entry(root)
    edit_company.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

    tk.Label(root, text="Job Title").grid(row=3, column=0, padx=10, pady=5, sticky='w')
    edit_title = tk.Entry(root)
    edit_title.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

    tk.Label(root, text="Application Date (YYYY-MM-DD)").grid(row=4, column=0, padx=10, pady=5, sticky='w')
    edit_date = tk.Entry(root)
    edit_date.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

    tk.Label(root, text="Application Posted Date (YYYY-MM)").grid(row=5, column=0, padx=10, pady=5, sticky='w')
    edit_status = tk.Entry(root)
    edit_status.grid(row=5, column=1, padx=10, pady=5, sticky='ew')

    tk.Label(root, text="Notes").grid(row=6, column=0, padx=10, pady=5, sticky='w')
    edit_notes = tk.Text(root, height=5, width=55)
    edit_notes.grid(row=6, column=1, padx=10, pady=5, sticky='ew')

    edit_cover_letter_var = tk.IntVar()
    edit_cover_letter_check = tk.Checkbutton(root, text="Include Cover Letter", variable=edit_cover_letter_var)
    edit_cover_letter_check.grid(row=7, column=0, columnspan=2, sticky='w')

    edit_job_replied_var = tk.IntVar()
    edit_job_replied_check = tk.Checkbutton(root, text="Job Replied", variable=edit_job_replied_var)
    edit_job_replied_check.grid(row=8, column=0, columnspan=2, sticky='w')

    def select_record(event):
        selected_items = tree.selection()
        if not selected_items:
            return
        selected = selected_items[0]
        values = tree.item(selected, 'values')
        edit_company.delete(0, tk.END)
        edit_company.insert(0, values[1])
        edit_title.delete(0, tk.END)
        edit_title.insert(0, values[2])
        edit_date.delete(0, tk.END)
        edit_date.insert(0, values[3])
        edit_status.delete(0, tk.END)
        edit_status.insert(0, values[4])
        edit_notes.delete("1.0", tk.END)
        edit_notes.insert("1.0", values[5])
        edit_cover_letter_var.set(1 if values[6] == "Yes" else 0)
        edit_job_replied_var.set(1 if values[7] == "Yes" else 0)

    def update_record():
        try:
            selected = tree.selection()[0]
            values = tree.item(selected, 'values')
            record_id = values[0]
            company = edit_company.get()
            title = edit_title.get()
            application_date = edit_date.get()
            status = edit_status.get()
            notes = edit_notes.get("1.0", tk.END).strip()
            cover_letter_included = edit_cover_letter_var.get()
            job_replied = edit_job_replied_var.get()

            conn = sqlite3.connect('job_applications.db')
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE applications SET company=?, title=?, application_date=?, status=?, notes=?, "
                "cover_letter_included=?, job_replied=? WHERE id=?",
                (company, title, application_date, status, notes, cover_letter_included, job_replied, record_id)
            )
            conn.commit()
            conn.close()

            view_applications()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a record to update")

    def delete_record():
        try:
            selected = tree.selection()[0]
            values = tree.item(selected, 'values')
            record_id = values[0]
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?"):
                conn = sqlite3.connect('job_applications.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM applications WHERE id=?", (record_id,))
                conn.commit()
                conn.close()
                view_applications()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a record to delete")

    def search_records(query):
        for item in tree.get_children():
            tree.delete(item)
        conn = sqlite3.connect('job_applications.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, company, title, application_date, status, notes, cover_letter_included, job_replied "
            "FROM applications WHERE company LIKE ? OR title LIKE ?", ('%' + query + '%', '%' + query + '%')
        )
        records = cursor.fetchall()
        conn.close()
        for record in records:
            cover_letter_text = "Yes" if record[6] == 1 else "No"
            job_replied_text = "Yes" if record[7] == 1 else "No"
            tree.insert('', tk.END, values=(
                record[0], record[1], record[2], record[3], record[4], record[5], cover_letter_text, job_replied_text
            ))

    tk.Button(root, text="Update Record", command=update_record).grid(row=9, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Delete Record", command=delete_record).grid(row=10, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Back to Main Menu", command=display_main_menu).grid(row=11, column=0, columnspan=2, pady=10)

    conn = sqlite3.connect('job_applications.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, company, title, application_date, status, notes, cover_letter_included, job_replied FROM applications"
    )
    records = cursor.fetchall()
    conn.close()

    for record in records:
        cover_letter_text = "Yes" if record[6] == 1 else "No"
        job_replied_text = "Yes" if record[7] == 1 else "No"
        tree.insert('', tk.END, values=(
            record[0], record[1], record[2], record[3], record[4], record[5], cover_letter_text, job_replied_text
        ))

    tree.bind("<<TreeviewSelect>>", select_record)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)


# Function to display the main menu
def display_main_menu():
    clear_frame()

    tk.Button(root, text="Add Application", command=display_entry_form, width=20, height=2).grid(row=0, column=0,
                                                                                                 padx=20, pady=20)
    tk.Button(root, text="View Applications", command=view_applications, width=20, height=2).grid(row=1, column=0,
                                                                                                  padx=20, pady=20)


# Initialize the database
initialize_database()

# Set up the main window
root = tk.Tk()
root.title("Job Application Tracker")
root.state('zoomed')  # Maximize the window

# Font configuration
label_font = ("Helvetica", 12, "bold")

# Create entry widgets
entry_company = tk.Entry(root)
entry_title = tk.Entry(root)
entry_date = tk.Entry(root)
entry_status = tk.Entry(root)
entry_notes = tk.Text(root, height=10, width=55)

cover_letter_var = tk.IntVar()
cover_letter_check = tk.Checkbutton(root, text="Include Cover Letter", variable=cover_letter_var)
job_replied_var = tk.IntVar()
job_replied_check = tk.Checkbutton(root, text="Job Replied", variable=job_replied_var)

# Display the main menu initially
display_main_menu()

# Start the main event loop
root.mainloop()



