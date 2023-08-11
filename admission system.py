import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog
from datetime import datetime

class Student:
    def __init__(self, student_id, name, date_of_birth, address, contact_info, previous_school, previous_grade):
        self.student_id = student_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.contact_info = contact_info
        self.previous_school = previous_school
        self.previous_grade = previous_grade

class SchoolAdmissionSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("School Admission System")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="School Admission System", font=("Arial", 16))
        self.label.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.label_id = tk.Label(self.frame, text="Student ID:")
        self.label_id.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = tk.Entry(self.frame)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        self.label_name = tk.Label(self.frame, text="Name:")
        self.label_name.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_dob = tk.Label(self.frame, text="Date of Birth:")
        self.label_dob.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_dob = tk.Entry(self.frame)
        self.entry_dob.grid(row=2, column=1, padx=5, pady=5)

        self.label_address = tk.Label(self.frame, text="Address:")
        self.label_address.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_address = tk.Entry(self.frame)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)

        self.label_contact = tk.Label(self.frame, text="Contact Info:")
        self.label_contact.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_contact = tk.Entry(self.frame)
        self.entry_contact.grid(row=4, column=1, padx=5, pady=5)

        self.label_previous = tk.Label(self.frame, text="Previous School:")
        self.label_previous.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_previous = tk.Entry(self.frame)
        self.entry_previous.grid(row=5, column=1, padx=5, pady=5)

        self.label_previous_grade = tk.Label(self.frame, text="Previous Grade:")
        self.label_previous_grade.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.entry_previous_grade = tk.Entry(self.frame)
        self.entry_previous_grade.grid(row=6, column=1, padx=5, pady=5)

        self.button_register = tk.Button(self.root, text="Register Student", command=self.register_student)
        self.button_register.pack(pady=10)

        self.button_admin = tk.Button(self.root, text="Admin Login", command=self.open_admin_window)
        self.button_admin.pack()

    def register_student(self):
        student_id = self.entry_id.get()
        name = self.entry_name.get()
        date_of_birth = self.entry_dob.get()
        address = self.entry_address.get()
        contact_info = self.entry_contact.get()
        previous_school = self.entry_previous.get()
        previous_grade = self.entry_previous_grade.get()

        student = Student(student_id, name, date_of_birth, address, contact_info, previous_school, previous_grade)
        self.save_student(student)
        self.update_index(student)

        messagebox.showinfo("Success", "Student registered successfully.")

        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_dob.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_contact.delete(0, tk.END)
        self.entry_previous.delete(0, tk.END)
        self.entry_previous_grade.delete(0, tk.END)

    def save_student(self, student):
        with open("students1.txt", "a") as file:
            file.write(
                f"{student.student_id},{student.name},{student.date_of_birth},{student.address},{student.contact_info},{student.previous_school},{student.previous_grade}\n"
            )

    def update_index(self, student):
        with open("index.txt", "r") as file:
            data = file.readlines()

        serial_number = len(data) + 1
        with open("index.txt", "a") as file:
            file.write(f"{serial_number},{student.student_id}\n")

    def open_admin_window(self):
        password = "admin123"  # Sample admin password

        admin_password = simpledialog.askstring("Admin Login", "Enter admin password:", show="*")

        if admin_password == password:
            self.save_admin_login(admin_password)
            self.save_admin_login_time()
            self.open_admin_panel()
        elif admin_password:
            messagebox.showerror("Error", "Invalid password.")

    def save_admin_login(self, password):
        with open("login.txt", "w") as file:
            file.write(password)

    def save_admin_login_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("login_times.txt", "a") as file:
            file.write(f"Login Time: {current_time}\n")

    def open_admin_panel(self):
        admin_panel = tk.Toplevel(self.root)
        admin_panel.title("Admin Panel")

        button_view_student = tk.Button(admin_panel, text="View Student Data", command=self.view_student_data)
        button_view_student.pack(pady=10)

        button_edit_student = tk.Button(admin_panel, text="Edit Student Data", command=self.edit_student_data)
        button_edit_student.pack(pady=10)

        button_delete_student = tk.Button(admin_panel, text="Delete Student Data", command=self.delete_student_data)
        button_delete_student.pack(pady=10)

        button_search_student = tk.Button(admin_panel, text="Search Student", command=self.search_student)
        button_search_student.pack(pady=10)

    def search_student(self):
        search_text = simpledialog.askstring("Search Student", "Enter Student ID or Name to search:")

        with open("students1.txt", "r") as file:
            data = file.readlines()

        found = False
        results = []
        for line in data:
            student_data = line.strip().split(",")
            student_id = student_data[0]
            student_name = student_data[1]

            if search_text.lower() in student_id.lower() or search_text.lower() in student_name.lower():
                results.append(line.strip())
                found = True

        if found:
            result_text = "\n".join(results)
            messagebox.showinfo("Search Results", result_text)
        else:
            messagebox.showinfo("Search Results", "No matching records found.")

    def view_student_data(self):
        student_data_window = tk.Toplevel(self.root)
        student_data_window.title("View Student Data")

        with open("students1.txt", "r") as file:
            data = file.readlines()

        text_data = tk.Text(student_data_window)
        for line in data:
            text_data.insert(tk.END, line)
        text_data.pack()

    def edit_student_data(self):
        student_id = simpledialog.askstring("Edit Student Data", "Enter Student ID:")

        with open("students1.txt", "r") as file:
            data = file.readlines()

        found = False
        for i, line in enumerate(data):
            if line.startswith(student_id):
                found = True
                break

        if found:
            student_data = data[i].strip().split(',')
            old_student = Student(*student_data)

            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Student Data")

            frame = tk.Frame(edit_window)
            frame.pack()

            label_id = tk.Label(frame, text="Student ID:")
            label_id.grid(row=0, column=0, padx=5, pady=5, sticky="e")
            entry_id = tk.Entry(frame)
            entry_id.grid(row=0, column=1, padx=5, pady=5)
            entry_id.insert(tk.END, old_student.student_id)

            label_name = tk.Label(frame, text="Name:")
            label_name.grid(row=1, column=0, padx=5, pady=5, sticky="e")
            entry_name = tk.Entry(frame)
            entry_name.grid(row=1, column=1, padx=5, pady=5)
            entry_name.insert(tk.END, old_student.name)

            label_dob = tk.Label(frame, text="Date of Birth:")
            label_dob.grid(row=2, column=0, padx=5, pady=5, sticky="e")
            entry_dob = tk.Entry(frame)
            entry_dob.grid(row=2, column=1, padx=5, pady=5)
            entry_dob.insert(tk.END, old_student.date_of_birth)

            label_address = tk.Label(frame, text="Address:")
            label_address.grid(row=3, column=0, padx=5, pady=5, sticky="e")
            entry_address = tk.Entry(frame)
            entry_address.grid(row=3, column=1, padx=5, pady=5)
            entry_address.insert(tk.END, old_student.address)

            label_contact = tk.Label(frame, text="Contact Info:")
            label_contact.grid(row=4, column=0, padx=5, pady=5, sticky="e")
            entry_contact = tk.Entry(frame)
            entry_contact.grid(row=4, column=1, padx=5, pady=5)
            entry_contact.insert(tk.END, old_student.contact_info)

            label_previous = tk.Label(frame, text="Previous School:")
            label_previous.grid(row=5, column=0, padx=5, pady=5, sticky="e")
            entry_previous = tk.Entry(frame)
            entry_previous.grid(row=5, column=1, padx=5, pady=5)
            entry_previous.insert(tk.END, old_student.previous_school)

            label_previous_grade = tk.Label(frame, text="Previous Grade:")
            label_previous_grade.grid(row=6, column=0, padx=5, pady=5, sticky="e")
            entry_previous_grade = tk.Entry(frame)
            entry_previous_grade.grid(row=6, column=1, padx=5, pady=5)
            entry_previous_grade.insert(tk.END, old_student.previous_grade)

            button_save = tk.Button(edit_window, text="Save Changes", command=lambda: self.save_edited_data(
                old_student, entry_id.get(), entry_name.get(), entry_dob.get(), entry_address.get(),
                entry_contact.get(), entry_previous.get(), entry_previous_grade.get(), student_id, edit_window))
            button_save.pack(pady=10)

        else:
            messagebox.showerror("Error", "Student ID not found.")

    def save_edited_data(self, old_student, new_id, new_name, new_dob, new_address, new_contact, new_previous, new_previous_grade, student_id, window):
        edited_fields = []
        if old_student.student_id != new_id:
            edited_fields.append(f"Student ID: {old_student.student_id} -> {new_id}")
        if old_student.name != new_name:
            edited_fields.append(f"Name: {old_student.name} -> {new_name}")
        if old_student.date_of_birth != new_dob:
            edited_fields.append(f"Date of Birth: {old_student.date_of_birth} -> {new_dob}")
        if old_student.address != new_address:
            edited_fields.append(f"Address: {old_student.address} -> {new_address}")
        if old_student.contact_info != new_contact:
            edited_fields.append(f"Contact Info: {old_student.contact_info} -> {new_contact}")
        if old_student.previous_school != new_previous:
            edited_fields.append(f"Previous School: {old_student.previous_school} -> {new_previous}")
        if old_student.previous_grade != new_previous_grade:
            edited_fields.append(f"Previous Grade: {old_student.previous_grade} -> {new_previous_grade}")

        if edited_fields:
            with open("students1.txt", "r") as file:
                data = file.readlines()

            with open("update.txt", "a") as file:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"Student ID: {student_id} | Edited Fields: {', '.join(edited_fields)} | Date/Time: {current_time}\n")

            for i, line in enumerate(data):
                if line.startswith(student_id):
                    data[i] = f"{new_id},{new_name},{new_dob},{new_address},{new_contact},{new_previous},{new_previous_grade}\n"
                    break

            with open("students1.txt", "w") as file:
                file.writelines(data)

            messagebox.showinfo("Success", "Student data updated successfully.")
            window.destroy()

        else:
            messagebox.showinfo("Information", "No changes made.")

    def delete_student_data(self):
        student_id = simpledialog.askstring("Delete Student Data", "Enter Student ID:")

        with open("students1.txt", "r") as file:
            data = file.readlines()

        found = False
        for i, line in enumerate(data):
            if line.startswith(student_id):
                found = True
                break

        if found:
            confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this student's data?")

            if confirm:
                with open("students1.txt", "w") as file:
                    for line in data:
                        if not line.startswith(student_id):
                            file.write(line)

                with open("index.txt", "r") as file:
                    index_data = file.readlines()

                with open("index.txt", "w") as file:
                    for line in index_data:
                        if not line.endswith(student_id):
                            file.write(line)

                with open("update.txt", "a") as file:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f"Student ID: {student_id} | Deleted | Date/Time: {current_time}\n")

                messagebox.showinfo("Success", "Student data deleted successfully.")
        else:
            messagebox.showerror("Error", "Student ID not found.")

root = tk.Tk()
app = SchoolAdmissionSystemGUI(root)
root.mainloop()
