import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Interface")

        self.user_type = tk.StringVar(value="Employee")

        tk.Label(root, text="Login as:").grid(row=0, column=0, padx=10, pady=10)
        tk.Radiobutton(root, text="Admin", variable=self.user_type, value="Admin").grid(row=0, column=1)
        tk.Radiobutton(root, text="Employee", variable=self.user_type, value="Employee").grid(row=0, column=2)

        tk.Label(root, text="Employee ID:").grid(row=1, column=0, padx=10, pady=10)
        self.employee_id_entry = tk.Entry(root)
        self.employee_id_entry.grid(row=1, column=1, columnspan=2)

        tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=2, column=1, columnspan=2)

        tk.Button(root, text="Login", command=self.login).grid(row=3, column=1, pady=10)

    def login(self):
        user_type = self.user_type.get()
        employee_id = self.employee_id_entry.get()
        password = self.password_entry.get()

        # Here you would add your authentication logic
        if user_type == "Admin" and employee_id == "admin" and password == "adminpass":
            messagebox.showinfo("Login Success", "Logged in as Admin")
        elif user_type == "Employee" and employee_id == "employee" and password == "employeepass":
            messagebox.showinfo("Login Success", "Logged in as Employee")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
