import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import re
from ttkbootstrap import Style
from code_size import count_lines_of_code
from cyclomatic_comp import calculate_cyclomatic_complexity_ast
from internal_reusability import calculate_internal_reusability
from portability import calculate_portability
from defect_density import calculate_defect_density
from halstead_measure import calculate_halstead_measure_from_file

def display_python_code(filepath, text_widget):
    try:
        with open(filepath, 'r') as file:
            code = file.read()
            text_widget.config(state="normal")  # Set state to "normal" to enable editing
            text_widget.delete('1.0', tk.END)
            text_widget.insert(tk.END, code)
            text_widget.config(state="disabled")  # Set state back to "disabled" to prevent editing
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file: {e}")

def show_code_size():
    global analysis_func
    filepath = filedialog.askopenfilename(title="Select Python File")
    if filepath:
        ncloc, cloc, analysis = count_lines_of_code(filepath)
        total_loc = ncloc + cloc
        result_text = f"Effective Lines of Code (NCLOC): {ncloc}\nComment Lines (CLOC): {cloc}\nTotal Size (LOC): {total_loc}\n"
        if total_loc != 0:
            comment_density = cloc / total_loc
            result_text += f"Comment Density (CLOC/LOC): {comment_density:.2f}\n"
        else:
            result_text += "Total Size is 0, cannot calculate Comment Density\n"
        result_label.config(text=result_text)
        
        # Display code in the text widget
        display_python_code(filepath, code_size_text)

        # Set the analysis function
        analysis_func = lambda: analysis

def show_cyclomatic_complexity():
    global analysis_func
    filepath = filedialog.askopenfilename(title="Select Python File")
    if filepath:
        complexity, analysis = calculate_cyclomatic_complexity_ast(filepath)
        result_label.config(text=f"Cyclomatic complexity: {complexity}")
        
        # Display code in the text widget
        display_python_code(filepath, cyclomatic_text)

        # Set the analysis function
        analysis_func = lambda: analysis

def show_internal_reusability():
    global analysis_func
    filepath = filedialog.askopenfilename(title="Select Python File")
    if filepath:
        reusability, analysis = calculate_internal_reusability(filepath)
        result_label.config(text=f"Internal Reusability (rG): {reusability}")
        
        # Display code in the text widget
        display_python_code(filepath, reusability_text)

        # Set the analysis function
        analysis_func = lambda: analysis

def show_portability():
    global analysis_func
    ET_input = et_entry.get()
    ER_input = er_entry.get()
    
    # Use regular expression to filter out non-numeric characters
    ET = float(re.sub("[^0-9.]", "", ET_input))
    ER = float(re.sub("[^0-9.]", "", ER_input))
    
    portability_score, analysis = calculate_portability(ET, ER)
    if portability_score is not None:
        result_label.config(text=f"The portability score is: {portability_score}")
        
        # Set the analysis function
        analysis_func = lambda: analysis

def show_defect_density():
    global analysis_func
    known_defects_input = known_defects_entry.get()
    product_size_input = product_size_entry.get()
    
    # Use regular expression to filter out non-numeric characters
    known_defects = int(re.sub("[^0-9]", "", known_defects_input))
    product_size = int(re.sub("[^0-9]", "", product_size_input))
    
    defect_density, analysis = calculate_defect_density(known_defects, product_size)
    if defect_density is not None:
        result_label.config(text=f"The defect density is: {defect_density}")
        
        # Set the analysis function
        analysis_func = lambda: analysis

def show_halstead_measure():
    global analysis_func
    filepath = filedialog.askopenfilename(title="Select Python File")
    if filepath:
        halstead_measure, analysis = calculate_halstead_measure_from_file(filepath)
        result_label.config(text=f"Halstead Measure: {halstead_measure}")
        
        # Display code in the text widget
        display_python_code(filepath, halstead_text)

        # Set the analysis function
        analysis_func = lambda: analysis

def clear_result():
    global analysis_func
    result_label.config(text="")
    et_entry.delete(0, tk.END)
    er_entry.delete(0, tk.END)
    known_defects_entry.delete(0, tk.END)
    product_size_entry.delete(0, tk.END)
    code_size_text.config(state="normal")
    code_size_text.delete('1.0', tk.END)
    code_size_text.config(state="disabled")
    cyclomatic_text.config(state="normal")
    cyclomatic_text.delete('1.0', tk.END)
    cyclomatic_text.config(state="disabled")
    reusability_text.config(state="normal")
    reusability_text.delete('1.0', tk.END)
    reusability_text.config(state="disabled")
    halstead_text.config(state="normal")
    halstead_text.delete('1.0', tk.END)
    halstead_text.config(state="disabled")
    combined_text.config(state="normal")
    combined_text.delete('1.0', tk.END)
    combined_text.config(state="disabled")
    analysis_func = None

