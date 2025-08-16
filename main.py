# Simple GUI Calculator using tkinter
# Step 1: Import tkinter
import tkinter as tk

# Step 2: Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Step 3: Create an entry widget to show numbers/results
entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Step 4: Functions for calculator operations
def button_click(value):
	entry.insert(tk.END, value)

def button_clear():
	entry.delete(0, tk.END)

def button_equal():
	try:
		result = eval(entry.get())
		entry.delete(0, tk.END)
		entry.insert(tk.END, str(result))
	except:
		entry.delete(0, tk.END)
		entry.insert(tk.END, "Error")

# Step 5: Create buttons for numbers and operations
buttons = [
	('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
	('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
	('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
	('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
	if text == '=':
		action = button_equal
	else:
		action = lambda x=text: button_click(x)
	tk.Button(root, text=text, width=5, height=2, font=('Arial', 16), command=action).grid(row=row, column=col, padx=5, pady=5)

# Step 6: Add a clear button
tk.Button(root, text='C', width=5, height=2, font=('Arial', 16), command=button_clear).grid(row=5, column=0, columnspan=4, sticky='we', padx=5, pady=5)

# Step 7: Start the GUI event loop
root.mainloop()
# Simple Calculator Program
# Step 1: Show a menu for the user to choose an operation
print("Welcome to the Simple Calculator!")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Step 2: Get the user's choice
choice = input("Enter the number corresponding to your choice (1-4): ")

# Step 3: Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 4: Perform the chosen operation
if choice == '1':
	result = num1 + num2
	print(f"{num1} + {num2} = {result}")
elif choice == '2':
	result = num1 - num2
	print(f"{num1} - {num2} = {result}")
elif choice == '3':
	result = num1 * num2
	print(f"{num1} * {num2} = {result}")
elif choice == '4':
	if num2 != 0:
		result = num1 / num2
		print(f"{num1} / {num2} = {result}")
	else:
		print("Error: Cannot divide by zero!")
else:
	print("Invalid choice. Please run the program again.")
