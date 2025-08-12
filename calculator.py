import tkinter as tk
from tkinter import messagebox

# Calculator App









class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Modern Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="#2C3E50")
        self.root.resizable(False, False)

        # Expression storage
        self.expression = ""

        # Display
        self.display_var = tk.StringVar()
        self.create_display()

        # Buttons
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#2C3E50")
        display_frame.pack(pady=20)

        display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 24, "bold"),
            bg="#ECF0F1",
            fg="#2C3E50",
            bd=5,
            relief="flat",
            justify="right",
            width=15
        )
        display.pack()

    def add_to_expression(self, value):
        self.expression += str(value)
        self.display_var.set(self.expression)

    def clear_expression(self):
        self.expression = ""
        self.display_var.set("")

    def calculate(self):
        try:
            result = eval(self.expression)
            self.display_var.set(result)
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Division by zero is not allowed.")
            self.clear_expression()
        except Exception:
            messagebox.showerror("Error", "Invalid expression.")
            self.clear_expression()

    def create_buttons(self):
        btn_frame = tk.Frame(self.root, bg="#2C3E50")
        btn_frame.pack()

        # Button Layout








        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            [".", "0", "=", "+"],
        ]

        # Special styling







        btn_font = ("Arial", 16, "bold")

        # Create number and operator buttons






        for row_index, row in enumerate(buttons):
            row_frame = tk.Frame(btn_frame, bg="#2C3E50")
            row_frame.pack(pady=5)
            for btn_text in row:
                if btn_text == "=":
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=btn_font,
                        bg="#27AE60",
                        fg="white",
                        width=5,
                        height=2,
                        bd=0,
                        command=self.calculate
                    )
                elif btn_text in ["÷", "×", "-", "+"]:
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=btn_font,
                        bg="#E67E22",
                        fg="white",
                        width=5,
                        height=2,
                        bd=0,
                        command=lambda b=btn_text: self.add_to_expression(
                            b.replace("×", "*").replace("÷", "/")
                        )
                    )
                else:
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=btn_font,
                        bg="#34495E",
                        fg="white",
                        width=5,
                        height=2,
                        bd=0,
                        command=lambda b=btn_text: self.add_to_expression(b)
                    )
                btn.pack(side="left", padx=5)

        # Clear button





        clear_btn = tk.Button(
            self.root,
            text="C",
            font=btn_font,
            bg="#C0392B",
            fg="white",
            width=22,
            height=2,
            bd=0,
            command=self.clear_expression
        )
        clear_btn.pack(pady=10)




# Run calculator





if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
