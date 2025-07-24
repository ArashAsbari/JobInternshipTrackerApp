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
        labels = ["Company", "Role", "Status", "Date Applied", "Location", "Notes"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self.add_tab, text=f"{label}:").grid(row=i, column=0, padx=10, pady=5, sticky='e')

            if label == "Notes":
                text = tk.Text(self.add_tab, height=4, width=40)
                text.grid(row=i, column=1, padx=10, pady=5)
                self.entries[label.lower()] = text
            else:
                entry = tk.Entry(self.add_tab, width=40)
                entry.grid(row=i, column=1, padx=10, pady=5)
                self.entries[label.lower()] = entry

        tk.Button(self.add_tab, text="Add Job", command=self.add_job).grid(row=len(labels), column=0, columnspan=2,
                                                                           pady=10)

    def create_view_tab(self):
        self.job_listbox = tk.Listbox(self.view_tab)
        self.job_listbox.pack(fill='both', expand=True, padx=10, pady=10)

    def add_job(self):
        job = {
            "company": self.entries["company"].get(),
            "role": self.entries["role"].get(),
            "status": self.entries["status"].get(),
            "date applied": self.entries["date applied"].get(),
            "location": self.entries["location"].get(),
            "notes": self.entries["notes"].get("1.0", tk.END).strip()
        }
        self.jobs.append(job)
        self.update_job_list()

        # Clear fields after adding
        for key, widget in self.entries.items():
            if key == "notes":
                widget.delete("1.0", tk.END)
            else:
                widget.delete(0, tk.END)

    def update_job_list(self):
        self.job_listbox.delete(0, tk.END)
        for idx, job in enumerate(self.jobs, 1):
            entry = f"{idx}. {job['company']} - {job['role']} ({job['status']})"
            self.job_listbox.insert(tk.END, entry)

if __name__ == "__main__":
    app = JobTrackerApp()
    app.mainloop()
