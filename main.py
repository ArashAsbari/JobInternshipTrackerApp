import tkinter as tk
from tkinter import ttk

class JobTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Job/Internship Tracker")
        self.geometry("800x500")
        self.configure(bg="#f2f2f2")

        self.jobs = []  # in-memory list to store jobs

        self.create_widgets()

    def create_widgets(self):
        # Create Notebook (Tabs)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Tabs
        self.add_tab = ttk.Frame(self.notebook)
        self.view_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.add_tab, text='Add Job')
        self.notebook.add(self.view_tab, text='View All')

        self.create_add_tab()
        self.create_view_tab()

    def create_add_tab(self):
        # Input Fields
        tk.Label(self.add_tab, text="Company:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.company_entry = tk.Entry(self.add_tab)
        self.company_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.add_tab, text="Role:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.role_entry = tk.Entry(self.add_tab)
        self.role_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.add_tab, text="Status:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.status_entry = tk.Entry(self.add_tab)
        self.status_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.add_tab, text="Add Job", command=self.add_job).grid(row=3, column=0, columnspan=2, pady=10)

    def create_view_tab(self):
        self.job_listbox = tk.Listbox(self.view_tab)
        self.job_listbox.pack(fill='both', expand=True, padx=10, pady=10)

    def add_job(self):
        job = {
            "company": self.company_entry.get(),
            "role": self.role_entry.get(),
            "status": self.status_entry.get()
        }
        self.jobs.append(job)
        self.update_job_list()

        # Clear fields
        self.company_entry.delete(0, tk.END)
        self.role_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)

    def update_job_list(self):
        self.job_listbox.delete(0, tk.END)
        for idx, job in enumerate(self.jobs, 1):
            entry = f"{idx}. {job['company']} - {job['role']} ({job['status']})"
            self.job_listbox.insert(tk.END, entry)

if __name__ == "__main__":
    app = JobTrackerApp()
    app.mainloop()
