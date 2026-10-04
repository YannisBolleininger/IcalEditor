import os
import ical_editor as ie
import customtkinter as tk

std_l_content = "Load file to show content"

class CheckboxFrame(tk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            cb = tk.CTkCheckBox(self, text=value)
            cb.grid(row=i, column=0, padx=10, pady=(10,0), sticky="w")
            self.checkboxes.append(cb)

    def get(self):
        checked_checkboxes = []
        for c in self.checkboxes:
            if c.get() == 1:
                checked_checkboxes.append(c.cget("text"))
        return checked_checkboxes

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ical Editor")
        self.geometry("400x150")

        self.b_load_file= tk.CTkButton(self, text="Open file", command=self.load_file)
        self.b_load_file.grid(row=0, column=0, padx=20, pady=20)

        self.b_unload_file= tk.CTkButton(self, text="X", command=self.unload_file)
        self.b_unload_file.grid(row=0, column=1, padx=0, pady=0)

        self.b_export_edited = tk.CTkButton(self, text="Export", command=self.export_edited)
        self.b_export_edited.grid(row=0, column=3, padx=0, pady=0)

        self.l_content = tk.CTkLabel(self, text=std_l_content, font=("Arial", 10))
        self.l_content.grid(row=1, column=0, padx=0, pady=0)

        tk.set_default_color_theme("dark-blue")

    def load_file(self):
        path = "/home/YBolleininger/Documents/Coding/IcalEditor/example.ics"
        if os.path.isfile(path):
            self.b_load_file.configure(fg_color="green")
            self.l_content.configure(text="File content")

        self.cal = ie.open_cal(path)

        distinct_content = []
        self.l_content.configure(text="Loading file content")
        for c in self.cal.walk():
            if c.name == "VEVENT":
                if c.get("summary") not in distinct_content:
                    distinct_content.append(c.get("summary"))

        self.checkbox_frame = CheckboxFrame(self, title="Entries", values=distinct_content)
        self.checkbox_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.l_content.configure(text="Select entries to keep")

    def unload_file(self):
        cal = None
        self.b_load_file.configure(fg_color="blue")
        self.l_content.configure(text=std_l_content)
        self.checkbox_frame.destroy()

    def export_edited(self):
        if not self.checkbox_frame:
            self.l_content.configure(text="Select a file first")

        for c in self.checkbox_frame.get():
            print(c)

app = App()
app.mainloop()
