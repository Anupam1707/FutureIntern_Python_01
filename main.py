import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.minsize(300, 400)

        self.entry_font = ("Helvetica", 16)
        self.button_font = ("Helvetica", 14)
        self.result_font = ("Helvetica", 14, "italic")

        self.num1_entry = tk.Entry(root, font=self.entry_font, width=10)
        self.num1_entry.grid(row=0, column=0, padx=10, pady=10)

        self.num2_entry = tk.Entry(root, font=self.entry_font, width=10)
        self.num2_entry.grid(row=0, column=2, padx=10, pady=10)

        self.add_button = tk.Button(root, text="+", font=self.button_font, command=lambda: self.calculate('+'))
        self.add_button.grid(row=1, column=0, padx=10, pady=5)

        self.sub_button = tk.Button(root, text="-", font=self.button_font, command=lambda: self.calculate('-'))
        self.sub_button.grid(row=1, column=1, padx=10, pady=5)

        self.mul_button = tk.Button(root, text="*", font=self.button_font, command=lambda: self.calculate('*'))
        self.mul_button.grid(row=1, column=2, padx=10, pady=5)

        self.div_button = tk.Button(root, text="/", font=self.button_font, command=lambda: self.calculate('/'))
        self.div_button.grid(row=1, column=3, padx=10, pady=5)

        self.result_label = tk.Label(root, text="Result: ", font=self.result_font, fg="blue")
        self.result_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    def calculate(self, operator):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    raise ValueError("Cannot divide by zero")
            self.result_label.config(text=f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

root = tk.Tk()
app = CalculatorApp(root)

root.mainloop()