def show_analysis():
    global analysis_func
    analysis_text = ""
    if analysis_func:
        analysis_text = analysis_func()
    if analysis_text:
        # Create a custom dialog for analysis
        analysis_dialog = tk.Toplevel(root)
        analysis_dialog.title("Result Analysis")

        # Apply the selected theme to the analysis dialog
        selected_theme = theme_var.get()
        style = ttk.Style(analysis_dialog)
        style.theme_use(selected_theme)

        # Customize label background, foreground, and font
        style.configure('Custom.TLabel', background='#282c34', foreground='white', font=('Roboto', 12))

        # Add a label to display the analysis text
        analysis_label = ttk.Label(analysis_dialog, text=analysis_text, style='Custom.TLabel', wraplength=400)
        analysis_label.pack(padx=20, pady=10)

        # Add a close button
        close_button = ttk.Button(analysis_dialog, text="Close", command=analysis_dialog.destroy)
        close_button.pack(pady=10)
    else:
        messagebox.showinfo("Result Analysis", "No result to analyze.")

def calculate_all_metrics():
    filepath = filedialog.askopenfilename(title="Select Python File")
    if filepath:
        # Calculate code size
        ncloc, cloc, analysis = count_lines_of_code(filepath)
        total_loc = ncloc + cloc
        result_text = f"Effective Lines of Code (NCLOC): {ncloc}\nComment Lines (CLOC): {cloc}\nTotal Size (LOC): {total_loc}\n"
        if total_loc != 0:
            comment_density = cloc / total_loc
            result_text += f"Comment Density (CLOC/LOC): {comment_density:.2f}\n"
        else:
            result_text += "Total Size is 0, cannot calculate Comment Density\n"

        # Calculate cyclomatic complexity
        complexity, analysis_cyclomatic = calculate_cyclomatic_complexity_ast(filepath)
        result_text += f"Cyclomatic Complexity: {complexity}\n"

        # Calculate internal reusability
        reusability, analysis_reusability = calculate_internal_reusability(filepath)
        result_text += f"Internal Reusability (rG): {reusability}\n"

        # Calculate Halstead Measure
        halstead_measure, analysis_halstead = calculate_halstead_measure_from_file(filepath)
        result_text += f"Halstead Measure: {halstead_measure}\n"

        result_label.config(text=result_text)

        # Display code in the text widget
        display_python_code(filepath, combined_text)

        # Set the analysis function
        global analysis_func
        analysis_func = lambda: f"{analysis}\n{analysis_cyclomatic}\n{analysis_reusability}\n{analysis_halstead}"


root = tk.Tk()
root.title("Metrics Tool")

# Apply TTKBootstrap style
style = Style(theme='vapor')

# Configure font settings
#style.configure('.', font=('Roboto', 12)) 

root.iconbitmap('Metrics.ico')

# Create a notebook-style navigation bar
navbar = ttk.Notebook(root)

# Frame for Code Size metric
code_size_frame = ttk.Frame(navbar)
navbar.add(code_size_frame, text="Code Size")

# Description label for Code Size
code_size_description = ttk.Label(code_size_frame, text="\nCode Size represents the total number of lines in your codebase.\nIt includes both effective lines of code (NCLOC) and comment lines (CLOC).\nAnalyzing code size helps in understanding the overall complexity and maintenance effort required for the project.\n")
code_size_description.pack()

code_size_button = ttk.Button(code_size_frame, text="Calculate Code Size", command=show_code_size)
code_size_button.pack(pady=10)

code_size_text = tk.Text(code_size_frame, height=25, width=100, state="disabled")
code_size_text.pack(pady=10)

# Frame for Cyclomatic Complexity metric
cyclomatic_frame = ttk.Frame(navbar)
navbar.add(cyclomatic_frame, text="Cyclomatic Complexity")

# Description label for Cyclomatic Complexity
cyclomatic_description = ttk.Label(cyclomatic_frame, text="\nCyclomatic Complexity measures the complexity of a program by counting the number of decision points in the code.\nIt helps in identifying complex areas that may require refactoring or further testing.\n")
cyclomatic_description.pack()

cyclomatic_button = ttk.Button(cyclomatic_frame, text="Calculate Cyclomatic Complexity", command=show_cyclomatic_complexity)
cyclomatic_button.pack(pady=10)

cyclomatic_text = tk.Text(cyclomatic_frame, height=25, width=100, state="disabled")
cyclomatic_text.pack(pady=10)

# Frame for Internal Reusability metric
reusability_frame = ttk.Frame(navbar)
navbar.add(reusability_frame, text="Internal Reusability")

# Description label for Internal Reusability
reusability_description = ttk.Label(reusability_frame, text="\nInternal Reusability (rG) measures the degree to which code within a software system is reused.\nIt helps in assessing the maintainability and scalability of the codebase.\n")
reusability_description.pack()

reusability_button = ttk.Button(reusability_frame, text="Calculate Internal Reusability", command=show_internal_reusability)
reusability_button.pack(pady=10)

