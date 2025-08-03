# My Calculator App
This is a modern calculator built with Python and Tkinter.
Created for fun using Python’s Tkinter module.


Overview
This is a modern, visually appealing calculator application built using Python and Tkinter. It performs basic arithmetic operations with a clean, dark-themed interface that follows contemporary design principles. The calculator features a dual-display system showing both the current input and the complete operation expression.

Features
Basic Arithmetic Operations:

Addition (+)

Subtraction (-)

Multiplication (×)

Division (÷)

Advanced Functions:

Clear (C) - Reset the calculator

Backspace (⌫) - Delete last digit

Toggle Sign (±) - Switch between positive/negative

Square (²) - Calculate the square of current number

Decimal Point Support

Modern UI Design:

Dark theme with orange accent buttons

Dual-display system (current input + operation history)

Responsive grid layout

Custom fonts and spacing

Visual feedback on button press

Error Handling:

Division by zero protection

Input validation

Clear error messages

Requirements
Python 3.6 or higher

Tkinter (usually included with Python installations)

How to Run
Clone the repository:

bash
git clone https://github.com/Daniel-Dadzie/Calculator.git
cd Calculator
Run the calculator:

bash
python calculator.py
Or if you're using Python 3 specifically:

bash
python3 calculator.py
Usage Instructions
Basic Operations:

Enter numbers using digit buttons (0-9)

Use operator buttons (+, -, ×, ÷) to perform calculations

Press = to see the result

Special Functions:

C - Clear all inputs and reset calculator

⌫ - Delete the last entered digit

± - Toggle positive/negative sign of current number

² - Calculate square of current number

. - Add decimal point

Keyboard Support:

Numeric keys (0-9) for number input

Operators: +, -, *, /

Enter key for equals (=)

Backspace key for delete (⌫)

Escape key for clear (C)

Code Structure
The calculator is implemented in a single Python file with the following components:

Calculator Class:

Handles all calculator operations and state management

Maintains current input, total expression, and operation state

UI Components:

create_display() - Creates the dual-display system

create_buttons() - Builds the calculator button grid

configure_grid() - Sets up responsive layout

Event Handling:

on_button_click() - Main button handler

Mathematical operation methods (add, subtract, multiply, divide)

Utility methods (clear, backspace, toggle_sign, square)

Customization Options
You can easily customize the calculator by modifying these variables:

Color Scheme:

Background: #2E2E2E

Number buttons: #505050

Function buttons: #3B3B3B

Operator buttons: #FF9500

Fonts:

Display font: Helvetica, 24pt

Button font: Helvetica, 16pt

Dimensions:

Window size: 350x500 pixels

Button padding: 2px

License
This project is open-source and free to use.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

🙋‍♂️ Author
Daniel Yaw Dadzie

📧 Email: ddadzie120@gmail.com

🌐 Portfolio Website

🔗 GitHub | LinkedIn



Enjoy calculating with this sleek, modern calculator!

>>>>>>> 3425a9d (Fresh start for Calculator-App)
