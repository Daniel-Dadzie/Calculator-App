import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E2E2E")
        
        # Custom font
        self.custom_font = font.Font(family="Helvetica", size=16)
        self.display_font = font.Font(family="Helvetica", size=24)
        
        # Initialize variables
        self.current_input = ""
        self.total_expression = ""
        self.operation = None
        self.overwrite = False
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
        # Configure grid
        self.configure_grid()
    
    def create_display(self):
        # Frame for display
        self.display_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.display_frame.pack(expand=True, fill="both", padx=10, pady=(20, 10))
        
        # Total label (smaller, top-aligned)
        self.total_label = tk.Label(
            self.display_frame,
            text=self.total_expression,
            font=self.custom_font,
            bg="#2E2E2E",
            fg="#AAAAAA",
            anchor="e",
            padx=10
        )
        self.total_label.pack(expand=True, fill="both")
        
        # Current input label (larger, bottom-aligned)
        self.current_label = tk.Label(
            self.display_frame,
            text=self.current_input,
            font=self.display_font,
            bg="#2E2E2E",
            fg="white",
            anchor="e",
            padx=10
        )
        self.current_label.pack(expand=True, fill="both")
    
    def create_buttons(self):
        # Button frame
        self.buttons_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Button layout
        button_layout = [
            ("C", "⌫", "²", "÷"),
            ("7", "8", "9", "×"),
            ("4", "5", "6", "-"),
            ("1", "2", "3", "+"),
            ("±", "0", ".", "=")
        ]
        
        # Create buttons
        self.buttons = {}
        for i, row in enumerate(button_layout):
            self.buttons_frame.rowconfigure(i, weight=1)
            for j, btn_text in enumerate(row):
                self.buttons_frame.columnconfigure(j, weight=1)
                
                # Determine button color
                if btn_text in {"C", "⌫", "±", "²"}:
                    bg_color = "#3B3B3B"
                elif btn_text in {"÷", "×", "-", "+", "="}:
                    bg_color = "#FF9500"
                else:
                    bg_color = "#505050"
                
                btn = tk.Button(
                    self.buttons_frame,
                    text=btn_text,
                    font=self.custom_font,
                    bg=bg_color,
                    fg="white",
                    activebackground="#AAAAAA",
                    activeforeground="white",
                    borderwidth=0,
                    relief="flat",
                    command=lambda x=btn_text: self.on_button_click(x)
                )
                btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                self.buttons[btn_text] = btn
    
    def configure_grid(self):
        # Configure grid weights
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)
    
    def on_button_click(self, btn_text):
        if btn_text.isdigit() or btn_text == ".":
            self.add_to_input(btn_text)
        elif btn_text in {"+", "-", "×", "÷"}:
            self.set_operation(btn_text)
        elif btn_text == "=":
            self.calculate()
        elif btn_text == "C":
            self.clear()
        elif btn_text == "⌫":
            self.backspace()
        elif btn_text == "±":
            self.toggle_sign()
        elif btn_text == "²":
            self.square()
    
    def add_to_input(self, value):
        if self.overwrite:
            self.current_input = ""
            self.overwrite = False
        
        if value == "." and "." in self.current_input:
            return
        
        self.current_input += value
        self.update_current_label()
    
    def set_operation(self, op):
        if not self.current_input:
            return
        
        if self.total_expression and not self.overwrite:
            self.calculate()
        
        self.operation = op
        self.total_expression = f"{self.current_input} {self.operation}"
        self.current_input = ""
        self.update_total_label()
        self.update_current_label()
    
    def calculate(self):
        if not self.current_input or not self.operation:
            return
        
        try:
            num1 = float(self.total_expression.split()[0])
            num2 = float(self.current_input)
            
            if self.operation == "+":
                result = num1 + num2
            elif self.operation == "-":
                result = num1 - num2
            elif self.operation == "×":
                result = num1 * num2
            elif self.operation == "÷":
                if num2 == 0:
                    self.current_input = "Error"
                    self.update_current_label()
                    return
                result = num1 / num2
            
            self.current_input = str(result)
            self.total_expression = ""
            self.operation = None
            self.overwrite = True
            self.update_total_label()
            self.update_current_label()
        except:
            self.current_input = "Error"
            self.update_current_label()
    
    def clear(self):
        self.current_input = ""
        self.total_expression = ""
        self.operation = None
        self.update_current_label()
        self.update_total_label()
    
    def backspace(self):
        if self.overwrite:
            return
        
        self.current_input = self.current_input[:-1]
        self.update_current_label()
    
    def toggle_sign(self):
        if not self.current_input:
            return
        
        if self.current_input[0] == "-":
            self.current_input = self.current_input[1:]
        else:
            self.current_input = f"-{self.current_input}"
        self.update_current_label()
    
    def square(self):
        if not self.current_input:
            return
        
        try:
            num = float(self.current_input)
            self.current_input = str(num ** 2)
            self.update_current_label()
        except:
            self.current_input = "Error"
            self.update_current_label()
    
    def update_current_label(self):
        self.current_label.config(text=self.current_input[:12])
    
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()