reusability_text = tk.Text(reusability_frame, height=25, width=100, state="disabled")
reusability_text.pack(pady=10)

# Frame for Halstead Measure metric
halstead_frame = ttk.Frame(navbar)
navbar.add(halstead_frame, text="Halstead Measure")

# Description label for Halstead Measure
halstead_description = ttk.Label(halstead_frame, text="\nHalstead Measure quantifies the complexity of a program by analyzing the number of unique operators and operands.\nIt helps in understanding the effort required to understand and maintain the code.\n")
halstead_description.pack()

halstead_button = ttk.Button(halstead_frame, text="Calculate Halstead Measure", command=show_halstead_measure)
halstead_button.pack(pady=10)

halstead_text = tk.Text(halstead_frame, height=25, width=100, state="disabled")
halstead_text.pack(pady=10)

# Frame for Portability metric
portability_frame = ttk.Frame(navbar)
navbar.add(portability_frame, text="Portability")

# Description label for Portability
portability_description = ttk.Label(portability_frame, text="\nPortability assesses how easily a software system can be adapted to different environments or platforms.\nIt helps in ensuring that the software can be deployed and run efficiently across various settings.\n")
portability_description.pack()

et_label = ttk.Label(portability_frame, text="Enter ET (resources needed to move the system to the target environment):")
et_label.pack(pady=5)
et_entry = ttk.Entry(portability_frame)
et_entry.pack(pady=5)
er_label = ttk.Label(portability_frame, text="Enter ER (resources needed to create the system for the resident environment):")
er_label.pack(pady=5)
er_entry = ttk.Entry(portability_frame)
er_entry.pack(pady=5)
portability_button = ttk.Button(portability_frame, text="Calculate Portability", command=show_portability)
portability_button.pack(pady=10)

# Frame for Defect Density metric
defect_density_frame = ttk.Frame(navbar)
navbar.add(defect_density_frame, text="Defect Density")

# Description label for Defect Density
defect_density_description = ttk.Label(defect_density_frame, text="\nDefect Density measures the number of defects per unit of code size.\nIt helps in assessing the quality and reliability of the software by identifying areas with higher defect rates.\n")
defect_density_description.pack()

known_defects_label = ttk.Label(defect_density_frame, text="Enter the number of known defects:")
known_defects_label.pack(pady=5)
known_defects_entry = ttk.Entry(defect_density_frame)
known_defects_entry.pack(pady=5)
product_size_label = ttk.Label(defect_density_frame, text="Enter the product size (measured in lines of code or function points):")
product_size_label.pack(pady=5)
product_size_entry = ttk.Entry(defect_density_frame)
product_size_entry.pack(pady=5)
defect_density_button = ttk.Button(defect_density_frame, text="Calculate Defect Density", command=show_defect_density)
defect_density_button.pack(pady=10)

# Frame for Combined Metrics
combined_frame = ttk.Frame(navbar)
navbar.add(combined_frame, text="All Codebase Metrics")

# Description label for Combined Metrics
combined_description = ttk.Label(combined_frame, text="\nThis section provides a consolidated view of all metrics calculated for the codebase.\n")
combined_description.pack()

combined_button = ttk.Button(combined_frame, text="Calculate All Metrics", command=calculate_all_metrics)
combined_button.pack(pady=10)

combined_text = tk.Text(combined_frame, height=25, width=100, state="disabled")
combined_text.pack(pady=10)

# Add the navigation bar to the main window
navbar.pack(expand=1, fill="both")

# Frame for Theme Selection
theme_frame = ttk.Frame(root)
theme_frame.pack(side="bottom", padx=10, pady=10, anchor="sw")

# Theme label
theme_label = ttk.Label(theme_frame, text="Select Theme:")
theme_label.grid(row=0, column=0, padx=5)

# Theme dropdown
available_themes = style.theme_names()
theme_var = tk.StringVar(value=available_themes[0])
theme_dropdown = ttk.Combobox(theme_frame, textvariable=theme_var, values=available_themes, state="readonly", width=20)
theme_dropdown.grid(row=0, column=1, padx=5)


# Change theme function
def change_theme():
    selected_theme = theme_var.get()
    style.theme_use(selected_theme)
    root.update()

# Apply theme change on dropdown selection
theme_dropdown.bind('<<ComboboxSelected>>', lambda event: change_theme())

# Frame for Result
result_frame = ttk.Frame(root)
result_frame.pack(pady=10)

# Result label
result_label = ttk.Label(result_frame, text="", font=('Roboto', 14))
result_label.pack()

# Frame for Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Buttons
clear_button = ttk.Button(button_frame, text="Clear", command=clear_result)
clear_button.grid(row=0, column=0, padx=5)

analyze_button = ttk.Button(button_frame, text="Analyze", command=show_analysis)
analyze_button.grid(row=0, column=1, padx=5)

exit_button = ttk.Button(button_frame, text="Exit", command=root.quit)
exit_button.grid(row=0, column=2, padx=5)

root.mainloop()
